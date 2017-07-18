# -*- coding:utf-8 -*-
import scrapy
import requests
import re
from saas.items import WorldBankItem


class WorldBankSpider(scrapy.Spider):
    name = "worldbank"
    filenames = []
    # excel_url = "http://api.worldbank.org/v2/zh/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel" #世界银行——中文——下载excel地址样式
    # excel_url = "http://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel" #世界银行——英文——下载excel地址样式
    # excel_url = "http://api.worldbank.org/v2/zh"
    excel_url = "http://api.worldbank.org/v2/en"

    # output_path = './test.xls'
    # start_url = 'http://data.worldbank.org.cn/indicator?tab=all' #世界银行——中文——获取指标
    start_url = 'http://data.worldbank.org/indicator?tab=all'  # 世界银行——英文——获取指标

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
            # i.replace("view=chart", "downloadformat=excel") #使用replace进行替换时总是不成功，有待探索！
            item['indi_name_en'] = i
            # items.append(item)
            yield scrapy.Request(url="http://api.worldbank.org/v2/en" + i, callback=self.download_excel)
        for j in indi_name_cn:
            print("indi_name_cn:", j)
            item['indi_name_cn'] = j
            self.filenames = indi_name_cn
            # items.append(item)

    def download_excel(self, response):
        # print("url:"+response.url)
        # excel_url = response.url
        name_temp = response.url.split("/")[-1]
        name = name_temp.split("?")[-2]
        print("name:", name)
        # for each in self.filenames:
        #     # print("name:" + name)
        #     self.filenames.index()
        filename = r"D:\workspace\scrapy\saas\worldbankexcelfiles\%s.xls" % name
        resp = requests.get(response.url)
        output = open(filename, 'wb')
        output.write(resp.content)
        output.close()
        return None



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
