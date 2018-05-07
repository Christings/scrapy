# _*_ coding:utf8 _*_

import redis

server = redis.Redis(host="127.0.0.1",port=6379)

if 'quora:dupefilter0' in server.keys():
    server.delete('quora:dupefilter0')

if 'quora:requests' in server.keys():
    server.delete('quora:requests')

if 'quora:question' in server.keys():
    server.delete('quora:question')
print 'Finish!'
