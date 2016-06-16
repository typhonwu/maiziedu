# -*- coding:utf-8 -*-
'''
爬取python贴吧里面用户名及头像图片信息.爬取网页链接:http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5，只需要爬取该贴吧链接里面的头像即可,用户名作为头像图片的名称。
'''
import requests
import re
from HTMLParser import HTMLParser
import pdb

class UserParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.user_list = []
        pass

    def handle_starttag(self,tag,attrs):
        pass

    def handle_data(self,data):
        pass

def retrive_users():
    url = 'http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5'
    r = requests.get(url)
    parser = poemParser()
    parser.feed(r.content)
    return parser.user_list

if __name__ == '__main__':
    retrieve_users()