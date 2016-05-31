from django.shortcuts import render
from baidu_search.models import Item
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'baidu_search.html')
def autoComplete(request):
    query = request.GET.get('query',None)
    if query:
        item_list = Item.objects.filter(title__contains=query)
    # 列表将会被转化为json数组
    return JsonResponse(item_list,safe=False)
