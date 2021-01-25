from django.shortcuts import render, HttpResponse, redirect
from app01 import models


# Create your views here.

def test(request):
    # 能够通过外键直接传对象
    # models.UToU.objects.create(b=boy, g=girl)
    # models.UToU.objects.create(b_id=1, g_id=6)
    # models.UToU.objects.create(b_id=2, g_id=4)
    # models.UToU.objects.create(b_id=1, g_id=4)
    # models.UToU.objects.create(b_id=3, g_id=6)
    # models.UToU.objects.create(b_id=3, g_id=5)
    # obj = models.UToU.objects.filter(b_id=2)
    # for row in obj:
    #     print(row.g.nickname)
    # boy = models.UserInfo.objects.filter(id=3).first()
    # boy_obj = boy.boy.all()
    # for row in boy_obj:
    #     print(row.g.nickname)

    # 查男生信息
    obj = models.UserInfo.objects.filter(id=1).first()
    # 拿到与男生关联信息的对象
    girl = obj.m.all()
    for row in girl:
        print(row.nickname)

    # 查看女生信息
    obj2 = models.UserInfo.objects.filter(id=4).first()
    # 拿到与女生相关联的对象
    boy = obj2.userinfo_set.all()
    for row in boy:
        print(row.nickname)
    return HttpResponse('ok')


def tests(request):
    print('中间件测试')
    return HttpResponse('ok')
