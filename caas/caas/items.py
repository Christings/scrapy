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

    catalog_year = scrapy.Field()  # 年份
    catalog_level1_num = scrapy.Field()  # 编号
    catalog_level1_name = scrapy.Field()  # 名称
    catalog_level1_desc = scrapy.Field()  # 描述


class ComtradeCatalogLevel2Item(scrapy.Item):
    # 二级目录
    # catalog_level2_url = scrapy.Field()
    catalog_level2_num = scrapy.Field()
    catalog_level2_name = scrapy.Field()
    catalog_level2_desc = scrapy.Field()


class ComtradeCatalogLevel3Item(scrapy.Item):
    # 三级目录
    catalog_level3_url = scrapy.Field()
    catalog_level3_num = scrapy.Field()
    catalog_level3_name = scrapy.Field()
    catalog_level3_desc = scrapy.Field()


class ComtradeCatalogLevel4Item(scrapy.Item):
    # 四级目录
    catalog_level4_url = scrapy.Field()
    catalog_level4_num = scrapy.Field()
    catalog_level4_name = scrapy.Field()
    catalog_level4_desc = scrapy.Field()


class FaoCountriesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # geo_country1 = scrapy.Field()
    # geo_country2 = scrapy.Field()
    # geo_country3 = scrapy.Field()
    #
    # eco_country1 = scrapy.Field()
    # eco_country2 = scrapy.Field()
    # eco_country3 = scrapy.Field()

    first=scrapy.Field()
    second=scrapy.Field()
    third=scrapy.Field()
