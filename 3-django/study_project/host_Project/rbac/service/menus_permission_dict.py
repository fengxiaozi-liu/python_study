from rbac import models


def menus_permission_dict():
    menus_list = models.Menu.objects.all().values('id', 'title')
    menus_dict = {}
    for row in menus_list:
        menus_dict[row['id']] = row
        menus_dict[row['id']]['children'] = []
    second_menus_list = models.Permission.objects.filter(menu_id__isnull=False).values('id', 'title', 'menu_id')
    second_menus_dict = {}
    for row in second_menus_list:
        menu_id = row['menu_id']
        menus_dict[menu_id]['children'].append(row)
        second_menus_dict[row['id']] = row
        second_menus_dict[row['id']]['children'] = []
    third_menus_list = models.Permission.objects.filter(menu_id__isnull=True).values('id', 'title', 'menu_id', 'pid_id')
    for row in third_menus_list:
        pid = row['pid_id']
        if not pid:
            continue
        second_menus_dict[pid]['children'].append(row)
    return menus_list
