# coding:utf-8
from django.db import models

# Create your models here.
class Item(models.Model):
    content = models.CharField(max_length=100,verbose_name=u"待办事项")
    is_done = models.BooleanField(default=False,verbose_name=u"事项状态")
    pub_date = models.DateTimeField(auto_now_add=True,verbose_name=u"发布时间")
    #指定后台看到的信息
    class Meta:
        verbose_name = '待办事项'
        verbose_name_plural = verbose_name
    #python3用这个返回信息，python2用__unicode__
    def __str__(self):
        return self.title
