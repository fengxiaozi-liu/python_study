from django.shortcuts import render, redirect, HttpResponse
from app import models
from operate_mysql import operate_mysql
from operate_mysql import SqlHelper
import json


# Create your views here.
# ===================================================页面布局的学习=============================================

# ===========================bootstrap的学习==============
# 测试页面的函数，主要是了解bootstrap中的css布局和组件，了解什么是响应式
def test(request):
    return render(request, 'test.html')


# 做学员管理的页面布局，具体学习bootstrap的页面布局
def layout(request):
    return render(request, 'layout.html')


# =================================================cookie的学习===================================================
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = str(request.POST.get('password'))
        obj = SqlHelper.SqlHelper()
        user_passwd_dict = obj.get_one('select passwd from user where username=%s', [username, ])
        user_passwd = user_passwd_dict['passwd']
        if user_passwd == password:
            objc = redirect('/class/')
            # import datetime
            # from datetime import timedelta
            # ct是当前的时间
            # ct = datetime.datetime.now()
            # timedelta是设置时间的可以是小时，秒，分钟或者星期等等
            # v = timedelta(seconds=10)
            # value是当前时间加上一个你设置的时间 也就是多长时间后的一个具体时间
            # value = ct + v
            # 一般推荐的是max_age写法因为他把上面的部分都做了
            # objc.set_cookie('ticket', 'qwert',max_age=10)
            # objc.set_cookie('ticket', 'qwer', expires=value)
            # set_signed_cookie多了一个参数salt相当于md5加密
            objc.set_cookie('ticket', '1234')
            return objc
        else:
            return HttpResponse('用户名或者密码错误')


# ======================================================新url的方式操作表格================================================

# 设置一个装饰器让每一函数都含有cookie
def dec_cookie(fn):
    def inner(request):
        tk = request.COOKIES.get('ticket')
        if not tk:
            return redirect('/login/')
        return fn(request)

    return inner


# =====================================================班级操作============================================
#  查看所有班级信息的函数
@dec_cookie
def classes(request):
    class_list = models.Classes.objects.all()
    return render(request, 'class.html', {'class_list': class_list})


# 添加班级的函数
@dec_cookie
def add_class(request):
    if request.method == 'GET':
        return render(request, 'add_class.html')
    else:
        value = request.POST.get('title')
        if len(value) > 0:
            models.Classes.objects.create(title=value)
            return redirect('/class/')
        else:
            return render(request, 'add_class.html', {'msg': '输入的班级不能为空'})


# 删除班级的函数
@dec_cookie
def del_class(request):
    nid = request.GET.get('nid')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/class/')


