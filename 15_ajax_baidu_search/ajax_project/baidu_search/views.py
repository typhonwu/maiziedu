from django.shortcuts import render
from baidu_search.models import Item
import json
# Create your views here.
def autoComplete(request):
    query = request.GET.get('query',None)
    if query:
        item_list = Item.objects.filter(title__contains=query)
        # 列表将会被转化为json数组
        result = json.dumps(item_list)
    return HttpResponse(result,content_type="application/json")
