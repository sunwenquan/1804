from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Article,Category

# Create your views here.

def home(request,page=1):
    """显示所有文章分类，和所有文章标题"""
    categories = Category.objects.all()
    posts = Article.objects.all()[:100]

    # posts = Article.objects.raw("select * from blog_article")

    # 分页功能
    # 1. 创建分页对象
    paginator = Paginator(posts, 2)
    # 2. 获得分页对象的总页数
    num_pages = paginator.num_pages
    # 3. 获取第page页数据
    posts = paginator.page(page)
    pages = range(1, 6)
    page = int(page)
    # 4. 页面范围控制

    # 4.1.总页数<5, 显示所有页码   1 2 3 4 5

    if num_pages < 5:
        pages = range(1,6)
    # 4.2.当前页是前3页，显示1-5页 1 2 3 4 5
    elif page <=3:
        pages = range(1,6)
    # 4.3.当前页是后3页，显示后5页 6 7 8 9 10
    elif page > num_pages - 3:
        pages = range(num_pages-4,num_pages+1)  # 后5 页
    # 4.4.其他情况，显示当前页前2页，后2页，当前页   10 11 12 13 14 15
    else:
        pages = range(page-2,page+3)  #  page = 6, 4 5 6 7 8  ,page放中间


    c = {
        'categories': categories,
        'posts': posts,
        'pages': pages,
        'cur_page':page,
    }

    return render(request, template_name='blog/index.html'
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