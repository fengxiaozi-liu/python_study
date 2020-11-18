from django.db.models import Count
from django.shortcuts import render, HttpResponse
from django.views import View
from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage
from app01 import models
from django.db.models import F, Q
from utils.pager import PageInfo


# Create your views here.
def test(request):
    # =======创建数据(创建完成之后要注释掉)因为不能重复创建==============

    # models.UserType.objects.create(title='普通用户')
    # models.UserType.objects.create(title='vip用户')
    # models.UserType.objects.create(title='svip用户')
    # models.UserInfo.objects.create(name='张三',age=18,ut_id=1)
    # models.UserInfo.objects.create(name='李四',age=20,ut_id=2)
    # models.UserInfo.objects.create(name='王五', age=24, ut_id=1)
    # models.UserInfo.objects.create(name='赵六', age=28, ut_id=3)
    # models.UserInfo.objects.create(name='娜美', age=20, ut_id=1)
    # models.UserInfo.objects.create(name='山治', age=19, ut_id=2)
    # models.UserInfo.objects.create(name='路飞', age=17, ut_id=3)
    # models.UserInfo.objects.create(name='索隆', age=18, ut_id=2)

    # =========获取数据（QuerySet=[obj,obj,ob,]============
    # result = models.UserInfo.objects.all()
    # for every_obj in result:
    #     # 跨表操作只要通过创建的外建就可以书写形式就是 foreignkey.字段名
    #     print(every_obj.name, every_obj.age, every_obj.ut.title)

    # QuerySet对象.values()之后拿到的也是一个对象，但是里面的数据以字典的形式保存
    # result的类型为QuerySet=[{'id':1,'name':'张三'},......]
    # result = models.UserInfo.objects.all().values('id', 'name')
    # for row in result:
    #     print(row)

    # QuerySet对象.values_list()之后拿到的也是一个对象，，但是里面的数据以元组的形式保存
    # result的类型为QuerySet=[(1,'张三'),......]
    # result = models.UserInfo.objects.all().values_list('id', 'name')
    # result = models.UserInfo.objects.filter(id__gt=3).values('id', 'name')
    # for row in result:
    #     print(row)

    # 反向查询,先拿到UserType里面的第一个对象
    # obj = models.UserType.objects.all().first()
    # 用userinfo_set 反向查询 语句 表名小写_set.all()做反向查询
    # for row in obj.userinfo_set.all():
    #     print(row.name, row.age)

    # ORM中的排序语句
    # result = models.UserInfo.objects.all().values('id', 'name').order_by('-id')
    # for row in result:
    #     print(row['id'], row['name'])

    # ORM中的分组语句
    # result = models.UserInfo.objects.filter(id__gt=3).values('ut_id').annotate(x=Count('id')).filter(x__gt=2).order_by(
    #     '-ut_id')
    # # select ut_id,count(id) as x from app01_userinfo where id >3 group by ut_id  having x>2 order by ut_id desc;
    # print(result)

    # ORM中的比较语句
    # models.UserInfo.objects.filter(id__gt=1)
    # models.UserInfo.objects.filter(id__lt=1)
    # models.UserInfo.objects.filter(id__gte=1)
    # models.UserInfo.objects.filter(id__lte=1)
    # models.UserInfo.objects.exclude(id=1)

    # ORM中的包含语句
    # models.UserInfo.objects.filter(ut_id__in=[1, 2, 3])
    # models.UserInfo.objects.filter(ut_id__range=[1, 3])
    # models.UserInfo.objects.filter(name__startwith='xx')
    # models.UserInfo.objects.filter(name__contains='xx')

    # ORM查询的F,Q,extra语句
    # from django.db.models import F
    # F的作用就是在更新的时候获取原来字段的值
    # models.UserInfo.objects.all().update(age=F('age') + 1)
    # # 相当于 update UserInfo set age=age+1

    # condition = {
    #     'id': 1,
    #     'name': '张三'
    # }
    # # filter还支持字典格式的查询
    # result = models.UserInfo.objects.filter(**condition)
    # print(result[0].id, result[0].name)

    # Q是用来解决一些查询的问题的(第一种用法)
    # from django.db.models import Q
    # # Q中一个|管道符表示or条件
    # result = models.UserInfo.objects.filter(Q(id=1) | Q(name='李四'))
    # # Q中&表示and条件
    # result1 = models.UserInfo.objects.filter(Q(id=1) & Q(name='张三'))
    # print(result[0].id, result[0].name, result[1].id, result[1].name)
    # print(result1[0].id, result1[0].name)

    # Q是用来解决一些查询的问题的(第二种用法)
    # q1 = Q()
    # # q1.connector = 'OR'，表示q1内部每一个条件用or
    # # 下面的三行代码表示 id=1 or id=10 or id=9
    # q1.connector = 'OR'
    # q1.children.append(('id', 1))
    # q1.children.append(('id', 10))
    # q1.children.append(('id', 9))
    #
    # # q2.connector = 'OR'，表示q2内部每一个条件用or
    # # 下面的三行代码表示 c1=1 or c1=10 or c1=9
    # q2 = Q()
    # q2.children.append(('c1', 1))
    # q2.children.append(('c1', 10))
    # q2.children.append(('c1', 9))
    #
    # con = Q()
    # # 把q1和q2以and的形式加到了con里面
    # # 表示((id=1)or(id=10)or(id=9))and((c1=1)or(c1=10)or(c1=9))
    # con.add(q1, 'AND')
    # con.add(q2, 'AND')

    # # Q是用来解决一些查询的问题的(第二种用法的简化)
    # condition1 = {
    #     'k1': [1, 2, 3, 4],
    #     'k2': [3, 4, 5],
    #     'k3': [1, 9, 10]
    # }
    # con1 = Q()
    # for key, value in condition1.items():
    #     q3 = Q()
    #     q3.connector = 'OR'
    #     for v_list in value:
    #         q3.children.append(key, v_list)
    #     con1.add(q3, 'AND')
    # models.UserInfo.objects.filter(con1)

    # extra(第一种 select 与 select_params)
    # v = models.UserInfo.objects.all().extra(select={'n': "select count(1) from app01_usertype where id>1"})
    # # 可以采用占位符
    # v1 = models.UserInfo.objects.all().extra(select={'n': "select count(1) from app01_usertype where id>%s and id<%s"},
    #                                          select_params=[1, 3])
    # v2 = models.UserInfo.objects.all().extra(select={'n': "select count(1) from app01_usertype where id>%s and id<%s",
    #                                                  'm': "select count(1) from app01_usertype where id=%s"},
    #                                          select_params=[1, 3, 3])
    # 相当于sql语句中 select *,(select count(1) from usertype) as n from userinfo
    # print(v)
    # for row in v:
    #     print(row.name, row.n)
    # for row in v1:
    #     print(row.name, row.n)
    # for row in v2:
    #     print(row.name, row.m)

    # extra(第二种where与param)
    # v4 = models.UserInfo.objects.extra(
    #     where=["id=1 or id=2", "name='张三' or name='李四'"]
    # )
    # # where里面也是可以用站位符的
    # v5 = models.UserInfo.objects.extra(
    #     where=["id=%s or id=%s", "name='张三' or name='李四'"], params=[1, 2]
    # )
    # # 相当于sql语句中的 select * from userinfo where (id=1 or id=2) and (name='张三' or name='李四')
    # for row in v4:
    #     print(row.id, row.name)
    # for row in v5:
    #     print(row.id, row.name,row.ut_id)
    #

    # extra(order_by)
    # v6 = models.UserInfo.objects.extra(select={'x': 'select count(1) from app01_usertype'}, where=['id>2', 'id<6'],
    #                                    order_by=['-id'])
    # print(v6.query)
    # for row in v6:
    #     print(row.id, row.name, row.ut_id)

    # extra(tables)
    # v7 = models.UserInfo.objects.extra(tables=['app01_usertype'])
    # # 相当于select * from app01_userinfo, app01usertype 默认是笛卡尔积
    # #
    # v8 = models.UserInfo.objects.extra(tables=['app01_usertype'], where=['app01_userinfo.ut_id=app01_usertype.id'])
    # print(v8.query)
    # for row in v8:
    #     print(row.id, row.name)

    # django原生的sql语句
    # from django.db import connections, connection
    # # cursor = connection.cursor() # 相当于cursor = connections['default'].cursor()
    # # Django的setting里面数据库有多个，可以connections(参数) 传递过来参数的变量名，就可以操作指定的数据库
    # cursor = connections['default'].cursor()
    # result = cursor.execute('select * from app01_userinfo')
    # user_list = cursor.fetchall()
    # # 用原生的sql语句拿到的数据是一个元组类型的数据
    # print(user_list)

    # 综合应用，不使用原生的sql语句
    # 第一种方式拿到8<id<=10的人的id和姓名，并倒叙排列
    # result = models.UserInfo.objects.all().values('id', 'name').extra(where=['id<=10', 'id>8'], order_by=['-id'])

    # 第二种方式拿到8<id<=10的人的id和姓名，并倒叙排列
    # result1 = models.UserInfo.objects.filter(Q(id__gt=8) & Q(id__lte=10)).values('id', 'name').order_by('-id')

    # 第三种方式
    # result2 = models.UserInfo.objects.filter(id__gt=8, id__lte=10).values('id', 'name').order_by('-id')

    # for row in result:
    #     print(row['id'], row['name'])
    #
    # for row in result1:
    #     print(row['id'], row['name'])

    # for row in result2:
    #     print(row['id'], row['name'])

    # 简单查询中的distinct关键字,distinct后面不能传递参数
    # result = models.UserInfo.objects.all().values('id').distinct()
    # 相当于sql语句中的 select distinct id from userinfo

    # 简单查询中的reverse，reverse前面有order_by的时候才有用
    # result = models.UserInfo.objects.all().order_by('id').reverse()

    # 简单查询中的only只拿id和name但是还是数据还是以对象的形式保存的
    # result = models.UserInfo.objects.all().only('id', 'name')
    # for row in result:
    #     print(row.id, row.name)

    # 简单查询中的defer(参数），意思是取除了参数里面以外的东西
    # result = models.UserInfo.objects.all().defer('id')
    # for row in result:
    #     print(row.name)

    # 简单查询的using 从指定的数据库里面拿取数据using(参数) using里面的参数是数据库的变量名
    # result = models.UserInfo.objects.all().using('default').values('id','name')
    # for row in result:
    #     print(row['name'], row['id'])

    # 整张表的聚合
    # result = models.UserInfo.objects.all().aggregate(k=Count('ut_id',distinct=True), n=Count('id'))
    # print(result)

    # 另一种创建数据库的方式
    # obj = models.UserType(title='尊贵用户') # 这是创建一条数据
    # obj.save() # 然后执行提交到数据库

    # bulk_create() 做批量增加
    # objs = [
    #     models.UserInfo(name='罗', age=22, ut_id=3),
    #     models.UserInfo(name='艾斯', age=23, ut_id=2),
    # ]
    # # 第一个参数是要创建的对象的列表，第二个参数是一次最多保存多少个对象
    # models.UserInfo.objects.bulk_create(objs, 10)

    # get_or_create() 如果存在就获取，如果不存在就创建
    # obj是如果查询到或者创建出来的一个对象，created是一个布尔类型的值，如果创建了就返回True，查询到了就返回False
    # obj, created = models.UserInfo.objects.get_or_create(name='张四', defaults={'age': 19, 'ut_id': 2})
    # print(obj, created)

    # update_or_create() 如果存在就更新，如果不存在就创建
    # obj, created = models.UserInfo.objects.update_or_create(name='张三', defaults={'age': 56, 'ut_id': 3})
    # print(obj.name, obj.age, created)

    # in_bulk 根据主键进行查询 看主键是否在列表里面
    # result = models.UserInfo.objects.in_bulk([1, 2, 3])
    # print(result)

    # raw(原生的sql语句)
    # models.UserInfo.objects.raw('insert into app01_usertype(title) values(%s)', ['豪横用户', ])
    # for row in result:
    #     print(row.id, row.name)

    # 在做反向查询数据库的时候，因为表1没有表2中的数据，因此必须又要去数据库中再拿取一次数据，所以在做反向查询的时候会出现查询次数增加一次的情况
    # 在做反向查询的时候，会出现多查询一次数据库的情况，有两种方式可以减少查询数据库的次数
    # select_related(外键名) 主动做联表操作 会减少查询的次数但是查询的速度会变慢
    # q = models.UserInfo.objects.all().select_related('ut')
    # for row in q:
    #     print(row.id, row.name, row.ut.title)

    # prefetch_related 不做联表做多次查询，会减少查询的次数，又会增加查询的速度，但是会增加硬盘的容量
    # q = models.UserInfo.objects.all().resolve_expression('ut')
    # 上面的代码进行了三步操作
    # 1. select * from userinfo 从userinfo中拿取所有的数据
    # 2. django内部做了去重，去除没有别关联的用户类型，假设usertype中的id只有[2,4]被使用
    # 3. select * from usertype where id in [2,4] 然后从usertype表中拿取别使用的用户类型的对象
    # for row in q:
    #     print(row.id, row.ut.title)

    # 创建多对多的关系
    # objs = [
    #     models.Love(b_id=1, g_id=1),
    #     models.Love(b_id=1, g_id=4),
    #     models.Love(b_id=2, g_id=2),
    #     models.Love(b_id=2, g_id=3),
    # ]
    # models.Love.objects.bulk_create(objs, 5)

    # 查询和小明有关系的姑娘
    # 第一种方法：用boy表先做反向查询，查询到love表，再做正向查询，查询到girl表

    # 以字典的形式查询
    # result = models.Boy.objects.filter(name='小明').values('love__g__nick')
    # for row in result:
    #     print(row['love__g__nick'])

    # 以对象的形式查询
    # result1 = models.Boy.objects.filter(name='小明').first().love_set.all().select_related('g')
    # for row in result1:
    #     print(row.g.nick)

    # 第二种方法：用love表做正向查询，先从boy表中查询到条件，再从girl表中查询数据

    # 以对象的形式查询
    # result2 = models.Love.objects.filter(b__name='小明')
    # for row in result2:
    #     print(row.g.nick)

    # 以字典的形式查询
    # result3 = models.Love.objects.filter(b__name='小明').values('g__nick')
    # for row in result3:
    #     print(row['g__nick'])

    # 找与品如相关联的男孩
    # 字典的形式查找，通过love正向查找
    # result = models.Love.objects.filter(g__nick='品如').values('b__name')
    # for row in result:
    #     print(row['b__name'])
    # # 以对象的形式查找，通过Girl反向查找
    # result1 = models.Girl.objects.filter(nick='品如').first().love_set.all()
    # for row in result1:
    #     print(row.b.name)

    # obj = models.Boy.objects.filter(name='小明').first()
    # obj.m.add(3)
    # obj.m.add(2, 4)
    # obj.m.add(*[1, ])
    # obj.m.remove(2, 3)
    # obj.m.remove(*[1, 4])
    # obj.m.add(1, 2, 3)
    # set会重置联表中的数据
    # obj.m.set([2, 4])
    # girl_obj = obj.m.all()  # django实现跨表，拿到的是Girl对象
    # obj.m.clear()  # 清空关联所有的数据

    # 做反向查询
    obj = models.Girl.objects.filter(nick='小丽').first()  # 拿到girl的一个对象
    print(obj.boy_set.all())
    return HttpResponse('ok')


