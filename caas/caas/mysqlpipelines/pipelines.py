# from .mysql import Mysql
from caas.mysqlpipelines.mysql import Mysql
from caas.items import WorldBankItem
from caas.items import ComtradeCountryListItem


class WorldBankPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, WorldBankItem):
            name = item["indi_name"]
            ret = Mysql.select_name(name)
            if ret[0] == 1:
                print("世界银行——已经存在！")
                pass
            else:
                indi_url = item["indi_url"]
                indi_name = item["indi_name"]
                Mysql.insert_worldbank_indicators(indi_url, indi_name)
                print("世界银行——开始存入数据")


class ComtradeCountryListPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, ComtradeCountryListItem):
            country_code = item["country_code"]
            ret = Mysql.select_code(country_code)
            if ret[0] == 1:
                print("comtrade--countrylist---已经存在！")
                pass
            else:
                country_name = item["country_name"]
                Mysql.insert_comtrade_countrylist(country_code, country_name)
                print("comtrade--countrylist---开始存入数据！")
