# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    domain = scrapy.Field()
    url = scrapy.Field()
    comname = scrapy.Field()
    typename = scrapy.Field()
    comdemo = scrapy.Field()
    areaname = scrapy.Field()
    address = scrapy.Field()
    tel = scrapy.Field()
    email = scrapy.Field()


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    domain = scrapy.Field()
    comurl = scrapy.Field()
    url = scrapy.Field()
    comname = scrapy.Field()
    jobname = scrapy.Field()
    jobdemo = scrapy.Field()
    areaname = scrapy.Field()
    address = scrapy.Field()
    salary = scrapy.Field()
    eduname = scrapy.Field()
    jobyear = scrapy.Field()
    begindate = scrapy.Field()
    enddate = scrapy.Field()
    fuli = scrapy.Field()
    tradename = scrapy.Field()
