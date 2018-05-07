# -*- coding: utf-8 -*-
# from settings import USER_AGENT_LIST
from hotel_grab import settings

import random
from scrapy import log

class RandomUserAgentMiddleware(object):
    print("小航")
    def process_request(self, request, spider):
        ua  = random.choice(settings.USER_AGENT_LIST)
        if ua:
            print(ua)
            request.headers.setdefault('User-Agent', ua)

