# -*- coding:utf-8 -*-
'''
爬取python贴吧里面用户名及头像图片信息.爬取网页链接:http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5，只需要爬取该贴吧链接里面的头像即可,用户名作为头像图片的名称。
'''


'''
要获取的html标签范围：
<div class="threadlist_lz clearfix"> # 这是第一个定位标签
    <div class="threadlist_title pull_left j_th_tit ">
        <a href="/p/4612057728" title="【腾讯课堂免费Python直播课程】秒杀一切Python视频资料" target="_blank" class="j_th_tit ">【腾讯课堂免费Python直播课程】秒杀一切Python视频资料</a>
    </div>
    <div class="threadlist_author pull_right">


    # 这是第二个定位标签，其中title是作者


    <span class="tb_icon_author " title="主题作者: openlabczx" data-field="{&quot;user_id&quot;:1087985062}">
        <i class="icon_author"></i>


        # 这是最后一个定位标签，其中href就是用户首页，可以获取头像，注意要拼接一下


        <a data-field="{&quot;un&quot;:&quot;openlabczx&quot;}" class="frs-author-name j_user_card " href="/home/main/?un=openlabczx&amp;ie=utf-8&amp;fr=frs" target="_blank">openlabczx</a>
        <span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    
    </span>
    <span class="pull-right is_show_create_time" title="创建时间">6-15</span>
</div>
            </div>
'''
import requests
import re
from HTMLParser import HTMLParser
import pdb
import chardet

class UserParser(HTMLParser):
    def __init__(self): # 一次请求只初始化一次
        HTMLParser.__init__(self)
        self.user_list = []
        self.in_div = False
        self.in_span = False
        self.current_user = {}
        self.user_list =[]

    def handle_starttag(self,tag,attrs):

        # 定义一个内部函数用来解析属性
        def _attr(attrlist, attrname):  # 传入属性列表和要获取属性值的属性名
            for attr in attrlist:  # 取出的attr是元组，0下标指属性名，1下标指向属性值
                if attr[0] == attrname:
                    return attr[1]
            return None
        # 确认用户名所在的div标签
        if tag == 'div' and _attr(attrs, 'class') == 'threadlist_lz clearfix':
            # pdb.set_trace()
            # print tag+':' + _attr(attrs, 'class')
            self.in_div = True

        # 轮到其中的span标签，可以获得用户名
        if self.in_div and tag == 'span': 
            self.in_span = True
            # print _attr(attrs, 'title')
            if _attr(attrs, 'title'):
                self.current_user['name'] = re.split(': ', # 把属性值分段
                    _attr(attrs, 'title')
                    # 要先转为字符串才能切分，然后取用户名,取完后还得转回unicode串  
                    .encode("utf-8"))[1].decode("utf-8")

        # 获取用户主页链接
        if self.in_span and tag == 'a':
            # print 'http://tieba.baidu.com' + _attr(attrs, 'href')
            # 拼接后获取用户信息
            user_info= requests.get('http://tieba.baidu.com' + _attr(attrs, 'href'))
            parser = UserInfoParser()
            parser.feed(user_info.content)
            # 把用户信息解析类返回的头像链接放入
            self.current_user['portrait'] == parser.img_url
            # 注意取完后关闭一下,并初始化 
            self.user_list.append(self.current_user)
            self.current_user = {}
            self.in_div = False
            self.in_span = False

# 用户头像解析类
class UserInfoParser(HTMLParser):
    def __init__(self):
        self.in_a = False

    # 定义一个内部函数用来解析属性
    def _attr(attrlist, attrname):  # 传入属性列表和要获取属性值的属性名
        for attr in attrlist:  # 取出的attr是元组，0下标指属性名，1下标指向属性值
            if attr[0] == attrname:
                return attr[1]
        return None

    def handle_starttag(self, tag, attrs):
        if tag == 'a' and self._attr(attrs, 'class') == 'userinfo_head':
            self.in_a = True

    def handle_startendtag(self, tag, attrs):
        if tag == 'img' and self.in_a:
            self.img_url == self._attr(attrs, 'src')


def retrieve_users():
    url = 'http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5'
    r = requests.get(url)
    parser = UserParser()
    print chardet.detect(r.content)
    parser.feed(r.content.decode('utf-8'))
    # print parser.user_list
    for user in parser.user_list:
        pass

if __name__ == '__main__':
    l = retrieve_users()
    # print('total %d users' % len(l))
