from django.urls import path
from django.conf.urls import url, re_path
from . import views

urlpatterns = [
    url(r'^$', views.showBlogLists, name='blog'),
    # url('^(\d+)$', views.showBlog)
    re_path('(?P<search_id>\d+)', views.showBlog, name='blog_detail'),
    re_path('^edit/(?P<blog_id>\d+)', views.editPage, name='edit_page'),
    url(r'^edit/page$', views.submitPage, name='submit_page')
]

