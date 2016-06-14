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

if __name__ == '__main__':
    get_json()