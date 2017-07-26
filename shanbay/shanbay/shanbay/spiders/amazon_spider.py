# coding:utf-8
import scrapy
from scrapy.selector import Selector
import logging

from shanbay.items import AmazonItem
from shanbay.spiders.utils import parse_params


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.cn"]
    base_url = "https://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A[node]"
    DOWNLOAD_DELAY = 2
    CONCURRENT_REQUESTS = 10

    start_urls = [
    ]

    node_dict = {
        "659380051": "中国现代",
        "659381051": "中国当代",
        # "659379051": "中国古代", "659382051": "外国",
        # "658515051": "散文随笔", "664802051": "随笔杂文", "659416051": "文学作品集", "664804051": "游记",
        # "664805051": "书信日记", "664803051": "小品文", "663238051": "散文杂著集", "663236051": "诗歌集",
        # "663237051": "小说集", "2147364051": "纪实文学集", "663240051": "民间文学集", "663300051": "现当代诗歌",
        # "663299051": "古典诗歌", "659420051": "诗歌研究", "663301051": "词", "663302051": "曲",
        # "663309051": "历史与社会纪实", "663308051": "人物纪实", "663311051": "回忆录与口述",
        # "663312051": "专题报道", "663310051": "报告文学集", "659362051": "诗歌词曲小说", "659363051": "戏剧",
        # "659371051": "各时代文学评论与鉴赏", "659372051": "文学批评", "659373051": "专题鉴赏",
        # "1355457071": "影视小说", "2126309051": "电影文学", "2126310051": "电视文学", "658520051": "期刊杂志",
        # "658508051": "文学理论", "658510051": "文学史", "658519051": "民间文学", "2147365051": "戏剧与曲艺",
        # "663149051": "文学作品导读", "659181051": "辞典与工具书", "658391051": "文学套装书",
    }

    for node in node_dict.keys():
        start_urls.append(base_url.replace("[node]", node))

    def parse(self, response):
        node, page = self.get_node_and_page(response.url)
        try:
            book_lis = response.xpath('//*[@id="s-results-list-atf"]/li')
            if len(book_lis) == 0:
                book_lis = response.xpath('//*[@id="mainResults"]/ul/li')
            if len(book_lis) == 0:
                raise ValueError
        except Exception as e:
            logging.log(logging.ERROR, 'Not get books <li>' + str(e))
            return

        for index, book in enumerate(book_lis):
            if not (u'精装' in book.extract() or u'平装' in book.extract()):
                # ignore e-book
                continue
            item = self.parse_item(book, node, page)
            yield item

        next_page = response.xpath('//*[@id="pagnNextLink"]/@href').extract()
        if next_page:
            next_page_url = 'https://www.amazon.cn' + next_page[0]
            logging.log(logging.INFO, 'Next page: %s' % next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse)

    @staticmethod
    def get_node_and_page(url):
        params = parse_params(url)
        if len(params) == 2:
            return params[0][1][0], 1
        elif len(params) == 3:
            return params[0][1][0][2:], params[2][1][0]
        else:
            logging.log(logging.ERROR, 'parse_params ERROR' + str(params))

    @staticmethod
    def parse_item(book, node, page):
        item = AmazonItem()
        item['node'] = node
        item['page'] = page
        try:
            item['book_id'] = book.xpath('@data-asin').extract()[0]
            item['name'] = book.xpath(
                './div/div/div/div[2]/div[1]/div[1]/a/h2/@data-attribute').extract()[0]
            try:
                item['num_comment'] = int(book.xpath(
                    './div/div/div/div[2]/div[2]/div[2]/div[1]/a/text()').extract()[0].replace(',', ''))
            except IndexError as e:
                # no comment yet
                item['num_comment'] = 0
            item['price'] = []
            price_divs = book.xpath(
                './div/div/div/div[2]/div[2]/div[1]/div')
            for div_index, div in enumerate(price_divs):
                price, pack = None, None
                try:
                    pack = div.xpath(
                        './a/h3/@data-attribute').extract()[0]
                    if pack:
                        price = float(div.xpath(
                            '../div[{}]/a/span[2]/text()'.format(div_index + 2)).extract()[0][1:])
                        if price:
                            # '精装', '平装', 'Kindle'
                            if u'精装' in pack:
                                item['price'].append((0, price))
                            elif u'平装' in pack:
                                item['price'].append((1, price))
                            elif u'Kindle' in pack:
                                item['price'].append((2, price))
                except (IndexError, ValueError) as e:
                    if len(item['price']) == 0 and div_index == len(price_divs) - 1:
                        # 直到最后一个div, 仍未获取价格, 打印错误信息
                        logging.log(logging.ERROR, 'XPath ERROR in <price_divs>: ' +
                                    str(item) + '\n--\n' + str(e))
        except (IndexError, ValueError) as e:
            logging.log(logging.ERROR, 'XPath ERROR in <book_li>: ' +
                        str(item) + '\n--\n' + str(e))
        yield item
