# -*- coding: utf-8 -*-
import urllib

def demo():
    s = urllib.urlopen('http://blog.kamidox.com')
    # print s.read(100)
    # print s.read() # 全部读出来
    # print s.readline() # 只打印一行
    # lines = s.readlines() # 返回一个列表
    # for line in s.readlines(): print line
    # print s.getcode() #获得状态码
    # -----------------------------------------------------------------------------
    msg = s.info() # 返回一个httpmessage对象
    # print dir(msg) # 使用dir函数获得对象所有方法
    # print msg.headers # 是一个列表
    # print msg.items() # 返回一个列表，包含头文件各个字段组成的元组
    # print msg.getheader('Content-Type') #获取头文件中指定字段的值
    # print msg.gettype() # 获取回应文件类型
    # print msg.getheaders() # 需要传入两个参数 
    # print msg.keys()

# ------------------------urllib.urlretrieve方式:用于获取文件
def retrieve():
    # 从第一个参数开始获取文件，以第二个参数为保存路径
    # python简洁写法，右边本来就要返回一个元组，包含两个值
    # 然后左边两个参数就是元组解包
    fname,msg = \
    urllib.urlretrieve('http://blog.kamidox.com','index.html', reporthook=progress)
    print fname # 这是文件保存路径
    print msg.items() # msg是httpmessage对象

# --------------------------用reporthook实现下载进度
def progress(block,block_size,total_size):
    print('%d/%d - %0.2f%%' % 
        (block * block_size, total_size, 
        (float)(block * block_size) * 100 / total_size))
    
# --------------------------用urllib进行编码和解码
def urlencode():
    params = {'score' : 100, 'name':'爬虫基础', 'coment': 'very good'}
    qs = urllib.urlencode(params)
    print qs

if __name__=='__main__':
    urlencode()
