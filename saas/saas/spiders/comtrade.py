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


class ComtradeSpider(scrapy.Spider):
    name = "comtrade"

    # start_url = "https://comtrade.un.org/db/dqBasicQueryResults.aspx?cc=all,%2002*&px=H0&r=all&y=all&p=all&rg=1,2&tv1=1&tv2=0&so=9999&rpage=dqBasicQuery&qt=y"
    # output_path = './test.zip'

    # def start_requests(self):
    #     url = self.start_url
    #     resp = requests.get(url)
    #     output = open(self.output_path, "wb")
    #     output.write(resp.content)
    #     output.close()
    #     return None

    def parse(self, response):
        start_urls = ("https://comtrade.un.org/db/dqBasicQueryResults.aspx?cc=all,%2002*&px=H0&r=all&y=all&p=all&rg=1,2&tv1=1&tv2=0&so=9999&rpage=dqBasicQuery&qt=y",)
        # requests.get(start_urls)
        resp = requests.get(start_urls)

        output = open('test.zip', 'wb')
        output.write(resp.content)
        output.close()

        print(response.body)