# 编辑班级的函数
@dec_cookie
def edit_class(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        result = models.Classes.objects.filter(id=nid)
        return render(request, 'edit_class.html', {'result': result})
    else:
        nid = request.POST.get('id')
        value = request.POST.get('title')
        models.Classes.objects.filter(id=nid).update(title=value)
        return redirect('/class/')


# ====================================================学生操作=====================================
# 查看所有学生信息的函数
@dec_cookie
def students(request):
    """
    学生列表
    :param request: 封装了请求的相关信息
    :return:
    """
    student_list = operate_mysql.get_formation(
        'select student.*,class.title from student inner join class on student.class_id=class.id',
        [])
    class_list = operate_mysql.get_formation('select * from class', [])
    return render(request, 'students.html', {'student_list': student_list, 'class_list': class_list})


# 增加学生信息的函数
@dec_cookie
def add_student(request):
    if request.method == 'GET':
        class_list = operate_mysql.get_formation('select * from class', [])
        return render(request, 'add_student.html', {'class_list': class_list})
    else:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        operate_mysql.modify_formation('insert into student(name, class_id) values(%s,%s)', [name, class_id, ])
        return redirect('/students/')


# 删除学生的函数
@dec_cookie
def del_student(request):
    nid = request.GET.get('nid')
    operate_mysql.modify_formation("delete from student where id=%s", [nid, ])
    return redirect('/students/')


# 编辑学生信息的函数
@dec_cookie
def edit_student(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        student = operate_mysql.get_one("select * from student where id=%s", [nid, ])
        class_list = operate_mysql.get_formation('select * from class', [])
        return render(request, 'edit_student.html', {'student': student, 'class_list': class_list})
    else:
        nid = request.POST.get('id')
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        operate_mysql.modify_formation('update student set name=%s,class_id=%s where id=%s', [name, class_id, nid])
        return redirect('/students/')


# ===============================多对多(老师操作)=========================================
# 查看老师所有的信息的函数
@dec_cookie
def teacher(request):
    teacher_lists = {}
    teacher_list = operate_mysql.get_formation(
        """
        select teacher.id as tid, teacher.name,class.title as class_title
        from teacher left join teacher_class on teacher.id= teacher_class.teacher_id 
        left join class on class.id= teacher_class.class_id;
        """, [])
    for every_dict in teacher_list:
        tid = every_dict['tid']
        if tid in teacher_lists:
            teacher_lists[tid]['class_title'].append(every_dict['class_title'])
        else:
            teacher_lists[every_dict['tid']] = {'tid': every_dict['tid'], 'name': every_dict['name'], 'class_title':
                [every_dict['class_title'], ]}
    return render(request, 'teacher.html', {'teacher_list': teacher_lists.values()})


# 添加教师的函数
@dec_cookie
def add_teacher(request):
    if request.method == 'GET':
        obj = SqlHelper.SqlHelper()
        class_list = obj.get_all('select * from class', [])
        obj.close()
        return render(request, 'add_teacher.html', {'class_list': class_list})
    else:
        name = request.POST.get('name')
        class_ids = request.POST.getlist('class_id')
        obj = SqlHelper.SqlHelper()
        teacher_id = obj.modify_get('insert into teacher(name) values(%s)', [name, ])
        data_list = []
        for cls_id in class_ids:
            temp = (teacher_id, cls_id)
            data_list.append(temp)
        obj.multiple_modify('insert into teacher_class(teacher_id,class_id) values(%s,%s)'
                            , data_list)
        obj.close()
        return redirect('/teacher/')


# 编辑教师的函数
@dec_cookie
def edit_teacher(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = SqlHelper.SqlHelper()
        teacher_list = obj.get_one('select * from teacher where id=%s', [nid, ])
        teacher_class_dict = obj.get_all('select teacher_id,class_id from teacher_class where teacher_id=%s', [nid, ])
        class_list = obj.get_all('select * from class', [])
        teacher_class_list = []
        for every in teacher_class_dict:
            cls_id = every.get('class_id')
            teacher_class_list.append(cls_id)
        return render(request, 'edit_teacher.html',
                      {'teacher_list': teacher_list, 'teacher_class_list': teacher_class_list,
                       'class_list': class_list})
    else:
        nid = request.POST.get('id')
        name = request.POST.get('name')
        class_id = request.POST.getlist('class_id')
        data_list = []
        for cls_id in class_id:
            temp = (nid, cls_id)
            data_list.append(temp)
        obj = SqlHelper.SqlHelper()
        obj.modify('update teacher set name=%s where id=%s', [name, nid])
        # 先把当前老师的对应的关系删掉再添加
        obj.modify('delete from teacher_class where teacher_id=%s', [nid, ])
        obj.multiple_modify('insert into teacher_class(teacher_id,class_id) values(%s,%s)', data_list)
        obj.close()
        return redirect('/teacher/')


# 删除教师的函数
@dec_cookie
def del_teacher(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = SqlHelper.SqlHelper()
        teacher_class_list = obj.get_all(
            """
            select teacher.*,class.title,teacher_class.class_id 
            from teacher left join teacher_class on teacher.id=teacher_class.teacher_id 
            left join class on class.id=teacher_class.class_id where teacher.id=%s;
            """, [nid, ])
        obj.close()
        teacher_id = teacher_class_list[0]['id']
        name = teacher_class_list[0]['name']
        teacher_class = {'id': teacher_id, 'name': name, 'title': None}
        title_list = []
        for every in teacher_class_list:
            temp = every.get('title')
            title_list.append(temp)
        teacher_class['title'] = title_list
        return render(request, 'del_teacher.html', {'teacher_class': teacher_class})
    else:
        nid = request.POST.get('id')
        obj = SqlHelper.SqlHelper()
        obj.modify('delete from teacher where id=%s', [nid, ])
        obj.modify('delete from teacher_class where teacher_id=%s', [nid, ])
        obj.close()
        return redirect('/teacher/')


# ======================================================模态对话框操作表格=================================================


# =========================================模态对话框操作班级=====================================
# 对话框添加班级
def modal_add_class(request):
    title = request.POST.get('title')
    if len(title) > 0:
        operate_mysql.modify_formation('insert into class(title) values(%s)', [title, ])
        # 不管是怎么样都会刷新
        # 刷新的原因：form表单的提交特性
        return HttpResponse('ok')
    else:
        # 目标：页面不刷新，提示错误信息 就不能用form表单提交,用ajax提交数据就能实现
        return HttpResponse('标题不能为空')


# 对话框编辑班级
def modal_edit_class(request):
    ret = {'status': True, 'message': None}
    try:
        nid = request.POST.get('id')
        title = request.POST.get('title')
        operate_mysql.modify_formation('update class set title=%s where id=%s', [title, nid])
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)

    return HttpResponse(json.dumps(ret))


# 对话框删除班级
def modal_del_class(request):
    ret = {'status': True, 'message': None}
    try:
        nid = request.POST.get('id')
        operate_mysql.modify_formation('delete from class where id=%s', [nid, ])
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)

    return HttpResponse(json.dumps(ret))


# =========================================模态对话框操作学生===================================
# 对话框添加学生
def modal_add_student(request):
    ret = {'status': True, 'message': None}
    try:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        operate_mysql.modify_formation('insert into student(name,class_id) values(%s,%s)', [name, class_id])
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))


