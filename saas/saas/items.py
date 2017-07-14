# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WorldBankItem(scrapy.Item):
    #定义需要格式化的内容（或是需要保存到数据库的字段）
    indi_name_en = scrapy.Field()   #指标(indicator)的url
    indi_name_cn = scrapy.Field()   #指标(indicator)的名字


# class SaasItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
