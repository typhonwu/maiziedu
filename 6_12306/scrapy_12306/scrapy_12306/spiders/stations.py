# -*- coding: utf-8 -*-
import json
import urllib

import scrapy
from scrapy.http.request import Request
from scrapy_12306.items import StationItem
from scrapy_12306.items import CommitItem

class StationsSpider(scrapy.Spider):
    name = 'StationsSpider'
    start_urls = ['http://www.12306.cn/mormhweb/kyyyz/']

    custom_settings = {
            'ITEM_PIPELINES': {
                'scrapy_12306.pipelines.StationSQLPipeline': 300,
            },
    }

    def parse(self, response):
        # css选择器就是chrome中复制selector那个
        # 返回一个选择器，extract后返回字符串，是unicode编码
        names = response.css("#secTable > tbody > tr > td::text").extract()
        sub_urls = response.css("#mainTable td.submenu_bg > a::attr(href)").extract()
        # 第一次请求站点页面之后再根据抓取的站点名称分别发出数据请求
        # 第二次请求响应的是站点数据
        for i in range(0, len(names)):
            sub_url1 = response.url + sub_urls[i * 2][2:]
            yield Request(sub_url1, callback = self.parse_station, meta = {'bureau':names[i], 'station':True})

            sub_url2 = response.url + sub_urls[i * 2 + 1][2:]
            yield Request(sub_url2, callback = self.parse_station, meta = {'bureau':names[i], 'station':False})
    # 对第二次请求得到的响应进行解析
    def parse_station(self, response):
        datas = response.css("table table tr")
        if len(datas) <= 2:
            return
        for i in range(0, len(datas)):
            if i < 2:
                continue
            infos = datas[i].css("td::text").extract()

            item = StationItem()
            item["bureau"] = response.meta["bureau"]
            item["station"] = response.meta["station"]
            item["name"] = infos[0]
            item["address"] = infos[1]
            item["passenger"] = infos[2].strip() != u""
            item["luggage"] = infos[3].strip() != u""
            item["package"] = infos[4].strip() != u""
            yield item
        yield CommitItem()



