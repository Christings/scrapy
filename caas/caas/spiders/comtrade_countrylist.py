# -*- coding:utf-8 -*-
import scrapy
from scrapy.conf import settings
from caas.items import ComtradeCountryListItem


class ComtradeCountryListSpider(scrapy.Spider):
    name = "comtradecountrylist"
    start_url = "https://comtrade.un.org/db/mr/rfReportersList.aspx"

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

    # 解析countrylist
    def parse(self, response):
        print(response.body)
        for each in response.xpath('//table[@id="dgPzReporters"]/tr'):
            item = ComtradeCountryListItem()

            temp1_country_code = each.xpath('td[1]/text()').extract()
            temp2_country_code = ('').join(temp1_country_code)  # 变成str类型
            if temp2_country_code != "Code":
                item["country_code"] = temp2_country_code
                # temp2_country_code = temp1_country_code
                print("temp2_country_code:", temp2_country_code)
                yield item

            temp1_country_name = each.xpath('td[2]/text()').extract()
            del (temp1_country_name[0])
            if temp1_country_name:
                item["country_name"] = str(temp1_country_name[1]).replace(":", "")
                print('item["country_name"]:', item["country_name"])
                yield item
