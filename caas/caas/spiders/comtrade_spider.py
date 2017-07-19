# https://comtrade.un.org/db/dqBasicQueryResults.aspx?cc=all&px=H0&r=all&y=all&p=all&rg=1,2&so=9999&rpage=dqBasicQuery&qt=y

# https://comtrade.un.org/db/dqBasicQueryResults.aspx?cc=all&px=H4&r=all&y=all&p=all&rg=1,2&tv1=1&tv2=0&so=9999&rpage=dqBasicQuery&qt=y

# https://comtrade.un.org/db/dqBasicQueryResults.aspx?cc=all&px=H3&r=all&y=all&p=all&rg=1,2&tv1=1&tv2=0&so=9999&rpage=dqBasicQuery&qt=y

# https://comtrade.un.org/db/dqBasicQueryResults.aspx?cc=TOTAL,%2001&px=H0&y=all&rg=1,2&tv1=1&tv2=0&so=9999&rpage=dqBasicQuery&qt=y
# https://comtrade.un.org/db/dqBasicQueryResults.aspx?cc=all,%2002*&px=H0&r=all&y=all&p=all&rg=1,2&tv1=1&tv2=0&so=9999&rpage=dqBasicQuery&qt=y
#
# https://comtrade.un.org/db/dqBasicQueryResults.aspx?cc=all,%2002*&px=H0&r=all&y=all,%20all,%20all,%20all,%20all,%20all,%20all,%20all&p=all&rg=1,2&tv1=1&tv2=0&so=9999&rpage=dqBasicQuery&qt=y
# https://comtrade.un.org/db/dqBasicQueryResults.aspx?cc=all,%20TOTAL*&px=H0&r=all&y=all&p=all&rg=1,2&tv1=1&tv2=0&so=9999&rpage=dqBasicQuery&qt=y

# -*- coding:utf-8 -*-
import scrapy
import requests
from scrapy.settings import Settings
from scrapy.conf import settings

# https://comtrade.un.org/db/dqBasicQueryResults.aspx?cc=all,%2002*&px=H0&r=all&y=all&p=all&rg=1,2&tv1=1&tv2=0&so=9999&rpage=dqBasicQuery&qt=y

class ComtradeSpider(scrapy.Spider):

    name = "comtrade"
    excel_url = "http://api.worldbank.org/v2/zh/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel"
    output_path = './test.zip'
    # start_url = 'http://data.worldbank.org.cn/indicator?tab=all'
    start_url = "https://comtrade.un.org/db/dqBasicQueryResults.aspx?cc=all,%2002*&px=H0&r=all&y=all&p=all&rg=1,2&tv1=1&tv2=0&so=9999&rpage=dqBasicQuery&qt=y"
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
        # url = response.xpath(
        #     '//*[@id="main"]/div[2]/section[1]/ul[2]/li[3]/a/@href').extract()
        # print('==\n', url, '==\n')
        # selector = scrapy.Selector(response)
        print("html:"+str(response.body))



    # def start_requests(self):
    #     url = self.start_url
    #     resp = requests.get(url)
    #     output = open(self.output_path, "wb")
    #     output.write(resp.content)
    #     output.close()
    #     return None

    #def parse(self, response):
        # start_urls = ("https://comtrade.un.org/db/dqBasicQueryResults.aspx?cc=all,%2002*&px=H0&r=all&y=all&p=all&rg=1,2&tv1=1&tv2=0&so=9999&rpage=dqBasicQuery&qt=y",)
        # requests.get(start_urls)
        # resp = requests.get(start_urls)
        #
        # output = open('test.xls', 'wb')
        # output.write(resp.content)
        # output.close()

