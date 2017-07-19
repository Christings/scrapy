# -*- coding:utf-8 -*-

from scrapy.conf import settings
import scrapy
import requests
import re


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

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse_urls, cookies=self.cookie, headers=self.headers,
                             meta=self.meta)

    def parse_urls(self, response):
        # item = WorldBankItem()
        # selector = scrapy.Selector(response)
        #
        # indicators = selector.xpath('//*[@id="main"]/div[2]')
        # # url = response.xpath('//*[@id="main"]/div[2]/section[1]/ul[2]/li[3]/a/@href').extract()
        # # print('==\n', url, '==\n')
        # # for each in indicators:
        # indi_name_en = indicators.xpath('section[@class="nav-item"]/ul/li/a/@href').extract()
        # # indi = re.findall(r'/indicator/.*/?view=chart', indicators, re.S)
        # indi_name_cn = indicators.xpath('section[@class="nav-item"]/ul/li/a/text()').extract()
        # # items=[]

        selector = scrapy.Selector(response)
        catalog_number = selector.xpath('//table[@id="dgPzCommodities"]/tr/td[1]/a/text()').extract()
        catalog = selector.xpath(u'//table[@id="dgPzCommodities"]/tr/td[2]/text()').extract()
        del (catalog[0:4])
        print("1", catalog_number)
        # y=catalog.remove('\r\n\t\t\t')
        # b=str(catalog).strip()
        #
        # import string
        # s = "a\nb\rc\td"
        # x=str(catalog)
        # print(x.translate(str.maketrans('\r\n\t\t\t', "     ")))

        # del (catalog[0])
        # # cat = str(catalog)
        for i in catalog:
            # if cat[i] == '\r\n\t\t\t\t' or cat[i] == '\r\n\t\t\\t':
            #     del (cat[i])
            row = i.replace('\r', '').replace('\n', '').replace('\t', '')
            if row != "":
                print("123:", row)

        for j in catalog_number:
            # if cat[i] == '\r\n\t\t\t\t' or cat[i] == '\r\n\t\t\\t':
            #     del (cat[i])
            row1 = j.replace('\xa0\xa0', '')
            if row1 != "":
                print("1234:", row1)


                        # row = row.replace('\r', '').replace('\n', '').replace('\t', '')
                # catalog[i].strip()

        # catalog_level1_name = catalog.xpath('tr[@class="theader"]/td/text()').extract()
        # for each in catalog:
        #     each = each[1:]
        #     print("each:", each)
        # x = str(catalog)
        # x.replace(":", "")
        # name = re.findall("\'(.*)\'", x, re.S)
        # print("name", x)
        print("111", catalog)
        print("bbb", y)
        # print("111", x)
