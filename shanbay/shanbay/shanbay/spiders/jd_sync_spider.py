# coding:utf-8
import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
import logging
import re
import json

import MySQLdb

from shanbay.items import SyncItem


class JdSyncSpider(scrapy.Spider):
    name = "jd-sync"
    allowed_domains = ["jd.com"]

    # jd price ajax url
    # jd_ajax_url = 'http://p.3.cn/prices/get?&skuid=J_[word]'
    jd_ajax_url = 'http://p.3.cn/prices/get?&pduid=14976113975431895909603&skuid=J_[word]'

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
            """SELECT id, jd_book_id
               FROM shanbay.books
               WHERE jd_book_id IS NOT NULL
               ORDER BY jd_update_time
               LIMIT 10;""")
        books = cur.fetchall()
        for book in books:
            item = SyncItem()
            item['_id'] = book[0]
            item['jd_book_id'] = book[2]
            jd_request = scrapy.Request(self.jd_ajax_url.replace(
                '[word]', item['jd_book_id']), callback=self.jd_parse)
            jd_request.meta['item'] = item
            yield jd_request

        cursor.close()

    def jd_parse(self, response):
        item = response.meta['item']
        try:
            jsonresponse = json.loads(response.body_as_unicode())
            item['jd_price'] = jsonresponse[0]['p']
        except Exception as e:
            logging.log(logging.DEBUG,
                        'XPath ERROR in sync-JD: =\n' + str(e))

        yield item
