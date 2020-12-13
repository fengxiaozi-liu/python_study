from django.shortcuts import render, HttpResponse, redirect
from django.forms import Form, fields
from app01 import models


# Create your views here.


def test(request):
    print('test')
    return HttpResponse('ok')


class LoginForm(Form):
    # 内部采取了正则的验证
    # required=True不能为空，max_length=18,min_length=6长度在6-18之间
    username_chinese_message = {
        'required': '用户名不能为空',
        'max_length': '最大长度不能超过8位',
        'min_length': '最小长度不能低于2位'
    }
    username = fields.CharField(
        # 最大长度
        max_length=8,
        # 最小长度
        min_length=2,
        # 是否可以为空
        required=True,
        # 用户自定义的错误信息的提示
        error_messages=username_chinese_message
    )
    password = fields.CharField(
        min_length=6,
        required=True,
        error_messages=username_chinese_message
    )


class RegisterForm(Form):
    username_chinese_error = {
        'min_length': '用户名长度不能小于2位',
        'max_length': '用户名长度不能大于8位',
        'required': '用户名不能为空',
    }
    password_chinese_error = {
        'min_length': '密码长度不能小于6位',
        'max_length': '密码长度不能大于12位',
        'required': '密码不能为空',
    }
    username = fields.CharField(min_length=2, max_length=8, required=True, error_messages=username_chinese_error)
    password = fields.CharField(min_length=6, max_length=12, required=True, error_messages=password_chinese_error)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 拿到一个由request和LoginForm共同组成的一个对象
        obj = LoginForm(request.POST)
        # obj.is_valid()如果符合正则表达式就返回True，如果不符合就返回False
        if obj.is_valid():
            # 如果不为空就拿取数据,拿到的数据是一个字典类型
            # 用户输入的格式错误
            dict1 = obj.cleaned_data
            obj = models.UserInfo.objects.filter(
                username=dict1.get('username'), password=dict1.get('password')).first()
            if obj:
                return redirect('https://www.baidu.com')
            else:
                return redirect('/login/')
        else:
            # 用户输入的格式正确
            # 拿到所有的错误信息
            dict2 = obj.errors
            return render(request, 'login.html', {'dict2': dict2})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    else:
        obj = RegisterForm(request.POST)
        if obj.is_valid():
            user_list = obj.cleaned_data
            models.UserInfo.objects.create(**user_list)
            return redirect('/login/')
        else:
            errors = obj.errors
            return render(request, 'register.html', {'errors': errors})
