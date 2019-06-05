from django.shortcuts import render

# Create your views here.


def hello(request):
    return render(request,template_name='index.html')


def add_message(request):
    """
    把留言保存到数据库
    :param request:
    :return:
    """
    pass

