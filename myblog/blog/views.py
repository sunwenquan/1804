from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,template_name='blog/index2.html')


# 显示所有文章
def articles(request):
    # TODO:获取所有文章
    pass


# 显示所有分类
def category_list(request):
    # TODO:获取所有分类列表
    # TODO: 使用Redis缓存分类列表，提高网站的访问速度
    pass


# 显示某个文章的详情
def article_detail(request,pk):
    # TODO:根据文章的ID，返回对应的内容
    pass