# 模态对话框编辑学生
def modal_edit_student(request):
    ret = {'status': True, 'message': None}
    try:
        name = request.POST.get('name')
        nid = request.POST.get('id')
        class_id = request.POST.get('class_id')
        operate_mysql.modify_formation('update student set name=%s,class_id=%s where id=%s', [name, class_id, nid])
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))


# 模态对话框删除学生
def modal_del_student(request):
    ret = {'status': True, 'message': None}
    try:
        nid = request.POST.get('id')
        operate_mysql.modify_formation('delete from student where id=%s', [nid, ])
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))


# ========================================模态对话框操作老师表======================================
# 模态对话框添加老师
def modal_add_teacher(request):
    ret = {'status': True, 'message': None}
    try:
        name = request.POST.get('name')
        class_ids = request.POST.getlist('class_id')
        obj = SqlHelper.SqlHelper()
        teacher_id = obj.modify_get('insert into teacher(name) values(%s)', [name, ])
        data_list = []
        for cls_id in class_ids:
            temp = (teacher_id, cls_id)
            data_list.append(temp)
        obj.multiple_modify('insert into teacher_class(teacher_id,class_id) values(%s,%s)', data_list)
        obj.close()
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))


def modal_get_add(request):
    obj = SqlHelper.SqlHelper()
    class_list = obj.get_all('select * from class', [])
    obj.close()
    return HttpResponse(json.dumps(class_list))


def modal_get_edit(request):
    teacher_id = request.GET.get('teacher_id')
    all = []
    select_id_list = []
    obj = SqlHelper.SqlHelper()
    class_list = obj.get_all('select * from class', [])
    select_id_dict = obj.get_all('select class_id from teacher_class where teacher_id=%s', [teacher_id, ])
    obj.close()
    for every in select_id_dict:
        temp = every['class_id']
        select_id_list.append(temp)
    all.append(class_list)
    all.append(select_id_list)
    return HttpResponse(json.dumps(all))


def modal_edit_teacher(request):
    ret = {'status': True, 'message': None}
    try:
        teacher_id = request.POST.get('teacher_id')
        teacher_name = request.POST.get('teacher_name')
        class_list = request.POST.getlist('class_list')
        data_list = []
        for cls_id in class_list:
            temp = (teacher_id, cls_id)
            data_list.append(temp)
        obj = SqlHelper.SqlHelper()
        obj.modify('update teacher set name=%s where id=%s', [teacher_name, teacher_id])
        obj.modify('delete from teacher_class where teacher_id=%s', [teacher_id, ])
        obj.multiple_modify('insert into teacher_class(teacher_id,class_id) values(%s,%s)', data_list)
        obj.close()

    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)

    return HttpResponse(json.dumps(ret))
