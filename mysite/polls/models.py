from django.db import models

# Create your models here.

# 投票应用：Question和Choice两个模型

# Question：问题描述和发布时间
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

# Choice：选项描述和当前投票数
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)      # models.CASCADE:删除主表时，关联的从表自动被删除
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text