# -*- coding: utf-8 -*-
import scrapy
import pdb
from douban_movie.items import DoubanMovieItem

class movie_scraper(scrapy.Spider):
    name = 'douban_movie_spider'
    allowed_domains = ["douban.com"]
    start_url = (
        'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0',
    )

    def parse(self,response):
        a_list = response.xpath("//*[@id='gaia']/div[4]/div/a")

        if not a_list:
            self.log("List Page error-- %s" % response.url)

