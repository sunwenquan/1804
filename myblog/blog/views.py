from django.shortcuts import render
from blog.models import Article,Category

# Create your views here.

def home(request):
    """显示所有文章分类，和所有文章标题"""
    categories = Category.objects.all()
    posts = Article.objects.all()
    # posts = Article.objects.raw("select * from blog_article")
    c = {
        'categories': categories,
        'posts': posts
    }
    c
    return render(request, template_name='blog/index3.html'
                  , context=c)


# 显示所有分类
def category_list(request):
    # 获取所有分类列表
    # 获得所有用all
    categories = Category.objects.all()
    return render(request,template_name='blog/category.html'
                  ,context={'categories':categories})
    # TODO: 使用Redis缓存分类列表，提高网站的访问速度

# 显示某分类下的所有文章
def articles_by_category(request,category_id):
    # 获得不确定个数的对象，用filter
    posts = Article.objects.filter(category_id=category_id)
    # print(posts.query)
    categories = Category.objects.all()
    c = {
        'categories': categories,
        'posts': posts
    }

    return render(request,template_name='blog/index3.html',context=c)

# 显示所有文章
def articles(request):
    # TODO:获取所有文章
    posts = Article.objects.all()
    return render(request,template_name='blog/index3.html',context={'posts':posts})



# 显示某个文章的详情
def article_detail(request,article_id):
    # 获得某个用get
    post = Article.objects.get(id=article_id)
    return render(request, template_name='blog/detail.html',
                  context={"post": post})


# TODO: 分页