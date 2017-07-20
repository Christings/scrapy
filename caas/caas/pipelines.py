# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from caas.items import ComtradeCatalogItem
from caas.MysqlComtradeCatalog import MySql


class ComtradeCatalogPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, ComtradeCatalogItem):
            ms = MySql(host="localhost", user="root", pwd="421498", db="caas")
            if len(item['indi_name_cn']) == 0:
                pass
            else:
                newsql = "insert into worldbank_indicators(indi_name_en,indi_name_cn)values('%s','%s')" % (
                    item['indi_name_en'], item['indi_name_cn'])
                print(newsql)
                ms.ExecNoQuery(newsql.encode('utf-8'))
        else:
            pass
        return item


class CaasPipeline(object):
    def process_item(self, item, spider):
        return item
