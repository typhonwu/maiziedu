from django.conf.urls import url
from blog.views import index,archive

urlpatterns = [
    url(r'^$',views.index,name='index'),
    #映射到归档页面
    url(r'^archive/',views.archive,name='archive'),
    #映射到标签页面
    url(r'^tag/',views.tag,name='tag'),
]