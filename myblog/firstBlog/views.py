from django.shortcuts import render
from .models import Blog
from django.template import loader
from django.http import HttpResponse

# Create your views here.
# 获取url,发送给服务器，并返回
def showBlogLists(request):
    tmp = loader.get_template('bloglists.html')
    blog = Blog.objects.all()
    context = {'blog': blog}
    res = tmp.render(context)
    return HttpResponse(res)