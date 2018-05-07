# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuoraItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topic = scrapy.Field()
    question = scrapy.Field()
    is_merged = scrapy.Field()
    merged_url = scrapy.Field()
    merged_question = scrapy.Field()
    question_details = scrapy.Field()
    answer_count = scrapy.Field()
    answer = scrapy.Field()
    url = scrapy.Field()
    html = scrapy.Field()


class AnswerItem(scrapy.Item):
    author = scrapy.Field()
    author_url = scrapy.Field()
    id = scrapy.Field()
    content = scrapy.Field()
    views = scrapy.Field()
    upvote = scrapy.Field()
    time = scrapy.Field()
    rank = scrapy.Field()
