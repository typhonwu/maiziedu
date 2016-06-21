# -*- coding: utf-8 -*-
import scrapy


class DoubanMovieItem(scrapy.Item):
    title = scrapy.Field()
    intro = scrapy.Field()
    post_url = scrapy.Field()
