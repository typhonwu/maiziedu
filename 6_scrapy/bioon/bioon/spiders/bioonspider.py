# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy import FormRequest
import pdb
from bioon import settings
from bioon.items import BioonItem

class BioonspiderSpider(scrapy.Spider):
    name = "bioonspider"
    allowed_domains = ["bioon.com"]
    start_urls=['http://login.bioon.com/login']

    def parse(self,response):

        # 从response.headers中获取cookies信息
        r_headers = response.headers['Set-Cookie']
        cookies_v = r_headers.split(';')[0].split('=')

        cookies = {cookies_v[0]:cookies_v[1]}

        # 模拟请求的头部信息
        headers = {
        'Host':	'login.bioon.com',
        'Referer':'http://login.bioon.com/login',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0',
        'X-Requested-With':'XMLHttpRequest' 
        }

        # 获取验证信息,这个主要通过分析出验证信息所在标签通过xpath获取属性值
        csrf_token = response.xpath(
            '//input[@id="csrf_token"]/@value').extract()[0]
        
        # 获得post的目的URL
        login_url = response.xpath(
            '//form[@id="login_form"]/@action').extract()[0]
        end_login = response.urljoin(login_url)
        
        # 生成post的数据,这些都是通过浏览器分析得知要传送给服务器验证的数据
        formdata={
        # 请使用自己注册的用户名
        'account':'johnson_hugh@163.com',
        'client_id':'usercenter',
        'csrf_token':csrf_token,
        'grant_type':'grant_type',
        'redirect_uri':'http://login.bioon.com/userinfo',
        # 请使用自己注册的用户名
        'username':'礁石',
        # 请使用自己用户名的密码
        'password':'123456',
        }
        
        # FormRequest把要传送的数据，头信息，cookies整合起来进行模拟登录
        # 同时还可以指定发送请求之后对返回的response如何处理的回调函数
        return FormRequest(
        end_login,
        formdata=formdata,
        headers=headers,
        cookies=cookies,
        callback=self.after_login
        )
    # 这是发送模拟登陆请求之后回调的函数
    # 如无意外，返回的将是登陆成功之后的response
    def after_login(self,response):
        
        self.log('Now handling bioon login page.')
        aim_url = 'http://news.bioon.com/Cfda/'
        # json.dumps : dict转成str
        # json.loads:str转成dict
        # 这里登陆请求发送后服务器返回的response.url为http://login.bioon.com/login/do_login
        # pdb调试可知它其实是一个json格式的字符串，所以这里转为字典，方便取数据
        obj = json.loads(response.body)
        
        print "Loging state: ", obj['message']
        if "success" in obj['message']:
            self.logger.info("=========Login success.==========")
        
        return scrapy.Request(aim_url,callback = self.parse_list)
    
    # 这个函数在登陆请求发送并验证之后执行
    # 但是并不要求一定要登陆后才执行
    def parse_list(self,response):
        
        # 获取所有文章链接
        # 注意：@href在chrome中并不能生效
        # 也就是说，chrome中copy xpath功能只能定位到标签
        # 然后属性我们自己再加上
        lis_news = response.xpath(
            '//ul[@id="cms_list"]/li/div/h4/a/@href').extract()
        pdb.set_trace()
        for li in lis_news:
            # 这是scrapy中的response的url拼接函数
            # response.urljoin() 是用来生成绝对地址的方法
            # 并告知 Request ，请求的页面使用 parse_content 这个方法来解析。
            yield scrapy.Request(response.urljoin(li),
                                    callback=self.parse_content)


    def parse_content(self,response):
        
        head = response.xpath(
            '//div[@class="list_left"]/div[@class="title5"]')[0]
        
        item=BioonItem()
        
        item['title'] = head.xpath('h1/text()').extract()[0]
            
        item['source'] = head.xpath('p/text()').re(ur'来源：(.*?)\s(.*?)$')[0]
        
        item['date_time'] = head.xpath('p/text()').re(ur'来源：(.*?)\s(.*?)$')[1]
        
        item['body'] = response.xpath(
            '//div[@class="list_left"]/div[@class="text3"]').extract()[0]
        
        return item