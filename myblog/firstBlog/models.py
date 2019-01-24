from django.db import models

# Create your models here.
# 设计数据库表

class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,)  # CASCADE: 级联删除 此参数避免两个表里的数据不一致
    content = models.TextField()
    visits = models.IntegerField(default=0)
    pubDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title