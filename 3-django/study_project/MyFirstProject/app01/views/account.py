from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django.forms import Form, fields, widgets


# Create your views here.
class RegisterForm(Form):
    username = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        min_length=3,
        max_length=9,
        error_messages={
            'required': '用户名不能为空',
            'min_length': '最小长度不能少于3位',
            'max_length': '最大长度不能超过9位'
        }
    )
    password = fields.CharField(
        min_length=8,
        max_length=16,
        widget=widgets.TextInput(attrs={'type': 'password','class':'form-control'}),
        error_messages={
            'min_length': '密码的最小长度是8位',
            'max_length': '密码的最大长度是16位',
            'required': '密码不能为空'
        }
    )


class LoginForm(Form):
    username = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        min_length=3,
        max_length=9,
        error_messages={
            'required': '用户名不能为空',
            'min_length': '最小长度不能少于3位',
            'max_length': '最大长度不能超过9位'
        }
    )
    password = fields.CharField(
        min_length=8,
        max_length=16,
        widget=widgets.TextInput(attrs={'type': 'password', 'class': 'form-control'}),
        error_messages={
            'min_length': '密码的最小长度是8位',
            'max_length': '密码的最大长度是16位',
            'required': '密码不能为空'
        }
    )


def register(request):
    if request.method == 'GET':
        obj = RegisterForm()
        return render(request, 'register.html', {'obj': obj})
    else:
        obj = RegisterForm(request.POST)
        if obj.is_valid():
            models.UserInfo.objects.create(**obj.cleaned_data)
            return redirect('/app01/login/')
        return render(request, 'register.html', {'obj': obj})


def login(request):
    if request.method == 'GET':
        obj = LoginForm()
        return render(request, 'login.html', {'obj': obj})
    else:
        obj = LoginForm(request.POST)
        if obj.is_valid():
            user = models.UserInfo.objects.filter(**obj.cleaned_data).first()
            if user:
                request.session['user_info'] = obj.cleaned_data
                return redirect('/app01/index/')
            else:
                return render(request, 'login.html', {'msg': '用户名或者密码错误，请核对信息', 'obj': obj})
        return render(request, 'login.html', {'obj': obj})


def zsc_session(fn):
    def inner(request):
        if request.session.get('user_info'):
            return fn(request)
        else:
            return redirect('/app01/login/')

    return inner


@zsc_session
def index(request):
    if request.method == 'GET':
        user = request.session.get('user_info').get('username')
        return render(request, 'index.html', {'user': user})


@zsc_session
def mother(request):
    return render(request, 'mother.html')


@zsc_session
def edit_self(request):
    if request.method == 'GET':
        username = request.session.get('user_info').get('username')
        user_list = models.UserInfo.objects.filter(username=username).values('username', 'password').first()
        obj = RegisterForm(initial=user_list)
        return render(request, 'edit_self.html', {'obj': obj})
    else:
        obj = RegisterForm(request.POST)
        username = request.session.get('user_info').get('username')
        if obj.is_valid():
            models.UserInfo.objects.filter(username=username).update(**obj.cleaned_data)
            request.session.delete(request.session.session_key)
            request.session['user_info'] = obj.cleaned_data
            return redirect('/app01/login/')
        return render(request, 'edit_self.html', {'obj': obj})


@zsc_session
def layout(request):
    request.session.clear()
    return redirect('/app01/login')
