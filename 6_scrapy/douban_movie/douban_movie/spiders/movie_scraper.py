# -*- coding: utf-8 -*-
import scrapy
import pdb
from douban_movie.items import DoubanMovieItem
import re

class movie_scraper(scrapy.Spider):
    name = 'douban_movie_spider'
    # 设置headers，注意每行要加逗号
    allowed_domains = ["douban.com"]

    def start_requests(self):
        headers = {
        'Accept':'*/*',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        # 暂时不用cookie试试。 'Cookie':'bid=yAMd84V94sg; ps=y; ll="118318"; ue="hughohoho@gmail.com"; dbcl2="113667643:Aku7Uxb2dSY"; ck=Hwp_; ap=1; __utma=30149280.743563175.1422940286.1466065258.1466501870.13; __utmc=30149280; __utmz=30149280.1465956799.11.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utmv=30149280.11366; __utma=223695111.1387345932.1466501870.1466501870.1466501870.1; __utmc=223695111; __utmz=223695111.1466501870.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); push_noty_num=0; push_doumail_num=4; _pk_id.100001.4cf6=f63938885dc79088.1466501870.2.1466574649.1466503191.; _pk_ses.100001.4cf6=*'
        'Host':'movie.douban.com',
        'Referer':'https://movie.douban.com/explore',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
        }


        url = "https://movie.douban.com/explore"
        # yield scrapy.Request(url = url, headers = headers)
        return [
            scrapy.Request(url = url, headers = headers,  ),
        ]
    
    def parse(self,response):
        print response.url
        cookie_list = response.headers['Set-Cookie'].split(';')
        cookie_value = [x.split('=')[1] for x in cookie_list]
        print cookie_value
        print cookie_str
        
        formdata = {
            'type':'movie',
            'tag':'热门',
            'sort':'time',
            'page_limit':'20',
            'page_start':'0',
        }

        # a_list = response.xpath("//*[@id='gaia']/div[4]/div/a")

        #if not a_list:
         
        #   self.log("List Page error-- %s" % response.url)

        # yield FormRequest()
