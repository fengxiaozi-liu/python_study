from django.shortcuts import redirect, render, HttpResponse
from web import models
from rbac import models
from rbac.service.__init__permission import init_permission
from web.forms import userinfo


def login(request):
    if request == 'GET':
        obj = userinfo.LoginForm()
        return render(request, 'login.html', {'obj': obj})
    form = userinfo.LoginForm(data=request.POST)
    if form.is_valid():
        current_user = models.UserInfo.objects.filter(name=form.cleaned_data['name'],
                                                      password=form.cleaned_data['password']).first()
        if not current_user:
            return render(request, 'login.html', {'msg': '用户名或者密码错误', 'obj': form})
        init_permission(request=request, current_user=current_user)
        return redirect('/customer/list/')
    return render(request, 'login.html', {'obj': form})
