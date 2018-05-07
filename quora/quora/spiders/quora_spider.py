# _* _ coding:utf-8 _*_
from scrapy.http import Request
from scrapy.selector import Selector

import time
import datetime
import pymysql
import redis
import re
import sys

from quora.scrapy_redis.spiders import RedisSpider
from quora.items import QuoraItem
from quora.items import AnswerItem
from quora import settings

reload(sys)
sys.setdefaultencoding("utf-8")


def get_html(html):
    sign = 0
    html_tmp = ""
    length = len(html)
    for index in range(0, length):
        if index + 8 <= length:
            if html[index:index + 8] == '<script ':
                sign = 1
            if html[index:index + 8] == '</script':
                sign = 0
        if sign == 0:
            html_tmp += html[index]
    return html_tmp


def getTime(time_str):
    num = time_str[:-1]
    num = int(num)
    type = time_str[-1]
    nowTime = datetime.datetime.now()
    if type == "h":
        time = nowTime - datetime.timedelta(hours=num)
    else:
        if type == "d":
            day = num
        elif type == "w":
            day = num * 7
        elif type == "m":
            day = num * 30
        elif type == "y":
            day = num * 365
        else:
            day = 0
        time = nowTime - datetime.timedelta(days=day)
    return time.strftime("%Y-%m-%d")


def encodeUtf(info):
    if info:
        info = info.encode('utf8')
    return info


