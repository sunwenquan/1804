from django.urls import path,re_pathfrom blog import viewsurlpatterns = [    # blog的主页    path('home/',views.home),    path('articles/',views.articles),    path('categories/',views.category_list),    # TODO: 用正则表达式传递文章ID    re_path('detail/',views.article_detail),]