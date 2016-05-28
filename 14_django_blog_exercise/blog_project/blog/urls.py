from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    # 映射到归档页面
    url(r'^archive/', archive, name='archive'),
    # 映射到文章页面
    url(r'^article/$', article, name='article'),
    # 映射到标签页面
    url(r'^tag/', tag, name='tag'),
    # 登录注册注销
    url(r'^logout$', do_logout, name='logtout'),
    url(r'^login$', login, name='login'),
    url(r'^reg$', reg, name='reg'),
]
