# coding:utf-8
from django.shortcuts import render

# Create your views here.
#待办事项列表
def index(request):
	return render(request,'index.html',locals())
#添加待办事项,需要对列表进行分页
def add(request):
    pass
#修改待办事项
def edit(request):
    pass
#删除待办事项
def delete(request):
    pass
#标记事项完成
def done(request):
    pass
