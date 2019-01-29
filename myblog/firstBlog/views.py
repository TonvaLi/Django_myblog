from django.shortcuts import render
from .models import Blog
from django.template import loader
from django.http import HttpResponse

# Create your views here.
# 获取url,发送给服务器，并返回

def showBlogLists(request):
    tmp = loader.get_template('firstBlog/bloglists.html')
    blog = Blog.objects.all()
    context = {'blog': blog}
    res = tmp.render(context)
    return HttpResponse(res)

def showBlog(request, search_id):
    tmp = loader.get_template('firstBlog/blogDetail.html')
    blog = Blog.objects.get(id=search_id)
    context = {'blog':blog}
    res = tmp.render(context)
    return HttpResponse(res)

def editPage(request, blog_id):
    if str(blog_id) == '0':
        return render(request, 'firstBlog/edit_page.html')
    else:
        blog = Blog.objects.get(pk=blog_id)
        return render(request, 'firstBlog/edit_page.html', {'blog':blog})

def submitPage(request):
    title = request.POST.get('title', 'TITLE')
    author = request.POST.get('author', 'AUTHOR')
    content = request.POST.get('content', 'CONTENT')
    Blog.objects.create(title=title, author=author, content =content)
    blog = Blog.objects.all()
    return render(request, 'firstBlog/bloglists.html',{'blog':blog})





