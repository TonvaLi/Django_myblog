from django.contrib import admin

# Register your models here.
from .models import Blog

admin.site.register(Blog)       # 将Blog应该注册到Admin中