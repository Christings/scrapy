# from .mysql import Mysql
from caas.mysqlpipelines.mysql import Mysql
from caas.items import WorldBankItem


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
