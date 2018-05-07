from scrapy.utils.serialize import ScrapyJSONEncoder
from twisted.internet.threads import deferToThread


import pymysql
import time
import json
from datetime import datetime
import logging
import re
import gzip

from . import connection
from .db import Mysql


class RedisPipeline(object):
    """Pushes serialized item into a redis list/queue"""

    def __init__(self, server, settings):
        self.server = server
        self.encoder = ScrapyJSONEncoder()
        self.mysql = Mysql()
        self.count = 0

    @classmethod
    def from_settings(cls, settings):
        server = connection.from_settings(settings)
        return cls(server, settings)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def process_item(self, item, spider):
        answers = item['answer']
        pattern = re.compile('\:(.*?)\?_escaped_fragment')
        print(item['url'])
        match = re.findall(pattern, item['url'])
        if len(match) > 0:
            url = match[0]
        else:
            pattern = re.compile('\:(.*?)\?redirected_qid')
            match = re.findall(pattern, item['url'])
            if len(match) > 0:
                url = match[0]
            else:
                urls = item['url'].split(':')
                url = urls[1]
        item['url'] = "https:" + url
#        dicts={}
#        self.count+=1
#        dicts['url']=item['url']
#        dicts['html']=item['html']
#        data = json.dumps(dicts)
#        filename = "./html_data/quora_"+str(self.count/1000)+".gz"
#        f = gzip.open(filename,'a+')
#        f.write(data)
#        f.write('\n')
#        f.close()
        if len(answers) > 10:
            item['answer_count'] = len(answers)
        try:
            question_id = self.mysql.get_question_id(url)
            if question_id:
                self.mysql.update_question(item, question_id)
            else:
                self.mysql.insert_question(item)
          #  html_id=self.mysql.get_html_id(question_id)
          #  if html_id:
          #      self.mysql.update_html(question_id,item['html'])
          #  else:
          #      self.mysql.insert_html(question_id,item['html'])
        except:
         #   istime = datetime.datetime.now()
            self.mysql.insert_question(item)
         #   question_id = self.mysql.get_question_id(url)
         #   if question_id:
         #       self.mysql.insert_html(question_id,item['html'])

         #   ietime = datetime.datetime.now()
        #    itime = (ietime - istime).microseconds
        #    logging.info('mysql insert time %f us'%itime)
        #    istime = datetime.datetime.now()
            question_id = self.mysql.get_question_id(url)
      #  if item['question'] and item['answer_count']>0:
      #      key = "quora:itemsUrl"
      #      data = item['url']
      #      self.server.rpush(key,data)
        topics = item['topic']
        for topic in topics:
            topic = topic.encode('utf8')
            topic_id = self.mysql.get_topic_id(topic)
            if topic_id:
                self.mysql.insert_topics(question_id, topic_id)
            else:
                self.mysql.insert_topic(topic)
                topic_id = self.mysql.get_topic_id(topic)
                self.mysql.insert_topics(question_id, topic_id)
        #    ietime = datetime.datetime.now()
        #    itime = (ietime - istime).microseconds
        #    logging.info('mysql query time %f us'%itime)
        # print question_id
        if item['is_merged']:
            try:
                self.mysql.insert_merged(
                    question_id, item['merged_url'], item['merged_question'])
            except:
                pass
        for answer in answers:
            now = datetime.now()
         #       ietime = datetime.datetime.now()
         #       logging.info('redis sadd time %f us'%itime)
            try:
                self.mysql.insert_answer(question_id, now, answer)
            except:
                self.mysql.update_answer(answer, answer['id'], now)
        return item

    def item_key(self, item, spider):
        return "%s:itemsUrl" % spider.name
