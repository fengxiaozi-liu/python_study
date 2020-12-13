from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse
from rbac import models
from rbac.forms.forms import RoleForm
from rbac.service.pagination import Pagination


def role_list(request):
    """

    :param request:
    :return:
    """
    numbers = models.Role.objects.all().count()
    query_params = request.GET.copy()
    query_params._mutable = True
    pager = Pagination(current_page=request.GET.get('page'),
                       all_count=numbers,
                       base_url=request.path_info,
                       query_params=query_params,
                       per_page=3)
    role_queryset = models.Role.objects.all()[pager.start:pager.end]
    return render(request, 'role_list.html', {'roles': role_queryset, 'pager': pager})


def role_add(request):
    origin_url = reverse('rbac:role_list')
    if request.method == 'GET':
        form = RoleForm()
        return render(request, 'role_change.html', {'form': form, 'cancel': origin_url})
    form = RoleForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(origin_url)
    return render(request, 'role_change.html', {'form': form, 'cancel': origin_url})


def role_edit(request, pk):
    """

    :param request: 请求相关的信息
    :param pk: 要修改的角色id
    :return:
    """
    origin_url = reverse('rbac:role_list')
    obj = models.Role.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse('角色不存在')
    if request.method == 'GET':
        form = RoleForm(instance=obj)
        return render(request, 'role_change.html', {'form': form, 'cancel': origin_url})
    form = RoleForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(origin_url)
    return render(request, 'role_change.html', {'form': form, 'cancel': origin_url})


def role_del(request, pk):
    """
    删除角色
    :param request: 请求相关的信息
    :param pk: 要删除的id
    :return:
    """
    origin_url = reverse('rbac:role_list')
    if request.method == 'GET':
        return render(request, 'delete.html', {'cancel': origin_url})
    models.Role.objects.filter(id=pk).delete()
    return redirect(origin_url)
