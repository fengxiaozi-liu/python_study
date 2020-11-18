from django.shortcuts import redirect, render, HttpResponse
from app01 import models


def index(request):
    user_info = request.session.get('user_info')
    if not user_info:
        return redirect('/app01/login.html')
    else:
        # 根据男女判断，怎么拿取列表
        gender = user_info.get('gender')
        if gender == '1':
            obj = models.Girl.objects.all()
        else:
            obj = models.Boy.objects.all()
        return render(request, 'index.html', {'user_info': user_info, 'obj': obj})


def others(request):
    gender = request.session.get('user_info').get('gender')
    userid = request.session.get('user_info').get('userid')
    if gender == '1':
        obj = models.BoyToGirl.objects.filter(b_id=userid)
        obj_list = []
        for row in obj:
            temp = (row.g.nickname, row.g.username)
            obj_list.append(temp)
    else:
        obj = models.BoyToGirl.objects.filter(g_id=userid)
        obj_list = []
        for row in obj:
            temp = (row.b.nickname, row.b.username)
            obj_list.append(temp)
    return render(request, 'others.html', {'obj_list': obj_list})