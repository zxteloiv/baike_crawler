# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BaikeItem(scrapy.Item):
    # define the fields for your item here like:
    itemid = scrapy.Field()
    itemtype = scrapy.Field()
    url = scrapy.Field()
    anchor = scrapy.Field()
    body = scrapy.Field()


