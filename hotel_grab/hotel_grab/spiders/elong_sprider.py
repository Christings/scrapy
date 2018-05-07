# # -*- coding: utf-8 -*-
# import scrapy
# from scrapy.selector import Selector
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# import time
# import os
# from os.path import exists
# import json
# import codecs
# import gzip
# import StringIO
#
# import urllib
# import urllib2
#
# import re
# from ..items import ELongItem
#
# class ElongSpriderSpider(scrapy.Spider):
#     name = 'elong_sprider'
#     allowed_domains = ['www.elong.com']
#     start_urls = ['http://hotel.elong.com/90555108/']
#
#     def parse(self, response):
#         null = ''
#         true =True
#         false = False
#         for page in xrange(1,2):
#
#             Comments=[]
#
#             page=str(page)
#             print "第"+page+"页"
#
#             # url="http://hotel.elong.com/ajax/detail/gethotelreviews/?hotelId="+hotelnumber+"&recommendedType=0&pageIndex="+page+"&mainTagId=0&subTagId=0&_=1468730838292"
#             url = 'http://hotel.elong.com/ajax/detail/gethotelreviews?hotelId=90555108&recommendedType=0&pageIndex='+page+'&mainTagId=0&subTagId=0&code=7171382&_=1501909250407'
#             headers={
#
#                 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
#                 'Accept':'application/json, text/javascript, */*; q=0.01',
#                 'Accept-Language':'zh-CN,zh;q=0.8',
#                 'Accept-Encoding':'gzip, deflate, sdch',
#                 'Connection':'keep-alive',
#                 'X-Requested-With':'XMLHttpRequest',
#                 #'Referer':'http://hotel.elong.com/guangzhou/32001005/',
#                 'Host':'hotel.elong.com'
#
#             }
#
#
#             #请求AJAX
#             req=urllib2.Request(url,None,headers)
#             res=urllib2.urlopen(req)
#             data=res.read()
#             res.close()
#
#             #因为data有压缩所以要从内存中读出来解压
#             data=StringIO.StringIO(data)
#             gz=gzip.GzipFile(fileobj=data)
#             ungz=gz.read()
#             dic_ungz = eval(ungz)
#             contents = dic_ungz['contents']
#             for fu in contents:
#                 item = ELongItem()
#                 item['nickName'] = fu['commentUser']['nickName']#用户ID
#                 print(item['nickName'])
#                 item['content'] = fu['content']#评论
#                 print(item['content'])
#                 item['houseType'] = fu['commentExt']['order']['roomTypeName']
#                 print(item['houseType'])
#                 yield item
