# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Player(scrapy.Item):
    id = scrapy.Field()
    season = scrapy.Field()
    team = scrapy.Field()
    name = scrapy.Field()
    short_name = scrapy.Field()
    age = scrapy.Field()
    pos = scrapy.Field()
    weight = scrapy.Field()
    height = scrapy.Field()
    exp = scrapy.Field()
    av = scrapy.Field()
    draft = scrapy.Field()
    salary = scrapy.Field()


class NflplayerattrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
