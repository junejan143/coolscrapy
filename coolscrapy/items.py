# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CoolscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HuxiuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标题
    link = scrapy.Field()  # 链接
    desc = scrapy.Field()  # 简述
    posttime = scrapy.Field()  # 发布时间

class DouBanItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    score = scrapy.Field()