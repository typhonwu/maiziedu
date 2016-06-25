# -*- coding: utf-8 -*-
import scrapy
import json

from scrapy.http.request import Request

class CustomSpider(scrapy.Spider):
    name = 'custom'

    start_urls = ['https://kyfw.12306.cn/otn/userCommon/allProvince']

    custom_settings = {
            'DUPEFILTER_DEBUG': True,
#            'DUPEFILTER_CLASS': "project29.custom_filter.CustomURLFilter"
    }

    def parse_e(self, response):
        self.logger.info(response.url)
        self.logger.info(response.meta)

    def parse(self, response):
        self.logger.info("--------------------------")
        j = json.loads(response.body)
        for prov in j["data"]:
            self.logger.info(prov["chineseName"])

        yield Request(url='https://www.baidu.com/s?wd=1', callback = self.parse_e)
        yield Request(url='https://www.baidu.com/s?wd=3', callback = self.parse_e)
        yield Request(url='https://www.baidu.com/s?wd=3', callback = self.parse_e)
        yield Request(url='https://www.baidu.com/s?wd=3', callback = self.parse_e, meta = {"timestamp":"1"})
        yield Request(url='https://www.baidu.com/s?wd=3', callback = self.parse_e, meta = {"timestamp":"2"})
        yield Request(url='https://www.baidu.com/s?wd=3', callback = self.parse_e, meta = {"timestamp":"2"})

