# -*- coding:utf-8 -*-
'''
urllib2比urllib多了urllib2.Request对象，请求头定制更加丰富
urllib独有编码解码功能
'''
import urllib2

def urlopen():
    url = 'http://blog.kamidox.com/no_exist'
    try:
        s = urllib2.urlopen(url, timeout=3)
    except urllib2.HTTPError,e:
        print e
    else:
        print s.read(100)
        s.close()

def request():
    # 定制 HTTP 头
    headers = {'User-Agent': 'Mozilla/5.0','x-my-header': 'my value'}
    req = urllib2.Request('http://blog.kamidox.com',headers=headers)
    # urlopen既可以接受网址为参数，也可以接受request对象为参数，后者可以定制请求头
    s = urllib2.urlopen(req)
    print s.read(100)
    print s.headers # 打印回应头的全部信息
    s.close()

if __name__ == '__main__':
    request()
