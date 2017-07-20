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
            # if len(item['catalog_level1_num']) == 0:
            #     pass
            # else:
                # newsql = "insert into catalog_level1(catalog_level1_name,catalog_level1_desc)values('%s','%s','%s')" % (
                #     item['catalog_level1_name'], item['catalog_level1_desc'])
            newsql = "insert into catalog_level1(catalog_level1_num,catalog_level1_name,catalog_level1_desc)values('%s','%s','%s')" % (
                item['catalog_level1_num'], item['catalog_level1_name'], item['catalog_level1_desc'])

            print(newsql)
            ms.ExecNoQuery(newsql.encode('utf-8'))
        else:
            pass
        return item


class CaasPipeline(object):
    def process_item(self, item, spider):
        return item
