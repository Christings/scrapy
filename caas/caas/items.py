# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ComtradeCatalogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 一级目录
    # catalog_level1_url = scrapy.Field()  # url
    catalog_level1_num = scrapy.Field()  # 编号
    catalog_level1_name = scrapy.Field()  # 名称
    catalog_level1_desc = scrapy.Field()  # 描述

    # 二级目录
    # catalog_level2_url = scrapy.Field()
    # catalog_level2_num = scrapy.Field()
    # catalog_level2_name = scrapy.Field()
    # catalog_level2_desc = scrapy.Field()

    # 三级目录
    # catalog_level3_url = scrapy.Field()
    # catalog_level3_num = scrapy.Field()
    # catalog_level3_name = scrapy.Field()
    # catalog_level3_desc = scrapy.Field()


class CaasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
