from django.conf import settings


# 根据此用户获取到此用户所有的权限并把它放入到session中
def init_permission(request, current_user):
    """
    用户权限的初始化
    :param:current_user:当前用户对象
    :param:request:请求的相关信息
    :return:
    """
    # 根据当前用户获取，用户的权限信息，和菜单信息
    permission_queryset = current_user.roles.filter(permissions__isnull=False).values(
        'permissions__url',
        'permissions__id',
        'permissions__title',
        'permissions__name',
        'permissions__menu_id',
        'permissions__menu__title',
        'permissions__menu__icon',
        'permissions__pid_id',
        'permissions__pid__title',
        'permissions__pid__url',
    ).distinct()
    menu_dict = {}
    permission_dict = {}
    for item in permission_queryset:
        temp = {
            'id': item['permissions__id'],
            'title': item['permissions__title'],
            'url': item['permissions__url'],
            'pid': item['permissions__pid_id'],
            # 找到它父亲的title和url
            'p_title': item['permissions__pid__title'],
            'p_url': item['permissions__pid__url'],
        }
        permission_dict[item['permissions__name']] = temp
        # 判断url权限能不能做菜单
        if not item['permissions__menu_id']:
            continue
        one_dict = {
            'id': item['permissions__id'],
            'title': item['permissions__title'],
            'url': item['permissions__url']
        }
        if item['permissions__menu_id'] in menu_dict:
            menu_dict[item['permissions__menu_id']]['children'].append(one_dict)
        else:
            menu_dict[item['permissions__menu_id']] = {
                'title': item['permissions__menu__title'],
                'icon': item['permissions__menu__icon'],
                'children': [one_dict, ]
            }
    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict
    request.session[settings.MENU_SESSION_KEY] = menu_dict
