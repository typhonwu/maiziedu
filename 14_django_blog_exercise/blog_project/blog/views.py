from django.shortcuts import render

# Create your views here.
#定义首页方法
def index(request):
    return render(request,'index.html',locals())
