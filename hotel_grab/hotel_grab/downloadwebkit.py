# -*- coding:utf-8 -*-
from selenium import webdriver
from scrapy.http import HtmlResponse
import time

# from settings import USER_AGENT_LIST
from hotel_grab.settings import USER_AGENT_LIST


import random


class WebkitDownloader(object):
    # 通过selenium打开chrome内核，从而获得网页加载后的源代码。
    def process_request(self, request, spider):
        print("小航")

        ua  = random.choice(USER_AGENT_LIST)
        if ua:
            print(ua)
            request.headers.setdefault('User-Agent', ua)
        if spider.name == "ctrip_sprider":   # 注意：之前scrapy和senelium一直没连接起来，是因为spider.name写的是spider。
            print("selenium is starting...")
            browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
            browser.get(request.url)
            time.sleep(5)
            # body=browser.find_element_by_id('groups-list')
            # body_child=body.get_attribute('innerHTML')
            body = browser.page_source
            print(u"访问的url：", request.url)
            return HtmlResponse(browser.current_url, body=body, encoding='utf-8', request=request)
        else:
            return
