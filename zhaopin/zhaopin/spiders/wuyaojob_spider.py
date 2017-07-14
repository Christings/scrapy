# -*- coding: utf-8 -*-

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from zhaopin.items import CompanyItem, JobItem


class wuyaojobSpider(scrapy.Spider):
    name = "wuyaojob"
    # allowed_domains=["51job.com"]
    domain = "51job.com"
    start_urls = ['http://51job.com']

    # rules = (
    #    ## 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
    #    #Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

    #    # 提取匹配 'item.html' 的链接并使用spider的parse_company方法进行分析
    #    Rule(LinkExtractor(allow=('\.html', )), callback='parse_company'),

    #    Rule(LinkExtractor(allow=('\.htm', )), callback='parse_job'),
    # )

    def start_requests(self):
        requests = []
        for item in self.start_urls:
            requests.append(scrapy.Request(url=item, headers={'Referer': 'http://www.baidu.com/'}, callback=self.parse))
        return requests

    def parse(self, response):

        # self.logger.info("访问地址：%s" % response.xpath('//a/@href').extract())

        for url in response.xpath('//a/@href').extract():
            if url.endswith('index.htm'):
                yield scrapy.Request(url, headers={'Referer': response.url}, callback=self.parse_company)
            elif url.endswith('.html') and url.startswith('http://jobs.51job.com/all/'):
                yield scrapy.Request(url, headers={'Referer': response.url}, callback=self.parse_job)
            else:
                yield
        return None

    def parse_company(self, response):

        links = response.xpath('//a')
        items = []

        for link in links:
            item = CompanyItem()
            item['domain'] = self.domain

            item['url'] = link.xpath('.//@href').extract()
            if len(item['url']) > 0:
                item['url'] = item['url'][0]
            else:
                item['url'] = ''

            item['comname'] = link.xpath('.//text()').extract()
            if len(item['comname']) > 0:
                item['comname'] = item['comname'][0]
            else:
                item['comname'] = ''

            items.append(item)
            # self.logger.info('地址： %s 名称：%s '%(item['url'],item['comname']))

        return items

    def parse_job(self, response):

        # self.log('职位页面地址： %s' % response.url)

        item = JobItem()
        item['domain'] = self.domain
        item['url'] = response.url

        # /html/body/div[2]/div[2]/div[2]/div/div[1]/h1
        item['jobname'] = response.xpath('//div[@class="cn"]//h1//text()').extract()
        if len(item['jobname']) > 0:
            item['jobname'] = item['jobname'][0]
        else:
            item['jobname'] = ''

        item['comname'] = response.xpath('//p[@class="cname"]//a//text()').extract()
        if len(item['comname']) > 0:
            item['comname'] = item['comname'][0]
        else:
            item['comname'] = ''

        item['comurl'] = response.xpath('//p[@class="cname"]//a//@href').extract()
        if len(item['comurl']) > 0:
            item['comurl'] = item['comurl'][0]
        else:
            item['comurl'] = ''

        item['salary'] = response.xpath('//div[@class="cn"]//strong//text()').extract()
        if len(item['salary']) > 0:
            item['salary'] = item['salary'][0]
        else:
            item['salary'] = ''

        item['fuli'] = response.xpath('//p[@class="t2"]//text()').extract()
        if len(item['fuli']) > 0:
            item['fuli'] = item['fuli'][0]
        else:
            item['fuli'] = ''

        item['jobdemo'] = response.xpath('//div[@class="bmsg job_msg inbox"]//text()').extract()
        if len(item['jobdemo']) > 0:
            item['jobdemo'] = item['jobdemo'][0]
        else:
            item['jobdemo'] = ''

        item['eduname'] = response.xpath('//div[@class="t1"]/span[2]//text()').extract()
        if len(item['eduname']) > 0:
            item['eduname'] = item['eduname'][0]
        else:
            item['eduname'] = ''

        item['tradename'] = response.xpath('//p[@class="fp f2"]/span[@class="el"]//text()').extract()
        if len(item['tradename']) > 0:
            item['tradename'] = item['tradename'][0]
        else:
            item['tradename'] = ''

        return item
