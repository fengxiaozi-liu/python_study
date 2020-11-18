from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from rbac import models
from rbac.forms.forms import UserForm, UpdateUserForm,ResetPwdForm


def user_list(request):
    """
    用户列表
    :param request:
    :return:
    """
    user_queryset = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {'users': user_queryset})


def user_add(request):
    origin_url = reverse('rbac:user_list')
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'user_change.html', {'form': form, 'cancel': origin_url})
    form = UserForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(origin_url)
    return render(request, 'user_change.html', {'form': form, 'cancel': origin_url})


def user_reset_pwd(request, pk):
    """
    重置密码
    :param request:
    :param pk:
    :return:
    """
    origin_url = reverse('rbac:user_list')
    obj = models.UserInfo.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse('用户不存在')
    if request.method == 'GET':
        form = ResetPwdForm()
        return render(request, 'user_change.html', {'form': form, 'cancel': origin_url})
    form = ResetPwdForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(origin_url)
    return render(request, 'user_change.html', {'form': form, 'cancel': origin_url})


def user_edit(request, pk):
    """
    编辑用户
    :param request:
    :param pk:
    :return:
    """
    origin_url = reverse('rbac:user_list')
    obj = models.UserInfo.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse('用户不存在')
    if request.method == 'GET':
        form = UpdateUserForm(instance=obj)
        return render(request, 'user_change.html', {'form': form, 'cancel': origin_url})
    form = UpdateUserForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(origin_url)
    return render(request, 'user_change.html', {'form': form, 'cancel': origin_url})


def user_del(request, pk):
    origin_url = reverse('rbac:user_list')
    if request.method == 'GET':
        return render(request, 'delete.html', {'cancel': origin_url})
    models.UserInfo.objects.filter(id=pk).delete()
    return redirect(origin_url)
