from django.contrib import admin
from blog.models import Article,Category

# Register your models here.

# 创建admin_site对象

admin.site.register(Article)
admin.site.register(Category)


