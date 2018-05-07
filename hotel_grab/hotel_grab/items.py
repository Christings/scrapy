# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CtripItem(scrapy.Item):
    # define the fields for your item here like:
    houseType = scrapy.Field()
    housePrice = scrapy.Field()
    bookingStatus = scrapy.Field()
    userId = scrapy.Field()
    hotelComments = scrapy.Field()
class ELongItem(scrapy.Item):
    nickName = scrapy.Field()
    content = scrapy.Field()
    houseType = scrapy.Field()
