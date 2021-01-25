from django.shortcuts import render, HttpResponse, redirect
from django.forms import Form, fields, widgets
from app01 import models


# ==========================session装饰器================================
def zsq_session(fn):
    def inner(request):
        if request.session.get('user_info'):
            return fn(request)
        else:
            return redirect('/app01/login/')

    return inner


def zsc_session(fn):
    def inner(request, arg):
        if request.session.get('user_info'):
            return fn(request, arg)
        else:
            return redirect('/app01/login/')

    return inner


# ======================================班级管理相关的操作================================
class ClassForm(Form):
    title = fields.RegexField(
        '第\w+',
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        min_length=2,
        max_length=5,
        error_messages={
            'min_length': '班级名称不能少于2位',
            'max_length': '班级名称不能多于5位',
            'required': '班级名称不能为空',
            'invalid': '班级必须以"第"字开头'
        }
    )


@zsq_session
def classes(request):
    class_list = models.Classes.objects.all().values('id', 'title')
    return render(request, 'class.html', {'class_list': class_list})


@zsq_session
def add_class(request):
    if request.method == 'GET':
        obj = ClassForm()
        return render(request, 'add_class.html', {'obj': obj})
    else:
        obj = ClassForm(request.POST)
        if obj.is_valid():
            models.Classes.objects.create(**obj.cleaned_data)
            return redirect('/app01/class/')
        return render(request, 'add_class.html', {'obj': obj})


@zsc_session
def edit_class(request, nid):
    if request.method == 'GET':
        class_list = models.Classes.objects.filter(id=nid).values('id', 'title').first()
        obj = ClassForm(initial=class_list)
        return render(request, 'edit_class.html', {'obj': obj, 'nid': nid})
    else:
        obj = ClassForm(request.POST)
        if obj.is_valid():
            models.Classes.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/app01/class/')
        return render(request, 'edit_class.html', {'obj': obj, 'nid': nid})


@zsc_session
def del_class(request, nid):
    if request.method == 'GET':
        class_list = models.Classes.objects.filter(id=nid).values('id', 'title').first()
        obj = ClassForm(initial=class_list)
        return render(request, 'del_class.html', {'obj': obj, 'nid': nid})
    else:
        obj = ClassForm(request.POST)
        if obj.is_valid():
            models.Classes.objects.filter(id=nid).delete()
            return redirect('/app01/class/')
        return render(request, 'del_class.html', {'obj': obj, 'nid': nid})


# =================================学生管理相关的操作==============================================
class StudentForm(Form):
    student_name = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        min_length=2,
        max_length=8,
        error_messages={
            'min_length': '学生姓名不能少于2位',
            'max_length': '学生姓名不能超过8位',
            'required': '学生姓名不能为空'
        }
    )
    gender = fields.IntegerField(
        widget=widgets.Select(choices=[(1, '男'), (2, '女')], attrs={'class': 'form-control'})
    )
    cls_id = fields.ChoiceField(
        choices=models.Classes.objects.all().values_list('id', 'title'),
        widget=widgets.Select(attrs={'class': 'form-control'})
    )


@zsq_session
def student(request):
    student_list = models.Student.objects.all()
    return render(request, 'student.html', {'student_list': student_list})


@zsq_session
def add_student(request):
    if request.method == 'GET':
        obj = StudentForm()
        return render(request, 'add_student.html', {'obj': obj})
    else:
        obj = StudentForm(request.POST)
        if obj.is_valid():
            models.Student.objects.create(**obj.cleaned_data)
            return redirect('/app01/student/')
        return render(request, 'add_student.html', {'obj': obj})


@zsc_session
def edit_student(request, nid):
    if request.method == 'GET':
        student_list = models.Student.objects.filter(id=nid).values('id', 'student_name', 'gender', 'cls_id').first()
        obj = StudentForm(initial=student_list)
        return render(request, 'edit_student.html', {'obj': obj, 'nid': nid})
    else:
        obj = StudentForm(request.POST)
        if obj.is_valid():
            models.Student.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/app01/student/')
        return render(request, 'edit_student.html', {'obj': obj, 'nid': nid})


