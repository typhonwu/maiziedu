# coding:utf-8
from django.shortcuts import render,redirect,resolve_url
from to_do_list.models import Item
# Create your views here.
#待办事项列表
def index(request):
    try:
        item_list = Item.objects.all().order_by("-pub_date")
    except Exception as e:
        print (e)
    return render(request,'index.html',locals())
#添加待办事项,需要对列表进行分页
def add(request):
    try:
        content = request.GET.get("item",None)
        #有输入时才处理
        if len(content) > 0:
            obj = Item.objects.create(content = content)
            #保存成功后再次跳转回待办事项列表
            if obj:
                return redirect(resolve_url("index"))
    except Exception as e:
        print (e)
    #如果保存失败则跳转到提示消息页面
    return render(request,"message.html",{"message":u"待办事项添加失败"})
#修改待办事项
def edit(request):
    pass
#删除待办事项
def delete(request):
    pass
#标记事项完成
def done(request):
    pass
