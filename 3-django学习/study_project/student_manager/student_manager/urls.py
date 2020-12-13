"""student_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # ===========学习bootstrap时用到的路径====================
    path('test/', views.test),
    # path('layout/', views.layout),
    # =====================================================新url的地址========================================

    # =======班级url-->对应的函数========
    path('class/', views.classes),
    url('add_class/', views.add_class, name='add_class'),
    path('del_class/', views.del_class),
    path(r'edit_class/', views.edit_class),

    # =======学生url-->对应的函数========
    path('students/', views.students),
    path('add_student/', views.add_student),
    path('del_student/', views.del_student),
    path('edit_student/', views.edit_student),

    # ============老师url--->对应的函数===================
    path('teacher/', views.teacher),
    path('add_teacher/', views.add_teacher),
    path('edit_teacher/', views.edit_teacher),
    path('del_teacher/', views.del_teacher),

    # =======班级模态对话框url-->对应的函数========
    path('modal_add_class/', views.modal_add_class),
    path('modal_edit_class/', views.modal_edit_class),
    path('modal_del_class/', views.modal_del_class),

    # =======学生模态对话框url-->对应的函数========
    path('modal_add_student/', views.modal_add_student),
    path('modal_edit_student/', views.modal_edit_student),
    path('modal_del_student/', views.modal_del_student),

    # ==================================================模态对话框url地址=============================================

    # ========老师模态对话框url-->对应的函数================
    path('modal_add_teacher/', views.modal_add_teacher),
    path('modal_get_add/', views.modal_get_add),
    path('modal_edit_teacher/', views.modal_edit_teacher),
    path('modal_get_edit/', views.modal_get_edit),

    # ==============cookie的学习=================
    # 用cookie设置用户登录
    path('login/', views.login),

]
