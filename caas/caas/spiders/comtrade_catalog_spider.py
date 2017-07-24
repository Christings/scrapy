# -*- coding:utf-8 -*-

from scrapy.conf import settings
import scrapy
import requests
import re
from caas.items import ComtradeCatalogItem
from caas.items import ComtradeCatalogLevel2Item


class ComtradeCatalogSpider(scrapy.Spider):
    name = "comtradecatalog"
    # 1.一级目录url，调整的关键字为px=H0-H4,S1-S4
    #   https://comtrade.un.org/db/mr/rfCommoditiesList.aspx?px=H0&cc=TOTAL
    # 2.二级子目录url，调整的关键字为px=H0-H4，cc=01-99
    #   https://comtrade.un.org/db/mr/rfCommoditiesList.aspx?px=H0&cc=01
    # 3.三级子目录url
    #   https://comtrade.un.org/db/mr/rfCommoditiesList.aspx?px=H0&cc=0101

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
        # self.start_url.split("&")[0]
        yield scrapy.Request(url=self.start_url, callback=self.parse_level1, cookies=self.cookie, headers=self.headers,
                             meta=self.meta)

    # 一级目录最终存储的地方（编号，名称，描述）
    # cat_level1_num = []
    # cat_level1_name = []
    # cat_level1_desc = []
    # 二级目录最终存储的位置（编号，名称，描述）
    cat_level2_url = []
    cat_level2_num = []
    cat_level2_name = []
    cat_level2_desc = []
    # 三级目录最终存储的位置（编号，名称，描述）
    cat_level3_url = []
    cat_level3_num = []
    cat_level3_name = []
    cat_level3_desc = []

    a = []
    b = []
    c = []

    # 解析一级目录
    def parse_level1(self, response):
        # selector = scrapy.Selector(response)
        # 一级分类的编号、名称、描述的原始数据

        # year = response.xpath(
        #     '//table[@id="pGrid"]/tbody/tr[2]/td/div[2]/span[@class="sTd"]').extract()
        # print("2333:", year)
        for sel in response.xpath('//table[@id="dgPzCommodities"]/tr'):
            item = ComtradeCatalogItem()

            year="1992"


            temp1_level1_num=sel.xpath('td[1]/a/text()').extract() #获得list的数据
            temp2_level1_num=('').join(temp1_level1_num)           #变成str类型

            temp1_level1 = sel.xpath('td[2]/text()').extract()  # 获得list的数据
            del(temp1_level1[0]) #过滤空字段
            if temp1_level1:
                if temp1_level1[0]!=": ALL COMMODITIES": #过滤掉第一行
                    # print("lala:", temp1_level1)
                    item["catalog_level1_name"]=str(temp1_level1[0]).replace(":","") #一级分类的名字
                    temp1_catalog_level1_desc=str(temp1_level1[1]).replace(":","")
                    item["catalog_level1_desc"]=temp1_catalog_level1_desc.replace("'","") #一级分类的描述,因为有单引号，导致某些数据插入失败。
                    # item["catalog_year"]=year
                    # print("lala:",item["catalog_level1_name"],"lala54:",item["catalog_level1_desc"])
                    yield item
            if temp2_level1_num:
                temp3_level1_num=temp2_level1_num.replace(u"\xa0\xa0",u"") #终于把字符串中的空格去掉了，前面加u
                item["catalog_level1_num"]=temp3_level1_num  #一级分类的目录
                item["catalog_year"]=year
                # print('item["catalog_level1_num"]:',item["catalog_level1_num"])
                yield item

            temp1_level2_url = sel.xpath('td[1]/a/@href').extract()  # 提取二级分类的url
            if temp1_level2_url and temp1_level2_url[0] != 'rfCommoditiesList.aspx?px=H0&cc=TOTAL':
                level2_url = temp1_level2_url;
                # temp1_year=str(temp1_level2_url).split("?")[1]
                # temp2_year=str(temp1_year).split("&")[0]
                # year=temp2_year.replace("H0").
                # print("temp1_level2_url:", level2_url)
                yield scrapy.Request(level2_url,callback=self.parse_level2)

        # 解析二级目录
        def parse_level2(self, response):


        # catalog_level1_num_primary = selector.xpath('//table[@id="dgPzCommodities"]/tr/td[1]/a/text()').extract()
        # catalog_level1_primary = selector.xpath(u'//table[@id="dgPzCommodities"]/tr/td[2]/text()').extract()
        #
        # # 提取二级分类的url,并进行请求
        # catalog_level2_url = selector.xpath('//table[@id="dgPzCommodities"]/tr/td[1]/a/@href').extract()
        # del (catalog_level2_url[0])
        # # print("catalog_level2_url:", catalog_level2_url)
        # for each in catalog_level2_url:
        #     level2_url = "https://comtrade.un.org/db/mr/" + each
        #     # print("each:",each)
        #     yield scrapy.Request(level2_url, callback=self.parse_level2)
        #
        # # 删除一级分类名称、描述前部无用的字段
        # del (catalog_level1_primary[0:4])
        # # print("1", catalog_number)
        #
        # # 提取一级分类名称、描述的有用字段
        # for i, each in enumerate(catalog_level1_primary):
        #     catalog_level1 = each.replace('\r', '').replace('\n', '').replace('\t', '')
        #     if catalog_level1 != "":
        #         catalog_level1 = catalog_level1[1:]
        #         if (i % 2 == 0):
        #             catalog_level1_name = catalog_level1
        #             print("双数catalog_level1_name:", catalog_level1_name)
        #             # item["catalog_level1_name"] = catalog_level1_name
        #             # print(item["catalog_level1_name"])
        #             # yield item
        #             self.cat_level1_name.append(catalog_level1_name);
        #             # print("self.a:", self.a)
        #
        #         elif (i % 2 == 1):
        #             catalog_level1_desc = catalog_level1
        #             print("单数catalog_level1_desc:", catalog_level1_desc)
        #             # item["catalog_level1_desc"] = catalog_level1_desc
        #             # yield item
        #             self.cat_level1_desc.append(catalog_level1_desc);
        #             # print("self.b:", self.b)
        #         else:
        #             pass
        # print("self.a:", self.cat_level1_name)
        # print("self.b:", self.cat_level1_desc)
        # # 提取一级分类编号的有用字段，去除空格等。
        # for each in catalog_level1_num_primary:
        #     catalog_level1_num = each.replace('\xa0\xa0', '')
        #     if catalog_level1_num != "":
        #         print("catalog_level1_number:", catalog_level1_num)
        #         # item["catalog_level1_num"] = catalog_level1_num
        #         # print("ok:", item["catalog_level1_num"])
        #         # yield item
        #         self.cat_level1_num.append(catalog_level1_num);
        # print("self.c:", self.cat_level1_num)
        #
        # # output = open(self.output_path, 'wb')
        # # output.write(bytearray(catalog_level1_number_list))
        # # output.close()
        # # return None
        #
        # for i in range(len(self.cat_level1_num)):
        #     item = ComtradeCatalogItem()
        #     item["catalog_level1_num"] = self.cat_level1_num[i]
        #     item["catalog_level1_name"] = self.cat_level1_name[i]
        #     item["catalog_level1_desc"] = self.cat_level1_desc[i]
        #     yield item
        #     # output = open(self.output_path, 'wb')
        #     # output.write(self.c[i])
        #     # output.close()
        #     # return None

    # 解析二级目录
    # def parse_level2(self, response):
    #     selector = scrapy.Selector(response)
    #     # 二级分类的编号、名称、描述的原始数据
    #     catalog_level2_num_primary = selector.xpath('//table[@id="dgPzCommodities"]/tr/td[1]/a/text()').extract()
    #     catalog_level2_primary = selector.xpath(u'//table[@id="dgPzCommodities"]/tr/td[2]/text()').extract()
    #
    #     # print("111P:",catalog_level2_num_primary)
    #     # print("1221P:",catalog_level2_primary)
    #
    #     # # 提取三级分类的url,并进行请求
    #     # catalog_level3_url = selector.xpath('//table[@id="dgPzCommodities"]/tr/td[1]/a/@href').extract()
    #     # del (catalog_level3_url[0])
    #     # # print("catalog_level2_url:", catalog_level2_url)
    #     # for each in catalog_level3_url:
    #     #     level3_url = "https://comtrade.un.org/db/mr/" + each
    #     #     # print("each:",each)
    #     #     yield scrapy.Request(level3_url, callback=self.parse_level3)
    #     #
    #
    #     # 删除二级分类名称、描述前部无用的字段
    #     # del (catalog_level2_primary[0:4])
    #     # print("1", catalog_level2_primary)
    #
    #     # 提取二级分类名称、描述的有用字段
    #
    #     # for i, each in enumerate(catalog_level2_primary):
    #     #     catalog_level2 = each.replace('\r', '').replace('\n', '').replace('\t', '')
    #     #     if catalog_level2 != "":
    #     #         catalog_level2 = catalog_level2[1:]
    #     #         if (i % 2 == 0):
    #     #             catalog_level2_name = catalog_level2
    #     #             # print("双数catalog_level2_name:", catalog_level2_name)
    #     #             self.cat_level2_name.append(catalog_level2_name)
    #     #             # print("self.a:", self.a)
    #     #         elif (i % 2 == 1):
    #     #             catalog_level2_desc = catalog_level2
    #     #             # print("单数catalog_level2_desc:", catalog_level2_desc)
    #     #             self.cat_level2_desc.append(catalog_level2_desc)
    #     #
    #     #             # print("self.b:", self.b)
    #     #         else:
    #     #             pass
    #     # print("self.cat_level2_name:", list(set(self.cat_level2_name)))
    #     # print("self.cat_level2_desc:", self.cat_level2_desc)
    #     # self.a = list(set(self.cat_level2_name))
    #     # self.b = list(set(self.cat_level2_desc))
    #
    #     # 提取二级分类编号的有用字段，去除空格等。
    #     for each in catalog_level2_num_primary:
    #         catalog_level2_num_temp1 = each.replace('\xa0\xa0', '')
    #         catalog_level2_num = catalog_level2_num_temp1.replace('TOTAL', '')
    #         if catalog_level2_num != "":
    #             # print("catalog_level2_number:", catalog_level2_num)
    #             item["xxx"]=catalog_level2_num
    #             self.cat_level2_num.append(catalog_level2_num)  # 实际上进行了多次循环
    #     print("self.cat_level2_num:", self.cat_level2_num)
    #     # self.c = list(set(self.cat_level2_num))
    #
    #     for i in range(len(self.c)):
    #         item = ComtradeCatalogLevel2Item()
    #         item["catalog_level2_num"] = self.c[i]
    #         item["catalog_level2_name"] = self.a[i]
    #         item["catalog_level2_desc"] = self.b[i]
    #         yield item
