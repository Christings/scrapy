# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
import sqlite3
import logging
import json
import urllib2
import random

from scrapy import signals
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

from fake_useragent import UserAgent


class RotateUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, user_agent=""):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        self.user_agent = UserAgent().random
        print(self.user_agent)
        if self.user_agent:
            logging.log(logging.DEBUG, 'Current UserAgent: ' + self.user_agent)
            request.headers.setdefault(b'User-Agent', self.user_agent)


log = logging.getLogger('scrapy.proxies')


class ProxyMiddleware(object):
    proxy_query_url = 'http://localhost:8000'
    proxy_del_url = 'http://127.0.0.1:8000/delete?ip='

    def __init__(self, settings):
        # self.proxies = json.load(urllib2.urlopen(self.proxy_query_url))
        pass

    @property
    def proxies(self):
        return json.load(urllib2.urlopen(self.proxy_query_url))

    @property
    def proxy(self):
        proxy = random.choice(self.proxies)
        return "http://" + proxy[0] + ":" + str(proxy[1])

    def delete(self, proxy):
        proxy = proxy.split('://')[1].split(':')
        ip, port = proxy
        is_deleted = json.load(urllib2.urlopen(self.proxy_del_url + ip))
        log.info('Removing failed proxy <%s>, %d proxies left' %
                 (ip, len(self.proxies)))
        return True if is_deleted else False

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        if 'proxy' in request.meta:
            if request.meta["exception"] is False:
                return
        request.meta["exception"] = False

        proxy = self.proxy
        request.meta['proxy'] = proxy

        log.info('Using proxy <%s>, %d proxies left.' %
                 (proxy, len(self.proxies)))

    def process_exception(self, request, exception, spider):
        if 'proxy' not in request.meta:
            return
        proxy = request.meta['proxy']
        if self.delete(proxy):
            request.meta["exception"] = True


class QuoraSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
