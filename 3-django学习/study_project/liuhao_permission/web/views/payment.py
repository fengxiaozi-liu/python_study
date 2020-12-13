#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect

from web import models
from web.forms.payment import PaymentForm, PaymentUserForm
from rbac.service.pagination import Pagination


def payment_list(request):
    """
    付费列表
    :return:
    """
    numbers = models.Payment.objects.all().count()
    query_params = request.GET.copy()
    query_params._mutable = True
    pager = Pagination(current_page=request.GET.get('page'),
                       all_count=numbers,
                       base_url=request.path_info,
                       query_params=query_params,
                       per_page=3)
    data_list = models.Payment.objects.all()[pager.start:pager.end]
    return render(request, 'payment_list.html', {'data_list': data_list, 'pager': pager})


def payment_add(request):
    """
    编辑付费记录
    :return:
    """
    if request.method == 'GET':
        form = PaymentForm()
        return render(request, 'payment_edit.html', {'form': form})
    form = PaymentForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/payment/list/')
    return render(request, 'payment_edit.html', {'form': form})


def payment_edit(request, pid):
    """
    新增付费记录
    :return:
    """
    obj = models.Payment.objects.get(id=pid)
    if request.method == 'GET':
        form = PaymentForm(instance=obj)
        return render(request, 'payment_add.html', {'form': form})
    form = PaymentForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/payment/list/')
    return render(request, 'payment_add.html', {'form': form})


def payment_del(request, pid):
    """
    删除付费记录
    :param request:
    :param cid:
    :return:
    """
    models.Payment.objects.filter(id=pid).delete()
    return redirect('/payment/list/')

