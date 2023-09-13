from django.db import models

# Create your models here.
from django.db import models


# 这个文件是数据库的 ORM 文件, Django 框架会根据定义自动生成对应的数据库表
# 每个模型被定义为 django.db.models.Model 类的子类
# 为了让 Django 依照这个文件创建数据库表,
# 需要将 polls.apps.PollsConfig (代表 Polls 应用的配置信息) 加入到 settings.py 的 INSTALLED_APP 中
class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 每个变量表示一个数据库字段, models.xxx 表示数据库类型
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