@zsc_session
def del_student(request, nid):
    if request.method == 'GET':
        student_list = models.Student.objects.filter(id=nid).values('id', 'student_name', 'gender', 'cls_id').first()
        obj = StudentForm(initial=student_list)
        return render(request, 'del_student.html', {'obj': obj, 'nid': nid})
    else:
        obj = StudentForm(request.POST)
        if obj.is_valid():
            models.Student.objects.filter(id=nid).delete()
            return redirect('/app01/student/')
        return render(request, 'del_student.html', {'obj': obj, 'nid': nid})


# ==================================老师管理相关的页面=======================================================
class TeacherForm(Form):
    teacher_name = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        min_length=2,
        max_length=8,
        error_messages={
            'min_length': '老师姓名不能少于2位',
            'max_length': '老师姓名不能超过8位',
            'required': '老师姓名不能为空',
        }
    )
    teacher__cles = fields.MultipleChoiceField(
        choices=models.Classes.objects.all().values_list('id', 'title'),
        widget=widgets.SelectMultiple(attrs={'class': 'form-control'}),
    )


@zsq_session
def teacher(request):
    teacher_list = models.Teacher.objects.all()
    return render(request, 'teacher.html', {'teacher_list': teacher_list})


@zsq_session
def add_teacher(request):
    if request.method == 'GET':
        obj = TeacherForm()
        return render(request, 'add_teacher.html', {'obj': obj})
    else:
        obj = TeacherForm(request.POST)
        if obj.is_valid():
            models.Teacher.objects.create(teacher_name=obj.cleaned_data['teacher_name'])
            tid = models.Teacher.objects.filter(teacher_name=obj.cleaned_data['teacher_name']).first().id
            for every in obj.cleaned_data['teacher__cles']:
                models.TeacherToClass.objects.create(tch_id=tid, cles_id=every)
            return redirect('/app01/teacher')
        return render(request, 'add_teacher.html', {'obj': obj})


@zsc_session
def edit_teacher(request, nid):
    if request.method == 'GET':
        teacher_list = models.Teacher.objects.filter(id=nid).first()
        class_list = models.Teacher.objects.filter(id=nid).values_list('teacher__cles__id', 'teacher__cles__title')
        class_tuple = []
        for every in class_list:
            temp = every[0]
            class_tuple.append(temp)
        class_tuple = tuple(class_tuple)
        obj = TeacherForm(
            initial={'teacher_name': teacher_list.teacher_name,
                     'teacher__cles': class_tuple})
        return render(request, 'edit_teacher.html', {'obj': obj, 'nid': nid})
    else:
        obj = TeacherForm(request.POST)
        if obj.is_valid():
            models.Teacher.objects.filter(id=nid).update(teacher_name=obj.cleaned_data['teacher_name'])
            models.TeacherToClass.objects.filter(tch_id=nid).delete()
            for every in obj.cleaned_data['teacher__cles']:
                models.TeacherToClass.objects.create(tch_id=nid, cles_id=every)
            return redirect('/app01/teacher/')
        return render(request, 'edit_teacher.html', {'obj': obj, 'nid': nid})


@zsc_session
def del_teacher(request, nid):
    if request.method == 'GET':
        teacher_list = models.Teacher.objects.filter(id=nid).first()
        class_list = models.Teacher.objects.filter(id=nid).values_list('teacher__cles__id', 'teacher__cles__title')
        class_tuple = []
        for every in class_list:
            temp = every[0]
            class_tuple.append(temp)
        class_tuple = tuple(class_tuple)
        obj = TeacherForm(
            initial={'teacher_name': teacher_list.teacher_name,
                     'teacher__cles': class_tuple})
        return render(request, 'del_teacher.html', {'obj': obj, 'nid': nid})
    else:
        obj = TeacherForm(request.POST)
        if obj.is_valid():
            models.Teacher.objects.filter(id=nid).delete()
            models.TeacherToClass.objects.filter(tch_id=nid).delete()
            return redirect('/app01/teacher/')
        return render(request, 'del_teacher.html', {'obj': obj, 'nid': nid})
