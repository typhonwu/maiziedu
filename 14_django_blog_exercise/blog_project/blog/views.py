# -*- coding:utf-8 -*-
from django.shortcuts import render
import logging
from django.conf import settings
from blog.models import *
#使用setting.py中配置的日志器，一般都在views.py中使用日志器，因为这里都是业务逻辑
logger = logging.getLogger('blog.views')
#用setting数据定义全局变量,返回一个字典
def global_setting(request):
    return {'SITE_NAME':settings.SITE_NAME,
            'SITE_DESC':settings.SITE_DESC}
# Create your views here.
#定义首页方法
def index(request):
    try:
        category_list = Category.objects.all()
    except Exception as e:
        #如果出现异常就写入日志
        logger.error(e)
    return render(request,'index.html',{'category_list':category_list})
