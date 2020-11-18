from django.shortcuts import render, HttpResponse
from django import forms
from django.forms import formset_factory
from app01 import models


class MultiPermissionForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    menu_id = forms.ChoiceField(
        choices=[(None, '------')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    pid_id = forms.ChoiceField(
        choices=[(None, '------')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(MultiPermissionForm, self).__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
        self.fields['pid_id'].choices += models.Permission.objects.filter(pid_id__isnull=True).exclude(
            menu__isnull=True).values_list('id', 'title')


class MultiUpdatePermissionForm(forms.Form):
    id = forms.IntegerField(
        widget=forms.HiddenInput(),
    )
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    menu_id = forms.ChoiceField(
        choices=[(None, '------')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    pid_id = forms.ChoiceField(
        choices=[(None, '------')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(MultiUpdatePermissionForm, self).__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
        self.fields['pid_id'].choices += models.Permission.objects.filter(pid_id__isnull=True).exclude(
            menu__isnull=True).values_list('id', 'title')


def multi_add(request):
    formset_class = formset_factory(MultiPermissionForm, extra=2)
    if request.method == 'GET':
        formset = formset_class()
        return render(request, 'multi_add.html', {'formset': formset})
    formset = formset_class(request.POST)
    if formset.is_valid():
        flag = True
        # 在外部先获取到数据，因为当内部的数据库中不唯一时，会传递一个错误，设置错误之后，在内部就获取不到下一个数据信息了
        post_row_list = formset.cleaned_data
        for i in range(formset.total_form_count()):
            row = post_row_list[i]
            if not row:
                continue
            try:
                obj = models.Permission(**row)
                obj.validate_unique()  # 检查当前对象在数据库中是否存在
                obj.save()
            except Exception as e:
                formset.errors[i].update(e)
                flag = False
        if flag:
            return HttpResponse('提交成功')
        return render(request, 'multi_add.html', {'formset': formset})
    return render(request, 'multi_add.html', {'formset': formset})


def multi_edit(request):
    formset_class = formset_factory(MultiUpdatePermissionForm, extra=0)
    if request.method == 'GET':
        permission_list = models.Permission.objects.all().values('id', 'title', 'name', 'url', 'menu_id', 'pid_id')
        formset = formset_class(initial=permission_list)
        return render(request, 'multi_edit.html', {'formset': formset})
    formset = formset_class(request.POST)
    if formset.is_valid():
        post_row_list = formset.cleaned_data
        flag = True
        for i in range(0, formset.total_form_count()):
            row = post_row_list[i]
            if not row:
                continue
            permission_id = row.pop('id')
            try:
                permission_obj = models.Permission.objects.filter(id=permission_id).first()
                # 通过反射来完成校验
                for key, value in row.items():
                    setattr(permission_obj, key, value)
                permission_obj.validate_unique()
                permission_obj.save()
            except Exception as e:
                formset.errors[i].update(e)
                flag = False
        if flag:
            return HttpResponse('更新成功')
        return render(request, 'multi_edit.html', {'formset': formset})
    return render(request, 'multi_edit.html', {'formset': formset})
