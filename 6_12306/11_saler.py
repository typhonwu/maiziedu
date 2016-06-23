# -*- coding: utf-8 -*-

import time
import json

import requests
from bs4 import BeautifulSoup

def fetch_provinces():
    # 通过开发者工具发现这个url
    url = "https://kyfw.12306.cn/otn/userCommon/allProvince"

    try:
        # 因为是发送https请求，所以加入verify参数
        s = requests.get(url, verify=False)
    except Exception, e:
        print "fetch provinces. " + url
        raise e

    j = json.loads(s.content)
    return j["data"]

if __name__ == "__main__":
    provs = fetch_provinces()
    for prov in provs:
        print prov["chineseName"]
