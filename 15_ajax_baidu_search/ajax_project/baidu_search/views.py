# coding:utf-8
from django.shortcuts import render
from baidu_search.models import Item
from django.http import JsonResponse,HttpResponse
from django.core.serializers import serialize
import json
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request,'baidu_search_tutorial.html')
def autoComplete(request):
    query = request.GET.get('query',None)
    if query:
        item_list = Item.objects.filter(title__icontains=query)
    # 列表将会被转化为json数组
    return JsonResponse(item_list,safe=False)

def search(req):
    word = req.GET.get('word','')
    print (word)
    try:
        if word:
            #区别contains和icontains，后者忽略大小写
            #考虑到实现效果4条一页，这里也这样分页
            paginator = Paginator(Item.objects.filter(title__icontains=word),4)
            #这里把列表序列化，然后取名为json，二者形成键值对的json对象，传给word_list
            #先返回第一页的四条记录
            word_list = serialize('json',paginator.page(1))
            #这里不需要返回模板，返回json即可,需要把它用dumps打包一下，指明类型
    except:
        pass
    return HttpResponse(json.dumps(word_list),content_type='application/json')
  
