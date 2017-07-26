import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
import logging
import re

import MySQLdb

from shanbay.items import JdItem
from shanbay.items import JdItem


class JdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["jd.com"]
    search_url = 'http://search.jd.com/Search?keyword=[word]&enc=utf-8'

    @staticmethod
    def connectDB():
        settings = get_project_settings()

        host = settings['MYSQL_HOST']
        port = settings['MYSQL_PORT']
        user = settings['MYSQL_USER']
        passwd = settings['MYSQL_PASSWD']
        db = settings['MYSQL_DBNAME']

        conn = MySQLdb.connect(host=host,
                               port=port,
                               user=user,
                               passwd=passwd,
                               charset='utf8')
        return conn

    def start_requests(self):
        cur = self.connectDB().cursor()
        cur.execute(
            """SELECT name, id FROM shanbay.books WHERE jd_book_id is NULL ORDER BY rand() LIMIT 1000;""")
        book_names = cur.fetchall()
        for book_name in book_names:
            request = scrapy.Request(self.search_url.replace('[word]', book_name[0]),
                                     callback=self.parse)
            request.meta['_id'] = book_name[1]
            yield request
        cur.close()

    def parse(self, response):
        try:
            book = response.xpath(
                '//*[@id="J_goodsList"]/ul/li[1]')
            item = self.parse_item(book, response.meta['_id'])
            yield item
        except Exception as e:
            logging.log(logging.DEBUG,
                        'XPath ERROR in JD: search page not found books=\n' + str(e))

    @staticmethod
    def parse_item(book, _id):
        item = JdItem()
        item['_id'] = _id
        try:
            item['book_id'] = book.xpath('@data-sku').extract()[0]
            item['price'] = float(book.xpath(
                './div/div[2]/strong/i/text()').extract()[0])
            try:
                item['num_comment'] = book.xpath(
                    '//*[@id="J_goodsList"]/ul/li[1]/div/div[5]/strong/a/text()').extract()[0]
            except:
                # no comment yet
                item['num_comment'] = 0
            print(item, '====\n')

        except Exception as e:
            logging.log(logging.ERROR, 'XPath ERROR in JD: book detail page error' +
                        str(item) + '\n--\n' + str(e))
        return item
