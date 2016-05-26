# -*- coding:utf-8 -*-
from django.shortcuts import render
import logging
#使用setting.py中配置的日志器，一般都在views.py中使用日志器，因为这里都是业务逻辑
logger = logging.getLogger('blog.views')
# Create your views here.
#定义首页方法
def index(request):
    try:
        file = open('sss.txt','r')
    except Exception as e:
        #如果出现异常就写入日志
        logger.error(e)
    return render(request,'index.html',locals())
