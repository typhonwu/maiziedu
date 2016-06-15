# -*- coding: utf-8 -*-
import requests
import re
from HTMLParser import HTMLParser


def _attr(attrs, attrname):
    for attr in attrs:
        if attr[0] == attrname:
            return attr[1]
    return None


class PoemParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        # 默认未进入特定的标签，后面如果找到符合条件的标签再改为True,然后开始抓取
        self.in_div = False
        self.in_a = False
        self.tangshi_list = []
        self.current_poem = {}
        pass

    def handle_starttag(self, tag, attrs):
        # 如果找到目标标签内容，就把标志改为True
        if tag == 'div' and _attr(attrs, 'class') == 'guwencont2':
            self.in_div = True

        if tag == 'a' and self.in_div:
            self.in_a = True
            self.current_poem['url'] = _attr(attrs, 'href')

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass


def retrive_tangshi_300():
    url = 'http://www.gushiwen.org/gushi/tangshi.aspx'
    r = requests.get(url)
    # 专门解析唐诗的解析器
    parser = PoemParser()
    parser.feed(r.content)
    return parser.tangshi_list


if __name__ == '__main__':
    l = retrive_tangshi_300()
    print('total %d poems.' % len(l))
    for i in range(10):
        print('标题: %(title)s\t作者：%(author)s\tURL: %(url)s' % (l[i]))

