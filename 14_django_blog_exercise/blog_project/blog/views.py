# -*- coding:utf-8 -*-
import pdb
from django.shortcuts import render
import logging
from django.conf import settings
from django.db.models import Count
from blog.models import *
#这是django的原生分页类，可以做许多设置
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
#使用setting.py中配置的日志器，一般都在views.py中使用日志器，因为这里都是业务逻辑
logger = logging.getLogger('blog.views')
#用setting数据定义全局变量,返回一个字典
def global_setting(request):
    #用变量装settings的设置,才能通过locals()传过去
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC
    #重构一：把类别，广告，归档这些公用内容提出来
    category_list = Category.objects.all()
    ad_list = Ad.objects.all()[:5]
    archive_list = Article.objects.distinct_date()
    article_list = Article.objects.all()
    #标签云数据
    tag_list = Tag.objects.all()
    #友情链接数据
    link_list = Links.objects.all()
    #文章排行榜数据-按点击排序
    click_article_list = article_list.order_by('click_count')
    #文章排行榜数据-按评论排序
    comment_article_list=[]
    result_list = Comment.objects.with_counts()
    #pdb.set_trace()
    for article_id in result_list:
        article = Article.objects.get(id = article_id)
        comment_article_list.append(article)
    #老师直接用聚合函数做评论排序
    #comment_count_list = Comment.objects.values('article')\
    #        .annotate(comment_count =\
    #        Count('article').order_by('-comment_count'))
    #comment_article_list = Article.objects.get(pk=comment[article])\
    #        for comment in comment_count_list
    
    #文章排行榜数据-只选推荐的
    recommend_article_list = Article.objects.filter(is_recommend = True)
    return locals()

# Create your views here.
#定义首页方法
def index(request):
    try:
        article_list = getPage(article_list)
    except Exception as e:
        #如果出现异常就写入日志
        logger.error(e)
    return render(request,'index.html',locals())
def archive(request):
    try:
        #先获取客户端提交的信息
        year = request.GET.get('year',None)
        month = request.GET.get('month',None)
        #同样的文章分页,但是用到filter()做模糊查询
        article_list = Article.objects.filter\
        (date_publish__icontains = year+'-'+month)
        article_list = getPage(article_list)
    except Exception as e:
        logger.error(e)
    return render(request,'archive.html',locals())

def tag(request):
    try:
        #先获取客户端提交的标签
        tag = request.GET.get('tag',None)
        #注意这里tag和article是多对多关系，需要分两步取出标签下的所有文章，要用到_set
        tag = Tag.objects.get(name = tag)
        article_list = tag.article_set.all()
        article_list = getPage(article_list)
    except Exception as e:
        logger.error(e)
    return render(request,'tag.html',locals())

#重构分页代码
def getPage(request,article_list):
    paginator = Paginator(article_list,10)
    try:
        page = int(request.GET.get('page',1))
        article_list = paginator.page(page)
    except (EmptyPage,InvalidPage,PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list 
    
