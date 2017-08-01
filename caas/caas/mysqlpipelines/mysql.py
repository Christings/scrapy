import pymysql

from caas import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_DBNAME = settings.MYSQL_DBNAME
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT

conn = pymysql.connect(host=MYSQL_HOSTS, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DBNAME,
                       charset="utf8")
cur = conn.cursor()


class Mysql:
    # 世界银行
    # 插入数据——世界银行
    @classmethod
    def insert_worldbank_indicators(cls, indi_url, indi_name):
        sql = 'insert into worldbank_indicators(indi_url,indi_name)values(%(indi_url)s,%(indi_name)s)'
        value = {
            'indi_url': indi_url,
            'indi_name': indi_name
        }
        cur.execute(sql, value)
        conn.commit()

    # 去重——世界银行
    @classmethod
    def select_name(cls, indi_name):
        sql = "select exists(select 1 from worldbank_indicators where indi_name=%(indi_name)s)"
        value = {
            'indi_name': indi_name,
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

    # 插入——comtrade——countrylist
    @classmethod
    def insert_comtrade_countrylist(cls, country_code, country_name):
        sql = 'insert into comtrade_countrylist(country_code,country_name)values(%(country_code)s,%(country_name)s)'
        value = {
            'country_code': country_code,
            'country_name': country_name
        }
        cur.execute(sql, value)
        conn.commit()

    # 去重——世界银行
    @classmethod
    def select_code(cls, country_code):
        sql = "select exists(select 1 from comtrade_countrylist where country_code=%(country_code)s)"
        value = {
            'country_code': country_code,
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

    @classmethod
    def insert_1992_catalog_level1(cls, catalog_level1_num, catalog_level1_name, catalog_level1_desc):
        sql = "insert into 1992_catalog_level1('catalog_level1_num','catalog_level1_name','catalog_level1_desc')values(%(catalog_level1_num)s,%(catalog_level1_name)s,%(catalog_level1_desc)s)"
        value = {
            'catalog_level1_num': catalog_level1_num,
            'catalog_level1_name': catalog_level1_name,
            'catalog_level1_desc': catalog_level1_desc
        }
