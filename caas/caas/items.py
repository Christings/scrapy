# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 世界银行数据
class WorldBankItem(scrapy.Item):
    # 定义需要格式化的内容（或是需要保存到数据库的字段）
    indi_url = scrapy.Field()  # 指标(indicator)的url的字段
    indi_name = scrapy.Field()  # 指标(indicator)的名字


# Comtrade————CountryList数据
class ComtradeCountryListItem(scrapy.Item):
    country_code=scrapy.Field()  # 国家代号
    country_name=scrapy.Field()  # 国家名称


# Comtrade————CommodityList数据
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

# FAO数据
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

    first = scrapy.Field()
    second = scrapy.Field()
    third = scrapy.Field()
