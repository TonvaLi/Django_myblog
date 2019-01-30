from django.contrib import admin

# Register your models here.
from .models import Blog
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content')

admin.site.register(Blog, BlogAdmin)       # 将Blog应该注册到Admin中