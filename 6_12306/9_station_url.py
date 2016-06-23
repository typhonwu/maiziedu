# -*- coding: utf-8 -*-

import time

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    url = "http://www.12306.cn/mormhweb/kyyyz/"

    try:
        s = requests.get(url)
    except Exception, e:
        print "requests url fail. " + url
        raise e

    b = BeautifulSoup(s.content, "lxml")
    names = b.select("#secTable > tbody > tr > td")
    sub_urls = b.select("#mainTable td.submenu_bg > a")

    for i in range(0, len(names)):
        sub_url1 = sub_urls[i * 2]["href"]
        sub_url2 = sub_urls[i * 2 + 1]["href"]
        print names[i].text, sub_url1, sub_url2


    



    


    














# vim: set ts=4 sw=4 sts=4 tw=100 et:
