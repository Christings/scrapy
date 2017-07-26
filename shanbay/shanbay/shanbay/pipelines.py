from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
import logging
from datetime import datetime

from .items import AmazonItem, JdItem, SyncItem


class MysqlPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=False,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        if isinstance(item, AmazonItem):
            query = self.dbpool.runInteraction(
                self.amazon_insert, item)
        elif isinstance(item, JdItem):
            query = self.dbpool.runInteraction(
                self.jd_update, item)
        elif isinstance(item, SyncItem):
            query = self.dbpool.runInteraction(
                self.price_update, item)
        query.addErrback(self._error, item, spider)
        return query

    def amazon_insert(self, cur, item):
        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
        sql = """insert into books(name, amazon_book_id, amazon_price, amazon_num_comment, amazon_node, amazon_page, amazon_update_time) values(%s, %s, %s, %s, %s, %s, %s)"""
        params = (item["name"], item['book_id'], str(item['price']),
                  item["num_comment"], item['node'], item['page'], now)
        cur.execute(sql, params)
        loggind.log(loggind.INFO, 'GET one amazon book', item)


    def jd_update(self, cur, item):
        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
        sql = """UPDATE books set jd_book_id=%s, jd_price=%s, jd_num_comment=%s, jd_update_time=%s where id=%s"""
        params = (item['book_id'], str(item['price']),
                  item["num_comment"], now, item['_id'])
        cur.execute(sql, params)
        loggind.log(loggind.INFO, 'GET one jd book', item)

    def price_update(self, cur, item):
        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
        if dict(item).has_key('jd_price'):
            sql = """UPDATE books set jd_price=%s, jd_update_time=%s where id=%s"""
            params = (item['jd_price'], now, item['_id'])
            loggind.log(loggind.INFO, 'UPDATE jd price', item)
        elif dict(item).has_key('amazon_price'):
            sql = """UPDATE books set amazon_price=%s, amazon_update_time=%s where id=%s"""
            params = (str(item['amazon_price']), now, item['_id'])
            loggind.log(loggind.INFO, 'UPDATE amazon price', item)
        else:
            return

        cur.execute(sql, params)

    def _error(self, failue, item, spider):
        logging.log(logging.ERROR, 'DB ERROR: ' +
                    str(item) + '\n--\n' + str(failue))
