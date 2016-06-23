# -*- coding: utf-8 -*-

import time
import json

import requests
from bs4 import BeautifulSoup

def fetch_provinces():
    url = "https://kyfw.12306.cn/otn/userCommon/allProvince"

    try:
        s = requests.get(url, verify = False)
    except Exception, e:
        print "fetch provinces. " + url
        raise e

    j = json.loads(s.content)
    return j["data"]

if __name__ == "__main__":
    provs = fetch_provinces()
    for prov in provs:
        print prov["chineseName"]



    



    


    














# vim: set ts=4 sw=4 sts=4 tw=100 et:
