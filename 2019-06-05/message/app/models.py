from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=30,verbose_name="姓名")
