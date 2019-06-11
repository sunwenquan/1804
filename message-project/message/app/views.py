from django.shortcuts import render

# Create your views here.
from app.models import Message


def hello(request):
    return render(request, template_name='index.html')


def add_message(request):
    """
    把留言保存到数据库
    :param request:
    :return:返回响应Response
    """
    # 思考：如何知道request是GET还是POST?
    #       - request是不是对象？  是
    #       - request有什么属性和方法？  dir(request)
    # print(dir(request))
    # print(request.method)

    #  browser    --获得(GET)留言表单--->     server
    #  browser    <---把留言表返回给浏览器--- server
    #  browser    ----把填好的表单提交(POST)给server---> server
    #  ..... server 开始保存数据到数据库
    #  browser    < ------成功或失败的信息返回给浏览器---server

    # 如果是GET请求，把留言表单发给用户，让用户填写留言信息
    if request.method == 'GET':
        return render(request, template_name='msg2.html')

    # 如果是POST请求，从请求request中获取提交的内容
    if request.method == 'POST':
        # print(request.POST)
        c = {
            'msg': '提交成功！'
        }

        # 思考：如果获得提交的数据？
        message = request.POST
        print(message['name'])
        name = message.get('name', None)  # gavin  ''  None  False
        if not name:  # 如果name没有值
            c['name_error'] = "用户名不能为空！"
        email = message.get('email')
        address = message.get('address')
        content = message.get('message')
        print(name, email, address)

        # 思考：如何保存？
        #  - 首先用Message类创建一个对象
        # 方法一：
        msg = Message(name=name, email=email, address=address, content=content)
        # 方法二：
        msg = Message()
        msg.name = name
        msg.email = email
        msg.address = address
        msg.content = content

        #  - 然后，调用对象的保存方法来保存数据
        print(dir(msg))
        msg.save()  # insert  into  ***

        return render(request, template_name='msg2.html', context=c)

    # 把获取到的内容保存到数据库

    # 返回一个Response信息，例如：成功提交！
