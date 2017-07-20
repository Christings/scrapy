# -*- coding:utf-8 -*-

from scrapy.conf import settings
import scrapy
from scrapy.item import i
import requests
import re
from caas.items import ComtradeCatalogItem


class ComtradeCatalogSpider(scrapy.Spider):
    name = "comtradecatalog"
    # 1.一级目录url，调整的关键字为px=H0-H4,S1-S4
    #   https: //comtrade.un.org/db/mr/rfCommoditiesList.aspx?px = H0 & cc = TOTAL
    # 2.二级子目录url，调整的关键字为px=H0-H4，cc=01-99
    #   https: //comtrade.un.org/db/mr/rfCommoditiesList.aspx?px = H0 & cc = 01
    # 3.三级子目录url
    #   https: // comtrade.un.org / db / mr / rfCommoditiesList.aspx?px = H0 & cc = 0101

    start_url = "https://comtrade.un.org/db/mr/rfCommoditiesList.aspx?px=H0&cc=TOTAL"

    cookie = settings['COOKIES']

    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    }

    meta = {
        'dont_redirct': True,
        'handle_httpstatus_list': [301, 302]
    }

    output_path = './test.csv'

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse_level1, cookies=self.cookie, headers=self.headers,
                             meta=self.meta)

    # 解析一级目录
    def parse_level1(self, response):
        item = ComtradeCatalogItem()
        selector = scrapy.Selector(response)
        # 一级分类的编号、名称、描述的原始数据
        catalog_level1_number_primary = selector.xpath('//table[@id="dgPzCommodities"]/tr/td[1]/a/text()').extract()
        catalog_level1_primary = selector.xpath(u'//table[@id="dgPzCommodities"]/tr/td[2]/text()').extract()

        catalog_level1_number_list = []
        # 提取一级分类编号的有用字段，去除空格等。
        for each in catalog_level1_number_primary:
            catalog_level1_num = each.replace('\xa0\xa0', '')
            if catalog_level1_num != "":
                # print("catalog_level1_number:", catalog_level1_num)
                # catalog_level1_number_list.append(catalog_level1_num)
                item["catalog_level1_num"] = catalog_level1_num

        # print("catalog_level1_number_list:", catalog_level1_number_list)
        # output = open(self.output_path, 'wb')
        # output.write(bytearray(catalog_level1_number_list))
        # output.close()
        # return None

        # 删除一级分类名称、描述前部无用的字段
        del (catalog_level1_primary[0:4])
        # print("1", catalog_number)

        # 提取一级分类名称、描述的有用字段
        for i, each in enumerate(catalog_level1_primary):
            catalog_level1 = each.replace('\r', '').replace('\n', '').replace('\t', '')
            if catalog_level1 != "":
                catalog_level1 = catalog_level1[1:]
                if (i % 2 == 0):
                    # catalog_level1_name = catalog_level1
                    # print("双数catalog_level1_name:", catalog_level1_name)
                    item["catalog_level1_name"] = catalog_level1
                else:
                    # catalog_level1_desc = catalog_level1
                    # print("单数catalog_level1_desc:", catalog_level1_desc)
                    item["catalog_level1_desc"] = catalog_level1
