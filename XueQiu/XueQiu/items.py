# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XueqiuItem(scrapy.Item):


    name = scrapy.Field()  #组合名字
    market = scrapy.Field()  #市场
    tags = scrapy.Field()  #投资标签
    description = scrapy.Field()  #投资建议
    income = scrapy.Field()  #收益率
    invesor = scrapy.Field()  #投资人
    concernNum = scrapy.Field()  #关注人数