class Quora(RedisSpider):
    name = "quora"
    redis_question = "quora:question"
    redis_url = "quora:question_urls"
    server = redis.Redis(host='redisi', port=6379)

    count = 0

    def start_requests(self):
        while self.server.llen(self.redis_url) > 0:
            # get one task from redis list
            url = self.server.rpop(self.redis_url)
            if url[0] == '/':
                url = 'https://www.quora.com' + url
                yield Request(url=url, callback=self.parse_item)

        conn = pymysql.connect(host=settings.MYSQL_HOST,
                               port=settings.MYSQL_PORT,
                               user=settings.MYSQL_USER,
                               passwd=settings.MYSQL_PASSWD,
                               db=settings.MYSQL_DB,
                               charset='UTF8')
        cur = conn.cursor()
        cur.execute(
            """select url,answer_count from question where answer_count > 5""")
        urls = cur.fetchall()
        for url in urls:
            baseurl = url[0]
            answer_count = url[1]
            if answer_count < 100:
                answer_count += 10
            else:
                answer_count = answer_count * 2 + random.randint(0, 100)
            url = baseurl + "#!n=" + str(answer_count)
            self.server.lpush(self.redis_url, url)

        while self.server.llen(self.redis_url) > 0:
            url = self.server.rpop(self.redis_url)
            yield Request(url=url, callback=self.parse_item)

    def parse_question(self, response):
        urls = response.xpath(
            '//div[@class = "ContentWrapper"]/div/div/div//a//@href').extract()
        for url in urls:
            self.server.lpush(self.redis_url, url)
            self.server.sadd(self.redis_question, url)
        #questions = response.xpath('//div[@class = "ContentWrapper"]/div/div/div//a/text()').extract()
       # question_list = []
       # for question in questions:
       #     question_list.append(question.encode('utf8'))
       # self.server.sadd(self.redis_question,*question_list)
           # yield Request(url = url,callback=self.parse_item)

    def parse_item(self, response):
        item = QuoraItem()
        item['url'] = encodeUtf(str(response.url))
        item['is_merged'] = 0

        html = response.body
        pattern = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)
        html = pattern.sub('', html)
        html = get_html(html)
        pattern = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)
        html = pattern.sub('', html)
        pattern = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)
        html = pattern.sub('', html)
        pattern = re.compile('<!--[^>]*-->')
        html = pattern.sub('', html)
        item['html'] = encodeUtf(html)
        pattern = re.compile('</p>')
        html = pattern.sub('\n</p>', html)
        pattern = re.compile('<br>|<br />')
        html = pattern.sub('\n', html)
        pattern = re.compile('</li>')
        html = pattern.sub('\n</li>', html)
        response = Selector(text=html)

        question = response.xpath(
            '//span[@class="rendered_qtext"]//text()').extract_first()
        item['question'] = encodeUtf(question)
        item['topic'] = response.xpath(
            '//span[@class="name_text"]/span//text()').extract()
        merged_url = response.xpath(
            '//div[@class="prompt_body"]/span/a/@href').extract_first()
        if merged_url:
            item['is_merged'] = 1
            item['merged_url'] = encodeUtf(merged_url)
            merged_question = response.xpath(
                '//div[@class="prompt_body"]/span/a/span/span/text()').extract_first()
            item['merged_question'] = encodeUtf(merged_question)

        detail = response.xpath(
            '//div[@class="question_details"]//text()').extract()
        question_content = ''
        for content in detail:
            question_content = question_content + encodeUtf(content)
        item['question_details'] = question_content
        answer_count = response.xpath(
            '//div[@class = "answer_count"]//text()').extract_first()

        if answer_count:
            answer_count = encodeUtf(answer_count)
            count = answer_count.split(' ')[0]
            if count[-1] == "+":
                count = count[:-1]
            if count[-1] == "k":
                count = count[:-1]
                count = int(float(count) * 1000)
            elif count[-1] == "w":
                count = count[:-1]
                count = int(float(count) * 10000)
            elif count[-1] == "m":
                count = count[:-1]
                count = int(float(count) * 1000000)
            else:
                count = int(count)
        else:
            count = 0
        item['answer_count'] = count
        items = []
        answers = response.xpath('//div[@class = "pagedlist_item"]')
        rank = 0
        for answer in answers:
            _id = answer.xpath('./div/div/div/a/@name').extract_first()
            if not _id:
                continue
            id_list = _id.split('_')
            if len(id_list) > 1:
                _id = int(id_list[1])
            else:
                _id = 0
            answerItem = AnswerItem()
            answerItem['id'] = _id
            rank = rank + 1
            answerItem['rank'] = rank

            author = answer.xpath(
                './/a[@class="anon_user"]//text() | .//a[@class="user"]//text() | .//a[@class="user qserif"]//text() | .//span[@class="anon_user"]//text() | .//span[@class="user"]//text() | .//span[@class="user qserif"]//text()').extract_first()
            author_url = answer.xpath(
                './/a[@class="anon_user"]/@href | .//a[@class="user"]/@href | .//a[@class="user qserif"]/@href | .//span[@class="anon_user"]/@href | .//span[@class="user"]/@href | .//span[@class="user qserif"]/@href').extract_first()
            answerItem['author_url'] = encodeUtf(author_url)
            answerItem['author'] = encodeUtf(author)
            views = answer.xpath(
                './/span[@class="meta_num"]//text()').extract_first()
            if views:
                if views[-1] == "+":
                    views = views[:-1]
                if views[-1] == "k":
                    views = views[:-1]
                    views = int(float(views) * 1000)
                elif views[-1] == "w":
                    views = views[:-1]
                    views = int(float(views) * 10000)
                elif views[-1] == "m":
                    views = views[:-1]
                    views = int(float(views) * 1000000)
                else:
                    views = int(views)
            else:
                views = 0
            answerItem['views'] = views
            upvote = answer.xpath(
                './/a[@class="AnswerVoterListModalLink VoterListModalLink"]//text()').extract_first()
            if upvote:
                try:
                    upvotes = upvote.split(' ')
                    upvote = upvotes[0]
                    upvote = upvote.replace(',', '')
                    upvote = int(upvote)
                except:
                    upvote = 0
            else:
                upvote = 0
            answerItem['upvote'] = upvote
            time = answer.xpath(
                './/span[@class="datetime"]//text()').extract_first()
            time = encodeUtf(time)
            time_list = time.split(' ')
            if time_list[1] == "ago":
                time = getTime(time_list[0])
            else:
                if len(time_list) == 3:
                    t = time.strptime(time, "%d %b %Y")
                    d = datetime.datetime(*t[:3])
                    time = d.strftime("%Y-%m-%d")
                else:
                    t = time.strptime(time, "%b %d")
                    d = datetime.datetime(*t[:3])
                    time = d.strftime("%m-%d")

            answerItem['time'] = encodeUtf(time)

            answerList = answer.xpath('.//*[@class="rendered_qtext"]/text() | .//*[@class="rendered_qtext"]/b//text() | .//*[@class="rendered_qtext"]/blockquote//text() | .//*[@class="rendered_qtext"]/p//text() | .//*[@class="rendered_qtext"]/div//text() | .//*[@class="rendered_qtext"]/span//text() | .//*[@class="rendered_qtext"]/ol//text() | .//*[@class="rendered_qtext"]/li//text() | .//*[@class="rendered_qtext"]/ul//text() ').extract()
            content = ''
            for temp in answerList:
                content = content + temp + u" "
            answerItem['content'] = encodeUtf(content)
            items.append(answerItem)
        item['answer'] = items
        urls = response.xpath(
            '//li[@class="related_question"]/div/div/a/@href').extract()
        for url in urls:
            if url[0] == '/':
                sadd = self.server.sismember(self.redis_question, url)
                if sadd:
                    pass
                else:
                    self.server.sadd(self.redis_question, url)
                    self.server.lpush(self.redis_url, url)
        return item
