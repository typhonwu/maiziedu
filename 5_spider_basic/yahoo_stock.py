# -*- coding:utf-8 -*-
import urllib

def download_stock_data(stock_list):
    # 对列表中的股票id一一获取记录
    for sid in stock_list:
        url = 'http://table.finance.yahoo.com/table.csv?s=' + sid
        fname = sid + '.csv'
        print 'downloading %s from %s' % (fname,url)
        urllib.urlretrieve(url,fname)

if __name__ == '__main__':
    stock_list = ['300001.sz','300002.sz']
    download_stock_data(stock_list)
