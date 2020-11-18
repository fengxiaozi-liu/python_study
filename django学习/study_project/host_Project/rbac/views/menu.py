from django.shortcuts import HttpResponse, render, redirect
from rbac import models
from rbac.forms.forms import MenuForm, SecondMenuForm, ThirdMenuForm, MultiAddPermissionForm, MultiUpdatePermissionForm
from rbac.service.urls import memory_reverse
from rbac.service import routes
from rbac.service.menus_permission_dict import menus_permission_dict
from collections import OrderedDict
from django.forms import formset_factory
from django.conf import settings
from django.utils.module_loading import import_string


def menu_list(request):
    """

    :param request:
    :return:
    """
    menu_queryset = models.Menu.objects.all()
    menu_id = request.GET.get('mid')
    menu_exits = models.Menu.objects.filter(id=menu_id).first()
    if not menu_exits:
        menu_id = None
    second_menu_id = request.GET.get('sid')
    second_menu_exits = models.Permission.objects.filter(id=second_menu_id).first()
    if not second_menu_exits:
        second_menu_id = None
    if menu_id:
        second_menu = models.Permission.objects.filter(menu_id=menu_id)
    else:
        second_menu = []
    if second_menu_id:
        third_menus = models.Permission.objects.filter(pid=second_menu_id)
    else:
        third_menus = []
    return render(
        request,
        'menu_list.html',
        {'menus': menu_queryset,
         'menu_id': menu_id,
         'second_menus': second_menu,
         'second_menu_id': second_menu_id,
         'third_menus': third_menus
         }
    )


def menu_add(request):
    """
    一级菜单的增加
    :param request:
    :return:
    """
    # 跳转到这里之前的url
    origin_url = memory_reverse(request, 'rbac:menu_list')
    if request.method == 'GET':
        form = MenuForm()
        return render(request, 'menu_change.html', {'form': form, 'cancel': origin_url})
    form = MenuForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(origin_url)
    return render(request, 'menu_change.html', {'form': form, 'cancel': origin_url})


def menu_edit(request, pk):
    """
    编辑一级菜单
    :param request:
    :param pk:
    :return:
    """
    origin_url = memory_reverse(request, 'rbac:menu_list')
    obj = models.Menu.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = MenuForm(instance=obj)
        return render(request, 'menu_change.html', {'form': form, 'cancel': origin_url})
    form = MenuForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(origin_url)
    return render(request, 'menu_change.html', {'form': form, 'cancel': origin_url})


def menu_del(request, pk):
    """
    删除一级菜单
    :param request:
    :param pk:
    :return:
    """
    origin_url = memory_reverse(request, 'rbac:menu_list')
    if request.method == 'GET':
        return render(request, 'delete.html', {'cancel': origin_url})
    models.Menu.objects.filter(id=pk).delete()
    return redirect(origin_url)


def second_menu_add(request, menu_id):
    """
    添加二级菜单
    :param request:
    :param menu_id:
    :return:
    """
    origin_url = memory_reverse(request, 'rbac:menu_list')
    menu_object = models.Menu.objects.filter(id=menu_id).first()
    if request.method == 'GET':
        form = SecondMenuForm(initial={'menu': menu_object})
        return render(request, 'menu_change.html', {'form': form, 'cancel': origin_url})
    form = SecondMenuForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(origin_url)
    return render(request, 'menu_change.html', {'form': form, 'cancel': origin_url})


def second_menu_edit(request, pk):
    """
    编辑二级菜单
    :param request:
    :param pk:
    :return:
    """
    origin_url = memory_reverse(request, 'rbac:menu_list')
    second_menu_object = models.Permission.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = SecondMenuForm(instance=second_menu_object)
        return render(request, 'menu_change.html', {'form': form, 'cancel': origin_url})
    form = SecondMenuForm(data=request.POST, instance=second_menu_object)
    if form.is_valid():
        form.save()
        return redirect(origin_url)
    return render(request, 'menu_change.html', {'form': form, 'cancel': origin_url})


def second_menu_del(request, pk):
    """
    删除二级菜单
    :param request:
    :param pk:
    :return:
    """
    origin_url = memory_reverse(request, 'rbac:menu_list')
    if request.method == 'GET':
        return render(request, 'delete.html', {'cancel': origin_url})
    models.Permission.objects.filter(id=pk).delete()
    return redirect(origin_url)


