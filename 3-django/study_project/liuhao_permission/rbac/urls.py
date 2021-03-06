from django.urls import re_path
from rbac.views import role, user, menu

urlpatterns = [
    re_path(r'^role/list/$', role.role_list, name='role_list'),
    re_path(r'^role/add/$', role.role_add, name='role_add'),
    re_path(r'^role/edit/(\d+).html$', role.role_edit, name='role_edit'),
    re_path(r'^role/del/(\d+).html$', role.role_del, name='role_del'),

    re_path(r'^user/list/$', user.user_list, name='user_list'),
    re_path(r'^user/add/$', user.user_add, name='user_add'),
    re_path(r'^user/edit/(\d+).html$', user.user_edit, name='user_edit'),
    re_path(r'^user/del/(\d+).html$', user.user_del, name='user_del'),
    re_path(r'^user/reset_pwd/(\d+).html$', user.user_reset_pwd, name='user_reset_pwd'),

    re_path(r'^menu/list/$', menu.menu_list, name='menu_list'),
    re_path(r'^menu/add/$', menu.menu_add, name='menu_add'),
    re_path(r'^menu/edit/(\d+).html$', menu.menu_edit, name='menu_edit'),
    re_path(r'^menu/del/(\d+).html$', menu.menu_del, name='menu_del'),

    re_path(r'^second/menu/add/(?P<menu_id>\d+)$', menu.second_menu_add, name='second_menu_add'),
    re_path(r'^second/menu/edit/(\d+).html$', menu.second_menu_edit, name='second_menu_edit'),
    re_path(r'^second/menu/del/(\d+).html$', menu.second_menu_del, name='second_menu_del'),

    re_path(r'^third/menu/add/(?P<second_menu_id>\d+)$', menu.third_menu_add, name='third_menu_add'),
    re_path(r'^third/menu/edit/(\d+).html$', menu.third_menu_edit, name='third_menu_edit'),
    re_path(r'^third/menu/del/(\d+).html$', menu.third_menu_del, name='third_menu_del'),

    re_path(r'^multi/permissions/$', menu.multi_permissions, name='multi_permissions'),
    re_path(r'^multi/permissions/del/(\d+)$', menu.multi_permissions_del, name='multi_permissions_del'),


    re_path(r'^distribute/permissions/$', menu.distribute_permissions, name='distribute_permissions'),
]
