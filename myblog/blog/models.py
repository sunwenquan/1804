from django.db import models

# Create your models here.




class Category(models.Model):
    """
    类别名：name
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Article(models.Model):
    """
    标题：title
    内容：content
    创建时间：created_time
    """
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    created_time = models.DateTimeField(auto_now_add=True)
    # 分类被删除的时候，分类下的文章要删除吗？category存储的是分类ID
    category = models.ForeignKey(to='Category',on_delete=models.SET_DEFAULT,default='1')

    # TODO:集成DjangoUeditor富文本编辑

    def __str__(self):
        """定制对象的可读性"""
        return self.title