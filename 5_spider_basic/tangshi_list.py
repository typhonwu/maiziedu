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
        self.tangshi_list = []
        self.current_poem = {}
        pass

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass


def retrive_tangshi_300():
    url = 'http://www.gushiwen.org/gushi/tangshi.aspx'
    r = requests.get(url)
    parser = PoemParser()
    parser.feed(r.content)
    return parser.tangshi_list


if __name__ == '__main__':
    l = retrive_tangshi_300()
    print('total %d poems.' % len(l))
    for i in range(10):
        print('标题: %(title)s\t作者：%(author)s\tURL: %(url)s' % (l[i]))

