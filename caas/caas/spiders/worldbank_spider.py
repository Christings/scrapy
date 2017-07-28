# -*- coding:utf-8 -*-
import scrapy
import requests
from caas.items import WorldBankItem


class WorldBankSpider(scrapy.Spider):
    name = "worldbank"

    # excel_url = "http://api.worldbank.org/v2/zh/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel" #世界银行——中文——下载excel地址样式
    # excel_url = "http://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel" #世界银行——英文——下载excel地址样式
    # excel_url = "http://api.worldbank.org/v2/zh"
    excel_url = "http://api.worldbank.org/v2/en"

    # start_url = 'http://data.worldbank.org.cn/indicator?tab=all' #世界银行——中文——获取指标
    start_url = 'http://data.worldbank.org/indicator?tab=all'  # 世界银行——英文——获取指标

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse_urls)

    # 获取世界银行所有指标，并且进行url拼凑，再对获得的url进行请求，从而下载excel文件
    def parse_urls(self, response):
        selector = scrapy.Selector(response)

        indicators = selector.xpath('//*[@id="main"]/div[2]/section[@class="nav-item"]/ul/li')
        # content = indicators.xpath('')
        for i in indicators:
            print(i)
            item = WorldBankItem()
            temp_url = i.xpath('a/@href').extract()
            indi_url = temp_url[:-10] + "downloadformat=excel"
            item["indi_url"] = indi_url
            print('item["indi_url"]:', item["indi_url"])
            item["indi_name"] = i.xpath('a/text()').extract()
            print('item["indi_name"]:', item["indi_name"])
            yield item
