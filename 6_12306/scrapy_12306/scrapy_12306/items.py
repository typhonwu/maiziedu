# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ProvinceItem(scrapy.Item):
    name = scrapy.Field()    

class AgencyItem(scrapy.Item):
    province = scrapy.Field()
    city = scrapy.Field()
    county = scrapy.Field()
    address = scrapy.Field()
    name = scrapy.Field()
    windows = scrapy.Field()
    start = scrapy.Field()
    end = scrapy.Field()

class StationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bureau = scrapy.Field()
    station = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    passenger = scrapy.Field()
    luggage = scrapy.Field()
    package = scrapy.Field()
# 这个item设计的非常巧妙，不需要字段
# 它的存在从名字就看出来了
# 类似于信号
# 通知pipeline执行提交操作
class CommitItem(scrapy.Item):
    pass
