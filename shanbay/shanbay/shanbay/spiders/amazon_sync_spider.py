# coding:utf-8
import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
import logging
import re
import json

import MySQLdb

from shanbay.items import SyncItem


class AmazonSyncSpider(scrapy.Spider):
    name = "amazon-sync"
    allowed_domains = ["amazon.cn"]
    DOWNLOAD_DELAY = 2
    CONCURRENT_REQUESTS = 10

    amazon_base_url = 'https://www.amazon.cn/dp/[word]'

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
        # 同步数据amazon数据
        cur.execute(
            """(SELECT id, amazon_book_id
                FROM shanbay.books
                WHERE amazon_price = '[]' limit 2)
            UNION
               (SELECT id, amazon_book_id
               FROM shanbay.books
               ORDER BY amazon_update_time
               LIMIT 2);""")
        books = cur.fetchall()
        for book in books:
            item = SyncItem()
            item['_id'] = book[0]
            item['amazon_book_id'] = book[1]

            amazon_request = scrapy.Request(self.amazon_base_url.replace(
                '[word]', item['amazon_book_id']), callback=self.amazon_parse)
            amazon_request.meta['item'] = item
            yield amazon_request

        cur.close()

    def amazon_parse(self, response):
        item = response.meta['item']
        try:
            price_lis = response.xpath('//*[@id="tmmSwatches"]/ul/li')
        except Exception as e:
            logging.log(
                logging.ERROR, 'XPath ERROR in sync-Amazon:Not get price <li>' + str(e))
            return
        item['amazon_price'] = []
        for li in price_lis:
            try:
                pack = li.xpath(
                    './span/span[1]/span[1]/a/span[1]/text()').extract()[0]
                price = float(li.xpath(
                    './span/span[1]/span[1]/a/span[2]/span/text()').extract()[0].strip()[1:])
                if price:
                    # '精装', '平装', 'Kindle'
                    if u'精装' in pack:
                        item['amazon_price'].append((0, price))
                    elif u'平装' in pack:
                        item['amazon_price'].append((1, price))
                    elif u'Kindle' in pack:
                        item['amazon_price'].append((2, price))
            except Exception as e:
                logging.log(logging.ERROR,
                            'XPath ERROR in sync-Amazon: =\n' + str(e))
        yield item
