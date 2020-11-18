from django.urls import path, re_path
from app01.views import account,manager

urlpatterns = [
    # ====================用户登录相关的url==========================
    path('register/', account.register, name='register'),
    path('login/', account.login, name='login'),
    path('index/', account.index, name='index'),
    path('mother/', account.mother, name='mother'),
    path('edit_self/', account.edit_self, name='edit_self'),
    path('layout/', account.layout, name='layout'),

    # ===================班级管理相关的url===========================
    path('class/', manager.classes, name='class'),
    path('add_class/', manager.add_class, name='add_class'),
    re_path(r'^edit_class/(\d+).html$', manager.edit_class, name='edit_class'),
    re_path(r'^del_class/(\d+).html$', manager.del_class, name='del_class'),

    # =================学生管理相关的url==================================
    path('student/', manager.student, name='student'),
    path('add_student/', manager.add_student, name='add_student'),
    re_path(r'^edit_student/(\d+).html$', manager.edit_student, name='edit_student'),
    re_path(r'^del_student/(\d+).html$', manager.del_student, name='del_student'),

    # ======================教师管理相关的url=====================================
    path('teacher/', manager.teacher, name='teacher'),
    path('add_teacher/', manager.add_teacher, name='add_teacher'),
    re_path(r'^edit_teacher/(\d+).html$', manager.edit_teacher, name='edit_teacher'),
    re_path(r'^del_teacher/(\d+).html$', manager.del_teacher, name='del_teacher'),
]