def third_menu_add(request, second_menu_id):
    """
    添加三级菜单（权限）
    :param request:
    :param second_menu_id:
    :return:
    """
    origin_url = memory_reverse(request, 'rbac:menu_list')
    if request.method == 'GET':
        # 可以采用选择框的方式，也可以不采用
        # second_obj = models.Permission.objects.filter(id=second_menu_id).first()
        form = ThirdMenuForm()
        return render(request, 'menu_change.html', {'form': form, 'cancel': origin_url})
    form = ThirdMenuForm(data=request.POST)
    if form.is_valid():
        second_menu_obj = models.Permission.objects.filter(id=second_menu_id).first()
        if not second_menu_obj:
            return HttpResponse('二级菜单不存在，请重新选择')
        form.instance.pid = second_menu_obj
        # instance 包含了用户提交的所有值
        # instance = models.Permission('title'='',name='', url='')
        # instance.pid = second_menu_object
        # instance.save()
        form.save()
        return redirect(origin_url)
    return render(request, 'menu_change.html', {'form': form, 'cancel': origin_url})


def third_menu_edit(request, pk):
    """
    编辑三级菜单(权限）
    :param request:
    :param pk: 当前权限的id
    :return:
    """
    origin_url = memory_reverse(request, 'rbac:menu_list')
    third_obj = models.Permission.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = ThirdMenuForm(instance=third_obj)
        return render(request, 'menu_change.html', {'form': form, 'cancel': origin_url})
    form = ThirdMenuForm(data=request.POST, instance=third_obj)
    if form.is_valid():
        form.save()
        return redirect(origin_url)
    return render(request, 'menu_change.html', {'form': form, 'cancel': origin_url})


def third_menu_del(request, pk):
    origin_url = memory_reverse(request, 'rbac:menu_list')
    if request.method == 'GET':
        return render(request, 'delete.html', {'cancel': origin_url})
    models.Permission.objects.filter(id=pk).delete()
    return redirect(origin_url)


def multi_permissions(request):
    """
    批量操作权限
    :param request:
    :return:
    """
    post_type = request.GET.get('type')
    formset_add_class = formset_factory(MultiAddPermissionForm, extra=0)
    formset_update_class = formset_factory(MultiUpdatePermissionForm, extra=0)
    formset_add = None
    if request.method == 'POST' and post_type == 'add':
        formset = formset_add_class(request.POST)
        if formset.is_valid():
            post_row_list = formset.cleaned_data
            flag = True
            permission_list = []
            for i in range(formset.total_form_count()):
                row = post_row_list[i]
                if not row:
                    continue
                try:
                    permission_obj = models.Permission(**row)
                    permission_obj.validate_unique()
                    permission_list.append(permission_obj)
                except Exception as e:
                    formset.errors[0].update(e)
                    flag = False
                    formset_add = formset
            if flag:
                models.Permission.objects.bulk_create(permission_list, batch_size=20)
        else:
            formset_add = formset
    formset_update = None
    if request.method == 'POST' and post_type == 'update':
        formset = formset_update_class(data=request.POST)
        if formset.is_valid():
            post_row_list = formset.cleaned_data
            for i in range(formset.total_form_count()):
                row = post_row_list[i]
                try:
                    permission_id = row.pop('id')
                    permission_obj = models.Permission.objects.filter(id=permission_id).first()
                    for key, value in row.items():
                        setattr(permission_obj, key, value)
                    permission_obj.validate_unique()
                    permission_obj.save()
                except Exception as e:
                    formset.errors[0].update(e)
                    formset_update = formset
        else:
            formset_update = formset

    # 获取项目中所有的url
    route_dict = routes.get_all_url_dict()
    # 获取到项目中所有的url
    route_name_set = set(route_dict.keys())
    # 获取到数据库中所有的url名称
    permissions = models.Permission.objects.all().values('id', 'title', 'url', 'name', 'menu_id', 'pid_id')
    permission_name_set = set()
    permission_dict = OrderedDict()
    for item in permissions:
        permission_name_set.add(item['name'])
        permission_dict[item['name']] = item
    for name, value in permission_dict.items():
        route_row_dict = route_dict.get(name)
        if not route_row_dict:
            continue
        if value['url'] != route_row_dict['url']:
            value['url'] = '和数据库中的值不一致'

    # 计算出应该增加的name
    if not formset_add:
        add_name_list = route_name_set - permission_name_set  # 当数据库中少于自动发现的，在数据库中做增加
        formset_add = formset_add_class(
            initial=[row_dict for name, row_dict in route_dict.items() if name in add_name_list])

    # 计算出来应该删除的name
    del_name_list = permission_name_set - route_name_set  # 当数据库中的多于自动发现的，在数据库中就删除
    del_row_list = [row_dict for name, row_dict in permission_dict.items() if name in del_name_list]

    # 计算出来应该更新的name
    if not formset_update:
        update_name_list = permission_name_set & route_name_set
        formset_update = formset_update_class(
            initial=[row_dict for name, row_dict in permission_dict.items() if name in update_name_list])
    return render(request, 'multi_permissions.html',
                  {'formset_add': formset_add, 'formset_update': formset_update, 'formset_del': del_row_list})


