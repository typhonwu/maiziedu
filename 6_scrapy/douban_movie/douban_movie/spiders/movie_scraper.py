# -*- coding: utf-8 -*-
import scrapy
from douban_movie.items import DoubanMovieItem

class movie_scraper(scrapy.Spider):
    name = 'douban_movie_spider'
    allowed_domains = ["http:/www.douban.com"]
    start_url = (
        'https://movie.douban.com/subject/10484117/?tag=热门&from=gaia'
    )

    def parse(self,response):

        a_list = response.xpath("//*[@id='gaia']/div[4]/div/a")

        if not a_list:
            self.log("List Page error-- %s" % response.url)

        print a_list
