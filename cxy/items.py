# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CxyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Ctitle          = scrapy.Field()        # 标题
    Curl            = scrapy.Field()        # url 地址
    ClikeCounts     = scrapy.Field()        # 好评数
    ClookCounts     = scrapy.Field()        # 浏览数
    Ctext           = scrapy.Field()        # 正文
    Ctime           = scrapy.Field()        # 发表时间