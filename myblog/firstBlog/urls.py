from django.urls import path
from django.conf.urls import url, re_path
from . import views

urlpatterns = [
    url(r'^$', views.showBlogLists),
    # url('^(\d+)$', views.showBlog)
    re_path('(?P<search_id>\d+)', views.showBlog, name='search_details')
]

