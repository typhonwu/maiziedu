# -*- coding:utf-8 -*-
'''
urllib2比urllib多了requests，定制更加丰富
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

if __name__ == '__main__':
    urlopen()
