from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$',index,name='index'),
    #映射到归档页面
    url(r'^archive/',archive,name='archive'),
    #映射到标签页面
    url(r'^tag/',tag,name='tag'),
]