# -*- coding:utf-8 -*-
'''
urllib2比urllib多了urllib2.Request对象，请求头定制更加丰富
urllib独有编码解码功能
'''
import urllib2
import urllib # 这里主要为了用它进行编码

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

def request_post_debug():
    # POST
    data = {'username': 'kamidox', 'password': 'xxxxxxxx'}
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(
        'http://www.douban.com',
        data=urllib.urlencode(data),
                    headers=headers)
    # 自定义handler，这是urllib2的特色。调试等级为1，会打印与服务器交互的信息
    opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
    s = opener.open(req)
    print s.read(100)
    s.close()

def install_debug_handler():
    opener = urllib2.build_opener(
        urllib2.HTTPHandler(debuglevel=1),
        urllib2.HTTPSHandler(debuglevel=1))
    urllib2.install_opener(opener) # 把自定义的handler安装成默认

if __name__ == '__main__':
    install_debug_handler()  # 调用这个方法把定义好的handler安装到默认
    request()
