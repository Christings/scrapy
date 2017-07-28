# -*- coding:utf-8 -*-
import scrapy
from caas.items import FaoCountriesItem
from bs4 import BeautifulSoup
from caas.items import FaoCountriesItem


class FaoCountriesSpier(scrapy.Spider):
    name = "faocountries"
    start_urls = ["http://www.fao.org/countryprofiles/geographic-and-economic-groups/en/"]
    print("start")

    # def start_requests(self):
    #     yield scrapy.Request(url=self.start_url, callback=self.parse)

    def parse(self, response):
        # 通过selenium打开chrome内核，从而获得网页加载后的源代码。
        # sel = scrapy.Selector(response)
        print("1:", response.body)

        # sel=scrapy.Selector(response.body).xpath('div[id="groups-list"]')
        # for each in sel.xpath('div/h3/text()').extract():
        #     print(each)
        a=response.xpath('//div[@id="groups-list"]/div/h3/text()').extract()
        b=response.xpath('//div[@id="groups-list"]/div[1]/div/h4/text()').extract()
        c=response.xpath('//div[@id="groups-list"]/div[1]/div/ul/li/a/text()').extract()
        # print("y:",y)
        item=FaoCountriesItem()
        # x=[]
        for each in a:
            item["first"]=each
            print(each)
            if each=="Geographical Region":
                item["second"]=b
                print(item["second"])
                item["third"]=c
                print(item["third"])
            # for i in b:
            #     item["second"] = i
            #     print("111:",i)



        # soup = BeautifulSoup(response.body, "lxml")

        # print("11:",soup.find(id="groups-list" "div"))
        # tags=soup.find_all("div",id_="groups-list")
        # temp=soup.select('div')
        # l1 = soup.select('div h3')
        # l2 = soup.select('div.divgroup h4')
        #
        # l3 = soup.select('ul li a')
        # #
        # for i in l1:
        #     print("1:",i.string)
        #
        #     # for j in l2:


        # first=soup.select('#groups-list div h3')
        # second=soup.select('#group-list div.divgroup')
        # third=soup.select('#group-list div.divgroup ul li a')
        # for i in first:
        #     item=FaoCountriesItem()
        #     item["first"]=i
        #     print("1:",first.string)
        #     for j in second:
        #         # item = FaoCountriesItem()
        #         item["second"] = j
        #         print("2:", second.string)
        #         for k in third:
        #             # item = FaoCountriesItem()
        #             item["third"] = k
        #             print("3:", third.string)


        # second=soup.select("div.divgroup h4")
        #
        # for t in second:
        #     ul_id="ul_"+t.get("rel")
        #     se=t.string
        #     print("se:",se)
        #     content=soup.select("ul#"+ul_id+"li a")
        #     for i in content:
        #         print("xx:")
