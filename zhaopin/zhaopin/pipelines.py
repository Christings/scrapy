# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import scrapy
from zhaopin.items import CompanyItem, JobItem
from zhaopin.mysql import MySql


class ZhaopinPipeline(object):
    def process_item(self, item, spider):

        if isinstance(item, CompanyItem):
            ms = MySql(host="localhost", user="root", pwd="421498", db="TalCrawl")
            if len(item['comname']) == 0:
                pass
            else:
                newsql = "insert into cra_craw_comdata(domain,url,comname)values('%s','%s','%s')" % (
                    item['domain'], item['url'], item['comname'])
                print(newsql)
                ms.ExecNonQuery(newsql.encode('utf-8'))

        elif isinstance(item, JobItem):
            if len(item['jobname']) == 0 or len(item['comname']) == 0:
                pass
            else:
                ms = MySql(host="localhost", user="root", pwd="421498", db="TalCrawl")
                newsql = "insert into cra_craw_jobdata(domain,url,jobname,comurl,comname,salary,eduname,fuli,jobdemo)\
                values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                         (item['domain'], item['url'], item['jobname'], item['comurl'], item['comname'], item['salary'],
                          item['eduname'], item['fuli'], item['jobdemo'])
                print(newsql)
                ms.ExecNonQuery(newsql.encode('utf-8'))
        else:
            pass
        return item
