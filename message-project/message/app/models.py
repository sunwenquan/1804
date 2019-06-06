from django.db import models

# Create your models here.

# ORM  对象关系映射
# - 对象  Message是一个类，msg = Message(name='gavin') 就是一个对象
# - 关系  实体和实体之间的关系
# - 映射
#   :  app_message表   和  Message类 是一一对应的
#   :  app_message表中每条记录  和   Message类创建的每个对象时一一对应的

class Message(models.Model):
    name = models.CharField(max_length=30,verbose_name="姓名")
    email = models.EmailField(max_length=20,verbose_name='邮箱')
    address = models.CharField(max_length=50,verbose_name='地址')
    content = models.CharField(max_length=200,verbose_name='留言内容')

