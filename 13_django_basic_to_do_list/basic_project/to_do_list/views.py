# coding:utf-8
from django.shortcuts import render,redirect,resolve_url
from to_do_list.models import Item
from django.core.paginator import Paginator,PageNotAnInteger,InvalidPage,EmptyPage
# Create your views here.
#待办事项列表
def index(request):
    try:
        item_list = Item.objects.all().order_by("-pub_date")
        paginator = Paginator(item_list,5)
        try:
            #获取页码并显示
            page = int(request.GET.get("page",1))
            item_list = paginator.page(page)
        #获取页码出错时直接显示第一页
        except (PageNotAnInteger,InvalidPage,EmptyPage):
            item_list = paginator.page(1)
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
    try:
        item_id = request.GET.get("item_id",None)
        content = request.GET.get("item",None)
        if len(item_id) > 0 and len(content) > 0 :
            obj = Item.objects.get(pk=item_id)
            obj.content = content
            obj.save()
        return redirect("/index/")
    except Exception as e:
        print (e)
    return render(request,"message.html",{"message":u"待办事项修改失败"})
#删除待办事项
def delete(request):
    pass
#标记事项完成
def done(request):
    pass
