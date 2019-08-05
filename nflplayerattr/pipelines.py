# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

team_trans = {
'crd':'ARI',
'atl':'ATL',
'rav':'BAL',
'buf':'BUF',
'car':'CAR',
'chi':'CHI',
'cin':'CIN',
'cle':'CLE',
'dal':'DAL',
'den':'DEN',
'det':'DET',
'gnb':'GB',
'htx':'HOU',
'clt':'IND',
'jax':'JAX',
'kan':'KC',
'sdg':'LAC',
'ram':'LA',
'mia':'MIA',
'min':'MIN',
'nwe':'NE',
'nor':'NO',
'nyg':'NYG',
'nyj':'NYJ',
'rai':'OAK',
'phi':'PHI',
'pit':'PIT',
'sfo':'SF',
'sea':'SEA',
'tam':'TB',
'oti':'TEN',
'was':'WAS'
}

def fix_height(height):
    if height is not None:
        idx = height.index('-')
        ft = height[:idx]
        inch = height[(idx+1):]
        height = int(ft) * 12 + int(inch)
    return height

def shorten(name):
    name_split = name.split(" ")
    initials = [name[0].upper() for name in name_split[:-1]]
    return '.'.join(initials + [name_split[-1]])

class NflplayerattrPipeline(object):
    def process_item(self, item, spider):
        # replace rook with 0 year experience
        item['height'] = fix_height(item['height'])
        item['weight'] = int(item['weight'])
        item['age'] = int(item['age'])
        item['av'] = int(item['av'])
        if item['pos'] is not None:
            item['pos'] = item['pos'].upper()

        if 'exp' in item.keys():
            if item['exp'] == 'Rook':
                item['exp'] = '0'
            item['exp'] = int(item['exp'])

        item['team']=team_trans[item['team']]

        item['short_name'] = shorten(item['name'])
        item['id'] = str(item['season'])+item['team']+item['short_name']
        return item