# ========================cbv方式处理url与函数之间的对应关系==========================
class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        return HttpResponse('ok')


# ===============================Django实现分页操作=================================

# django自带的分页功能
def index(request):
    """
    Django自带功能分页的实现
    """
    # 获取数据
    current_page = request.GET.get('page')
    user_list = models.UserInfo.objects.all()
    # 创建一个分页对象
    paginator = Paginator(user_list, 3)
    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger as e:
        posts = paginator.page(1)
    except EmptyPage as e:
        posts = paginator.page(1)
    return render(request, 'index.html', {'posts': posts})


# 自己自定义的一个分页的功能，其方法封装成了一个类放在了utils下的pager.py文件中
def customer(request):
    # 按条件获取数据库中的总数据数量
    numbers = models.UserInfo.objects.all().count()
    # 从浏览器上得到当前页
    current_page = request.GET.get('page')
    # 生成一个分页对象
    page_info = PageInfo(current_page, numbers, 2, '/app01/customer.html')
    start = page_info.start()
    end = page_info.end()
    # 根据数据开始和结束的位置，精准定位应该取数据库的第几条到第几条的数据
    user_list = models.UserInfo.objects.all()[start: end]
    return render(request, 'customer.html', {'user_list': user_list, 'page_info': page_info})


# ===========================xss攻击================================
msg = []


def test_xss(request):
    if request.method == 'GET':
        return render(request, 'test_xss.html')
    else:
        content = request.POST.get('content')
        msg.append(content)
        return render(request, 'test_xss.html')


def comment(request):
    return render(request, 'comment.html', {'msg': msg})


def csrf1(request):
    if request.method == 'GET':
        return render(request, 'csrf1.html')
    else:
        value = request.POST.get('user')
        print(value)
        return HttpResponse('ok')
