# coding:utf-8
import scrapy


class AmazonItem(scrapy.Item):
    book_id = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    node = scrapy.Field()
    page = scrapy.Field()
    # press = scrapy.Field()
    num_comment = scrapy.Field()


class JdItem(scrapy.Item):
    _id = scrapy.Field()
    book_id = scrapy.Field()
    price = scrapy.Field()
    num_comment = scrapy.Field()


class SyncItem(scrapy.Item):
    _id = scrapy.Field()
    jd_book_id = scrapy.Field()
    amazon_book_id = scrapy.Field()
    jd_price = scrapy.Field()
    amazon_price = scrapy.Field()