def multi_permissions_del(request, pk):
    """
    批量删除权限
    :param request:
    :param pk:
    :return:
    """
    origin_url = memory_reverse(request, 'rbac:multi_permissions')
    if request.method == 'GET':
        return render(request, 'delete.html', {'cancel': origin_url})
    models.Permission.objects.filter(id=pk).delete()
    return redirect(origin_url)


def distribute_permissions(request):
    """
    权限的分配
    :param request:
    :return:
    """
    user_id = request.GET.get('uid')
    role_id = request.GET.get('rid')
    # 根据传过来的uid获取当前用户
    userinfo = import_string(settings.RBAC_USER_MODEL_CLASS)
    user_obj = models.userinfo.objects.filter(id=user_id).first()
    role_obj = models.Role.objects.filter(id=role_id).first()

    # 根据隐藏的input框来判断要更新数据库中的哪个列表
    type_value = request.POST.get('type')
    if request.method == 'POST' and type_value == 'roles':
        roles_id_list = request.POST.getlist('roles')
        # 用户和角色关系添加到对应的关系表中
        if not user_obj:
            return HttpResponse('请选择用户，然后分配角色')
        user_obj.roles.set(roles_id_list)
    if request.method == 'POST' and type_value == 'permissions':
        permissions_id_list = request.POST.getlist('permissions')
        if not role_obj:
            return HttpResponse('请选择角色，然后选择权限')
        role_obj.permissions.set(permissions_id_list)

    if not role_obj:
        role_id = None

    # 对用户所拥有的角色，以及用户所用户的权限进行显示
    if not user_obj:
        user_id = None
    if user_id:
        # 根据当前用户拿到当前用户所拥有的角色
        user_to_roles = user_obj.roles.all()
    else:
        user_to_roles = []
    if role_obj:
        # 根据当前用户的角色拿到角色相关的所有权限
        roles_to_permissions = role_obj.permissions.all()
        roles_permissions_dict = {item.id: None for item in roles_to_permissions}
    elif user_obj:
        roles_to_permissions = user_obj.roles.filter(permissions__id__isnull=False).values('id',
                                                                                           'permissions').distinct()
        roles_permissions_dict = {item['permissions']: None for item in roles_to_permissions}
    else:
        roles_to_permissions = []
        roles_permissions_dict = {}

    # 将用的id作为key，None作为value，放入到一个字典中，用来做角色粒度的判断
    user_roles_dict = {item.id: None for item in user_to_roles}

    # 用来传递到用户信息列表
    user_list = models.userinfo.objects.all()
    # 用来传递到角色信息列表
    role_list = models.Role.objects.all()
    # 用来传递到权限信息列表,是一个字典类型，三重套娃
    menus_list = menus_permission_dict()

    return render(request, 'distribute_permissions.html',
                  {
                      'user_list': user_list, 'role_list': role_list, 'menus_list': menus_list,
                      'user_id': user_id, 'role_id': role_id,
                      'user_roles_dict': user_roles_dict, 'roles_permissions_dict': roles_permissions_dict
                  })
