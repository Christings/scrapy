# -*- coding:utf-8 -*-
import scrapy
import requests
from saas.items import WorldBankItem


class WorldBankSpider(scrapy.Spider):
    name = "worldbank"
    excel_url = "http://api.worldbank.org/v2/zh/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel"
    output_path = './test.xls'
    # start_url = 'http://data.worldbank.org.cn/indicator?tab=all'
    start_url = 'https://comtrade.un.org/db/dqBasicQueryResults.aspx?cc=all,%2002*&px=H0&r=all&y=all&p=all&rg=1,2&tv1=1&tv2=0&so=9999&rpage=dqBasicQuery&qt=y'

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse_urls)

    def parse_urls(self, response):
        # url = response.xpath(
        #     '//*[@id="main"]/div[2]/section[1]/ul[2]/li[3]/a/@href').extract()
        # print('==\n', url, '==\n')
        url = response.body
        print("url:" + url)
