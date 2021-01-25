from django.shortcuts import render, HttpResponse, redirect
from django.forms import Form, fields, widgets
from django.core.validators import RegexValidator
import json


# Create your views here.


class LoginForm(Form):
    username = fields.CharField(max_length=8, min_length=2, required=True)
    password = fields.CharField(max_length=12, min_length=6, required=True)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        obj = LoginForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            return redirect('https://www.baidu.com')
        else:
            print(obj.errors)
        return render(request, 'login.html', {'obj': obj})


def ajax_login(request):
    ret = {'status': True, 'msg': None}
    obj = LoginForm(request.POST)
    print(obj)
    if obj.is_valid():
        print(obj.cleaned_data)
    else:
        v = json.dumps(obj.errors)
        print(v)
        ret['status'] = False
        ret['msg'] = obj.errors
    return HttpResponse(json.dumps(ret))


class TestForm(Form):
    t1 = fields.CharField(
        # 下面的六行代码放在一起使用，会自动生成HTML标签
        widget=None,
        label='用户名',
        disabled=False,
        label_suffix=': ',
        validators=[RegexValidator(r'a(\d){2,3}', '5-8位数的字母')],
        required=True,
        max_length=8,
        min_length=2,
        error_messages={
            'max_length': '最大长度不能超过8',
            'min_length': '最小长度不能少于2',
            'required': '不能为空'
        }
    )
    t2 = fields.EmailField()


def test(request):
    if request.method == 'GET':
        obj = TestForm()
        return render(request, 'test.html', {'obj': obj})
    else:
        obj = TestForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
        else:
            print(obj.errors)
        return render(request, 'test.html', {'obj': obj})
