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
        # 定义一个内部函数用来解析属性
        def _attr(attrlist, attrname):  # 传入属性列表和要获取属性值的属性名
            for attr in attrlist:  # 取出的attr是元组，0下标指属性名，1下标指向属性值
                if attr[0] == attrname:
                    return attr[1]
            return None

    def handle_data(self,data):
        pass

def retrive_users():
    url = 'http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5'
    r = requests.get(url)
    parser = poemParser()
    parser.feed(r.content)
    return parser.user_list

if __name__ == '__main__':
    l = retrieve_users()
    print('total %d users' % len(l))
    