# -*- coding:utf-8 -*-
import scrapy
import requests
import re
from saas.items import WorldBankItem


class WorldBankSpider(scrapy.Spider):
    name = "worldbank"
    # excel_url = "http://api.worldbank.org/v2/zh/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel"
    excel_url = "http://api.worldbank.org/v2/zh"
    # output_path = './test.xls'
    start_url = 'http://data.worldbank.org.cn/indicator?tab=all'

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse_urls)


    def parse_urls(self, response):
        item = WorldBankItem()
        selector = scrapy.Selector(response)

        indicators = selector.xpath('//*[@id="main"]/div[2]')
        # url = response.xpath('//*[@id="main"]/div[2]/section[1]/ul[2]/li[3]/a/@href').extract()
        # print('==\n', url, '==\n')
        # for each in indicators:
        indi_name_en = indicators.xpath('section[@class="nav-item"]/ul/li/a/@href').extract()

        # indi = re.findall(r'/indicator/.*/?view=chart', indicators, re.S)
        indi_name_cn = indicators.xpath('section[@class="nav-item"]/ul/li/a/text()').extract()
        # items=[]
        for i in indi_name_en:
            # print("indi_name_en:", i)
            i = i[:-10] + "downloadformat=excel"
            # i.replace("view=chart", "downloadformat=excel")
            item['indi_name_en'] = i
            # items.append(item)
        for j in indi_name_cn:
            print("indi_name_cn:", j)
            item['indi_name_cn'] = j
            # items.append(item)

            yield item

# -*- coding:utf-8 -*-

# import scrapy
# import requests
# from saas.items import WorldBankItem
#
#
# class WorldBankSpider(scrapy.Spider):
#     name = "worldbank"
#
#     word = input("Input key word: ")
#     excel_url = 'http://api.worldbank.org/v2/zh/indicator/NY.GDP.MKTP.KD.ZG?'+word+'downloadformat=excel'
#
#     # excel_url = "http://api.worldbank.org/v2/zh/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel"
#     output_path = './test.xls'
#
#     def start_requests(self):
#         url = self.excel_url
#         resp = requests.get(self.excel_url)
#         output = open(self.output_path, 'wb')
#         output.write(resp.content)
#         output.close()
#         return None
#
#         # def parse(self, response):
#         #     start_urls = ("http://api.worldbank.org/v2/zh/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel",)
#         #
#         #     resp = requests.get(start_urls)
#         #
#         #     output = open('test.xls', 'wb')
#         #     output.write(resp.content)
#         #     output.close()
#         # print(response.body)
#
# # item = WorldBankItem()
# # selector = scrapy.Selector(response)
# # content = selector.xpath('//div[@id="homepage"]')
# # for each in content:
# #     title = each.xpath('h1[@class="app-title"]/span/text()').extract()[0]
# #     item['title']=title
# #     print("title:", item['title'])
# #     yield item
