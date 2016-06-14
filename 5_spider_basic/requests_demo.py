# -*- coding: utf-8 -*-
'''
requests:第三方库，http for humans
'''


import requests


def get_json():
    r = requests.get('https://api.github.com/events')
    print(r.status_code)
    # print(r.content)
    print(r.text)
    print(r.headers)
    # print(r.json())

def get_querystring():
    # 这个网址专门用于测试http协议
    url = 'http://httpbin.org/get'
    params = {'qs1': 'value1', 'qs2': 'value2'}
    r = requests.get(url, params=params)
    print(r.status_code)
    print(r.content)


def get_custom_headers():
    headers = {'x-header1': 'value1', 'x-header2': 'value2'}
    r = requests.get('http://httpbin.org/get', headers=headers)
    print(r.status_code)
    print(r.content)

if __name__ == '__main__':
    # get_json()
    # get_querystring()
    get_custom_headers()