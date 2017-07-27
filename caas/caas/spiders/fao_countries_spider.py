# -*- coding:utf-8 -*-

# import scrapy
# from caas.items import FaoCountriesItem
# import spynner
#
# class FaoCountriesSpier(scrapy.Spider):
#     name = "faocountries"
#     start_url = "http://www.fao.org/countryprofiles/geographic-and-economic-groups/en/"
#
#     def start_requests(self):
#         yield scrapy.Request(url=self.start_url, callback=self.parse)
#
#     def parse(self, response):
#         # print(response.body)
#         # for each in response.xpath('//h4[@class="openedHeader"]/text').extract():
#         #     x = each.xpath('li/a/text()').extract()
#         #     print("x:", each)
#         #     # y=each.xpath('div[@class="divgroup"]/@rel').extract()
#         #     # print("y:",y)
#         x= response.xpath('//div[@id="compactgroup_geo13"]/h4/text()').extract()
#         print("x:",x)



