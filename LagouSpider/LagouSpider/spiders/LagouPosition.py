# -*- codingLutf-8 -*-
import scrapy


class LagoupositionSpider(scrapy.Spider):
    name = "LagouPosition"
    allowed_domains=["lagou.com/zhaopin/"]
    start_urls=(
        'http://www.lagou.com/zhaopin',
    )

    def parse(self, response):
        fp=open('1.html','w')
        fp.write(response.body)
        fp.close()
        print(response.body)