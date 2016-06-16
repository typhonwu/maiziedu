# -*- utf-8 -*-
'''
爬取python贴吧里面用户名及头像图片信息.爬取网页链接:http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5，只需要爬取该贴吧链接里面的头像即可,用户名作为头像图片的名称。
'''
import requests
import re
from HTMLParser import HTMLParser
import os
from pip.download import user_agent


class python_tieba_spider():
    def __init(self):
        self.url = 'http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5'
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0'


    def get_page(self):
        pass

    def parse(self,content):
        pass

    def save(self):
        pass

    def run(self):
        print('开始抓取python贴吧用户名及图片信息...')
        content = self.get_page(self.url)
        items = self.parse(content)
        self.save(items,'python_tieba_users')

class UserParser(HTMLParser):
    def __init__(self):
        pass

    def handle_starttag(self,tag,attrs):
        pass

    def handle_data(self,data):
        pass

    def handle_
if __name__ == '__main__'
    pts = python_tiea_spider()
    pts.run()