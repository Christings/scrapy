# -*- coding:utf-8 -*-
import scrapy
from scrapy.conf import settings

class ComtradeCountryListSpider(scrapy.Spider):
    name = "comtradecountrylist"
    start_url="https://comtrade.un.org/db/mr/rfReportersList.aspx"

    cookie = settings['COOKIES']

    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    }

    meta = {
        'dont_redirct': True,
        'handle_httpstatus_list': [301, 302]
    }

    def start_requests(self):
        # self.start_url.split("&")[0]
        yield scrapy.Request(url=self.start_url, callback=self.parse, cookies=self.cookie, headers=self.headers,
                             meta=self.meta)

    def parse(self, response):
        print(response.body)