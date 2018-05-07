# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import requests
from scrapy.http import Request
import re
from lxml import etree


class CtripSpriderSpider(scrapy.Spider):
    name = 'ctrip_sprider'
    allowed_domains = ['hotels.ctrip.com']
    print("start。。。。。。。。。")
    start_urls = ['http://hotels.ctrip.com/hotel/1519714.html?isFull=F#ctm_ref=hod_sr_lst_dl_n_1_1']

    def parse(self, response):
        houseType = response.xpath('//*[@id="4056396"]/a[2]/text()').extract()
        print(str(houseType))
        # print(str(houseType).decode("unicode-escape"))
        housePrice = response.xpath('//*[@id="J_RoomListTbl"]/tbody/tr[3]/td[8]/p[1]/span/text()').extract()
        print(str(housePrice))
        # print(str(housePrice).decode("unicode-escape"))
        bookingStatus = response.xpath('//*[@id="J_RoomListTbl"]/tbody/tr[3]/td[9]/div/a/div[1]/text()').extract()
        print(str(bookingStatus))
        # print(str(bookingStatus).decode("unicode-escape"))
        # userId = response.xpath('//*[@id="divCtripComment"]/div[4]/div[1]/div[1]/p[2]/span').extract()
        # print(userId)
        # hotelComments = response.xpath('//*[@id="divCtripComment"]/div[4]/div[1]/div[2]/div[1]/div[1]').extract()
        # print(str(hotelComments).decode("unicode.-escape"))
        x = response.body
        print(x)
        print("1111111111111111111")
        # reg = r'<p class="name">(.*?)</p>'
        # reg_data = re.compile(reg,re.S)
        # userIds = re.findall(reg_data,x)

        comment = response.xpath('//div[@class="comment_title"]/span[2]/span/text()').extract()
        print("comment:", comment)
        #
        # reg1 = r'<a id="morecomment" data-dopost="T" href="(.*?)" name="needTraceCode">更多携程点评</a>'
        # reg_data1 = re.compile(reg1,re.S)
        # dianp_url = re.findall(reg_data1,x)[0]
        #
        #
        # yy=dianp_url.encode("utf-8")
        # print("测试：", yy)
        # yield Request(url=dianp_url,callback=self.get_comments)
        # requests.get(dianp_url)
        # print(str(userIds).decode("unicode-escape"))
        # print(dianp_url)
        # def get_comments(self,response):
        #     print("行总  ")
        #     xx = response.xpath('//*[@id="divCtripComment"]/div[@class="comment_detail_list"]/div[6]/div[1]/p[2]/span')
        #     # html = response.execute_script("return document.documentElement.outerHTML")
        #     # doc = etree.HTML(html)
        #     print(xx)
        #     # print(doc)
