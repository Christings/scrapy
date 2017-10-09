# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from .items import BeltandRoadItem
import csv

# 一带一路战略支撑平台
class BeltandRoadPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        self.db = self.client[settings['MONGO_DB']]
        self.BeltandRoad = self.db['BeltandRoad']

    def process_item(self, item, spider):
        if isinstance(item, BeltandRoadItem):
            try:
                if item['name']:
                    item = dict(item)
                    self.BeltandRoad.insert(item)
                    print("插入成功")
                    return item
            except Exception as e:
                spider.logger.exception("")

    # def __init__(self):
    #     with open('BeltandRoad.csv', 'w') as csvout:
    #         self.csvwriter = csv.writer(csvout)
    #         self.csvwriter.writerow([b'name', b'content'])
    #
    # def process_item(self, item, spider):
    #     if isinstance(item, BeltandRoadItem):
    #         try:
    #             rows = zip(item['name'], item['content'])
    #             for row in rows:
    #                 self.csvwriter.writerow(row)
    #             self.csvwriter.close()
    #             return item
    #
    #             # self.ws.append(line)
    #             # self.wb.save('/CaasSpider/files/BeltandRoad.xlsx')
    #         except Exception as e:
    #             spider.logger.exception("")

