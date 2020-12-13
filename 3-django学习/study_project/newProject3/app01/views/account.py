from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from app01 import models


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        gender = request.POST.get('gender')
        rmb = request.POST.get('remember')
        if gender == '1':
            obj = models.Boy.objects.filter(username=username, password=passwd).first()
        else:
            obj = models.Girl.objects.filter(username=username, password=passwd).first()
        if obj:
            # request.session['user_id'] = obj.id
            # request.session['user_name'] = obj.username
            # request.session['user_password'] = obj.password
            # request.session['user_password'] = gender
            # request.session['nick_name'] = obj.nickname
            request.session['user_info'] = {
                'userid': obj.id,
                'username': obj.username,
                'userpassword': obj.password,
                'nickname': obj.nickname,
                'gender': gender,
            }
            return redirect('/app01/index.html')
        else:
            return render(request, 'login.html', {'msg': '输入的信息有误'})


def logout(request):
    # 这个删除会把数据库中session表中的用户随机字符串删除
    # request.session.delete(request.session.session_key)
    # 这个删除会把cookie的超时时间设置成0了
    if request.session.get('user_info'):
        request.session.clear()
    return redirect('/app01/login.html')