from django.shortcuts import render, HttpResponse, redirect
from app01 import models


# Create your views here.

def test(request):
    # models.UserInfo.objects.create(username='张三', email='qwert')
    # models.UserInfo.objects.filter(id=1).update(ctime='2020-9-20')

    return render(request, 'test.html', {'user': 'xiaoming'})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        user = request.POST.get('user')
        password = request.POST.get('password')
        obj = models.UserList.objects.filter(username=user, passwd=password).first()
        if obj:
            # 1.生成随机字符串
            # 2.通过cookie发送给客户端
            # 3.服务端保存{'随机字符串':{用户信息}}
            request.session['username'] = user
            request.session['passwd'] = password
            return redirect('/app01/index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或者密码错误'})


def index(request):
    # index做判断
    # 1.获取客户端cookie中的随机字符串
    # 2.去session中查找有没有这个随机字符串
    # 3.去session中对应key的value中是否有username
    v = request.session.get('username')
    if v:
        return HttpResponse('登录成功%s' %v)
    else:
        return redirect('/app01/login.html')
