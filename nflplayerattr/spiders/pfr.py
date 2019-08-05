# -*- coding: utf-8 -*-
import scrapy

from scrapy.selector import Selector

from nflplayerattr.items import Player
from nflplayerattr.pfr_settings import *

class PfrSpider(scrapy.Spider):
    name = 'pfr'
    allowed_domains = ['pro-football-reference.com']
    start_urls = ['http://pro-football-reference.com/']

    def generate_urls(self):
        urls = []
        seasons = range(START_YEAR, END_YEAR+1)
        for season in seasons:
            for team in TEAM_ABBR:
                url_obj = {}
                url_obj['season'] = season
                url_obj['team'] = team
                url_obj['url'] = 'https://www.pro-football-reference.com/teams/'+team+'/'+str(season)+'_roster.htm'
                urls.append(url_obj)
        return urls

    def start_requests(self):
        urls = self.generate_urls()

        # test
        # urls = urls[:1]

        for url in urls:
            request = scrapy.Request(url=url['url'], callback=self.parse)
            request.meta['season'] = url['season']
            request.meta['team'] = url['team']

            print(url['season'], url['team'])
            print(url['season'], url['team'])
            print(url['season'], url['team'])
            print(url['season'], url['team'])

            yield request

    def parse(self, response):
        extracted_text = response.xpath('//div[@id="all_games_played_team"]//comment()').extract()[0]
        new_selector = Selector(text=extracted_text[4:-3].strip())
        rows = new_selector.xpath('//*[@id="games_played_team"]/tbody//tr')
        for row in rows:
            player = Player()
            cells = row.css('td')
            if len(cells) == 12:
                player['season'] = response.meta['season']
                player['team'] = response.meta['team']
                player['name'] = cells[0].css('::text').get()
                player['age'] = cells[1].css('::text').get()
                player['pos'] = cells[2].css('::text').get()
                player['weight'] = cells[5].css('::text').get()
                player['height'] = cells[6].css('::text').get()
                player['exp'] = cells[9].css('::text').get()
                player['av'] = cells[10].css('::text').get()
                player['draft'] = cells[11].css('::text').get()
            elif len(cells) == 13:
                player['season'] = response.meta['season']
                player['team'] = response.meta['team']
                player['name'] = cells[0].css('::text').get()
                player['age'] = cells[1].css('::text').get()
                player['pos'] = cells[2].css('::text').get()
                player['weight'] = cells[5].css('::text').get()
                player['height'] = cells[6].css('::text').get()
                player['exp'] = cells[9].css('::text').get()
                player['av'] = cells[10].css('::text').get()
                player['draft'] = cells[11].css('::text').get()
                player['salary'] = cells[12].css('::text').get()
            yield player
