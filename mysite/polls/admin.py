from django.contrib import admin

# Register your models here.

from .models import Question

admin.site.register(Question)       # 将Question对象添加到Admin中，统一管理