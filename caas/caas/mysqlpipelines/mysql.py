import pymysql
from caas import settings


class Mysql:
    @classmethod
    def insert_1992_catalog_level1(cls, catalog_level1_num, catalog_level1_name, catalog_level1_desc):
        sql = "insert into 1992_catalog_level1('catalog_level1_num','catalog_level1_name','catalog_level1_desc')values(%(catalog_level1_num)s,%(catalog_level1_name)s,%(catalog_level1_desc)s)"
        value={
            'catalog_level1_num':catalog_level1_num,
            'catalog_level1_name':catalog_level1_name,
            'catalog_level1_desc':catalog_level1_desc
        }