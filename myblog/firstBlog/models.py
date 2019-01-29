from django.db import models

# Create your models here.
# 设计数据库表

# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()
#     def __str__(self):
#         return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    content = models.TextField()
    def __str__(self):
        return self.title