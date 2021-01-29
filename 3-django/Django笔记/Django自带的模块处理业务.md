[TOC]

#### 关于app的各个文件

1. admin 
   + Django后台管理相关的配置都放在这个文件下....
   + 可以帮我们做数据库操作
2. app
   + 相关的配置文件
3. model（重点）
   + 里面存放Django的一些类
   + 根据类可以创建数据库表
4. test
   + 做单元测试的
5. views
   + 业务处理放在这个文件下
   + 可以创建一个文件，然后进行分类
     + ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200915213538.png)

#### 路由系统

1. 路由系统的本质

   + url -------> 函数

2. 路由系统的样式

   1. 一 一对应

      + /login/ ----->def login
      + /add-user/(正则表达式)/ ------> def add_user(request)

   2. 函数组合

      1. 第一种(get方式用?nid查找相关的网页)

      + ```python
        http://127.0.0.1:8000/index/?nid=1
        url('/edit',views.edit)
        def edit(request):
            return HttpResponse('ok')
        ```

      + ```jinja2
        {# 采用第一种方式HTML页面的写法 #}
        <a href="/edit/？nid=1"></a>
        ```

      2. 第二种方式（关联正则表达式）-----又叫做动态路由

      + ```python 
        http://127.0.0.1:8000/index/alex/
        re_path(r'/edit/(\w+)',views.edit)
        # 正则表达式里面的值会赋值给args
        def edit(request,args):
            return HttpResponse('ok')
        # 可以给正则表达式命名，找指定的参数
        re_path(r'^edit/(?P<args>\w+/)', views.edit)
        ```

        **注意：**在用正则表达式的时候要统一用法，要么用命名的，要么不命名

      + ```jinja2
        {# 采用第二种方式HTML页面的写法 #}
        <a href="/edit/x"></a>
        {# x是符合正则表达式的值 #}
        ```

      + 用正则表达式的作用

        + 可以增加seo权重，让别人搜索我们网页的时候更加靠前
        + 可以让浏览器中显示url的时候更加美观

   3. 伪静态

      + 定义：

        就是在url中的正则表达式里面加上.html页面

      + 作用

        可以用来增加SEO权重

   4. 路由分发

      + 在主工程内的urls地址中加上每一个app的地址

      + ```python
        from django.contrib import admin
        from django.urls import path, re_path, include
        from app01 import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            # path第一个参数什么都不写就是不指定url，访问默认页面
            path('', views.index),
            # 路由分发用include
            path('app01/', include('app01.urls')),
        ]
        ```

      + 在app内写上指定的url，与其对应的函数即可

      + ```python
        from django.urls import path, re_path
        from app01 import views
        
        urlpatterns = [
            re_path(r'^index.html$', views.index),
            # 每一个参数需要用放在一个括号里面
            re_path(r'^edit/(\w+.html$)/', views.edit),
        ]
        ```

      + **注意：**

        + 当用正则表达式的时候，每一个对应的参数用括号括起来，才能找到对应的参数

        + ```python 
          # 这里是指当不指定url地址时，默认访问的页面
          path('', views.index)
          ```

   5. 给路由系统命名

      + name关键字命名url

        + 作用：

          1. **用于根据名字反生成url**
          2. 可以给正则表达式的地址传递对应的参数

        + 具体用法

          + url中的写法

            ```python
            path('index/',views.index, name=inxde)
            ```

          + views中的写法

            ```python
            from django import reverse
            def index(request,args):
                url_name = reverse('index',args=(1,))
            	return HttpResponse('ok')
            ```

          + 在HTML页面中的写法可以根据url的名字来找指定的地址

            ```jinja2
            {# 无正则表达式(即无参数的写法) #}
            <form action="{% url "index" %}">
            </form>
            {# url中有正则表达式的写法  #}
            <a href="{% url "edit" 变量i %}"</a> {# i就是传递给正则参数的变量值 #}
            ```

          + **注意：**
            + 在用reverse给返回的url传递参数的时候，如果没有给正则表达式里面的内容命名，参数要以元组的形式进行传参
            + 如果给正则表达式中的参数命名了，要以字典的形式进行传参
            + <a href="{% url "edit" i %}"</a> {# i就是接受正则参数的地方 #} 这个问题现在没有解决我传入的时候会出错
            + 上面的问题解决了，其中i是传递给edit的变量，不是edit要传给i的，传递的方向弄错了

#### ORM操作

##### 1. HTTP请求

+ url ------>   视图（模板+数据库）

##### 2.ORM的两大功能

###### 操作表

1. 创建表
2. 修改表
3. 删除表

###### 操作数据行

1. 注意：

   + ORM不能直接操作数据库要利用pymysql等第三方工具连接数据库
   + ORM默认连接 mysql用的是MySQLDB的方式连接
   + django默认连接SQLlite
   + 因此要修改Django的连接方式，让它可以使得ORM可以连接到数据库

2. 修改Django的连接方式，可以用ORM能够访问到

   + Django的默认连接数据库

     ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.sqlite3',
              'NAME': BASE_DIR / 'db.sqlite3',
          }
      }
     ```

   + 修改Django连接数据库的方式第一步

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'python_study',
             'USER': 'liu',
             'PASSWORD': 'lh284259',
             'HOST': '127.0.0.1',
             'PORT': '3306',
         }
     }
     ```

   + 修改默认的连接数据库方式第二步

     在`__init__`文件中写上下面两行代码

     ```python
     import pymysql
     pymysql.install_as_MySQLdb()
     ```

     执行完上面两行代码之后就把SQLlite替换成了MySQLDB

   + 可能会出现的问题

     如果代码出现下面的问题

     ```python
     raise ImproperlyConfigured('mysqlclient 1.4.0 or newer is required; you have %s.' % Database.__version__)
     ```

     就找到当前工程环境下的这个文件

     ```python
     newProject\Lib\site-packages\django\db\backends\mysql\base.py
     ```

     注释掉下面的代码

     ```python
     # if version < (1, 4, 0):
     #     raise ImproperlyConfigured('mysqlclient 1.4.0 or newer is required; you have %s.' % Database.__version__)
     ```

     最后执行

     ```python
     python manage.py makemigrations
     python manage.py migrate
     ```


##### 3. 用ORM操作数据库

###### 1.创建一张表

1. 在model.py里面写上以下代码

   ```python
   class UserInfo(models.Model):
       nid = models.AutoField(primary_key=True)
       username = models.CharField(max_length=32)
       password = models.CharField(max_length=64)
   ```

2. 注册相关的app

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       # 注册app 添加上你的app名称
       'app01',
   ]
   ```

3. 在终端中用命令创建数据表

   ```
   python manage.py makemigrations
   python manage.py mirgate
   ```

4. 创建一对多的关系

   ```python
   class UserGroup(models.Model):
       title = models.CharField(max_length=16)
       
   class UserInfo(models.Model):
       nid = models.AutoField(primary_key=True)
       username = models.CharField(max_length=32)
       # 当给一个表增加一列时可以设置默认值
       age = models.IntegerField(default=18)
       password = models.CharField(max_length=64)
       # 会自动生成 user_group_id将关系对应起来， 一定要加on_delete=models.CASCADE
       user_group = models.ForeignKey('UserGroup', null=True, on_delete=models.CASCADE)
   ```

###### 2.对表的增删改查操作

+ 单表的增加`create()`

  ```python
  # 增加数据用create
  models.UserGroup.objects.create(title='销售部')
  models.UserInfo.objects.create(username='李四', password='456', age=18, user_group_id=1)
  # create的第二种用用法
  obj = models.UserType(title='尊贵用户') # 这是创建一条数据
  obj.save() # 然后执行提交到数据库
  
  ```

+ 单表的查询`all()`或者`filter(条件)`

  ```python
  # 拿到UserGroup的所有数据
  group_list = models.UserGroup.objects.all()
  # group_list是一个QuerySet类型（列表），是一个可迭代的对象
  
  # 拿到指定条件的数据
  # 获取到指定条件的数据
  user_one = models.UserInfo.objects.filter(nid=1)
  # 大于号在过滤器中的应用
  user_a = models.UserInfo.objects.filter(nid__gt=1)
  # 小于号在过滤器中的应用
  user_b = models.UserInfo.objects.filter(nid__lt=1)
  ```

  `filter(条件)`的第二种用法

  ```python
  condition = {
      'id': 1,
      'name': '张三'
  }
  # filter还支持字典格式的查询
  result = models.UserInfo.objects.filter(**condition)
  ```

+ 单表的更改`update()`

  ```python
  # 更新数据
  models.UserGroup.objects.filter(id=2).update(title='公关部')
  ```

+ 单表的删除`delete()`

  ```python
  # 删除指定的数据
  models.UserInfo.objects.filter(nid=2).delete()
  ```

##### 4.联表查询

###### 1.用foreignkey正向查询

+ 使用创建关联表时的foreignkey字段名

+ 具体操作

  ```python
  result = models.UserInfo.objects.all()
  result.ut.title
  ```

###### 2.用表名小_set.all()反向查询

+ 使用被关联的表名的小写+_set+.all()反向的查询

+ 具体操作

  ```python 
  obj = models.UserType.objects.all().first()
  # 用userinfo_set 反向查询 语句 表名小写_set.all()做反向查询
  for row in obj.userinfo_set.all():
  	print(row.name,row.age)
  ```

###### 3.拿到不同类型的数据

1. 拿到QuerySet的**数据以对象**的形式保存

   + models.UserInfo.objects.all()拿取数据以QuerySet=[obj,obj,ob,..]形式保存

     ```python
     # 以QuerySet=[obj,obj,ob,..]形式保存
     result = models.UserInfo.objects.all()
     for every_obj in result:
     	print(every_obj.name, every_obj.age, every_obj.ut.title)
     ```

2. 拿到QuerySet的**数据以字典**的形式保存

   + QuerySet对象.values()之后拿到的也是一个对象，但是里面的数据以字典的形式保存

   + models.UserInfo.objects.all().valuese()拿取数据以QuerySet=[{'id':1,'name':'张三'},......]形式保存

     ```python
     # 以QuerySet=[{'id':1,'name':'张三'},......]形式保存
     result = models.UserInfo.objects.all().values('id', 'name')
     for row in result:
     	print(row)
     ```

3. 拿到QuerySet的**数据以元组**的形式保存

   + QuerySet对象.values_list()之后拿到的也是一个对象，但是里面的数据以元组的形式保存

   + models.UserInfo.objects.all().valuese_list()拿取数据,以QuerySet=[(1,'张三'),......]形式保存

     ```python 
     # 以QuerySet=[(1,'张三'),......] 
     result = models.UserInfo.objects.all().values_list('id', 'name')
     for row in result:
     	print(row)
     ```

4. 以对象的形式实现跨表操作

   + `外键名`.`字段名`实现正向跨表查询

     ```python
     result = models.UserInfo.objects.all()
     result.ut.title
     ```

   + `表名小写_set`.`all()`/`filter()`

     ```python
     obj = models.UserType.objects.all().first()
     # 用userinfo_set 反向查询 语句 表名小写_set.all()做反向查询
     for row in obj.userinfo_set.all():
     	print(row.name,row.age)
     ```

5. 以字典的形式实现跨表操作

   + 外建名加`__ `双下划线实现正向跨表查询

     ```python
     # 使用双下划线在取数据的时候实现跨表操作'ut__title'
     result = models.UserInfo.objects.all().values('id', 'name', 'ut__title')
     for row in result:
     	print(row)
     ```

   + 表名小写加`__`双下划线实现反向跨表查询

     ```python
     # 在values里面用关联的表名的小写+双下划线实现反向查找 'userinfo__name'
     models.UserType.object.values('id','title','userinfo__name')
     ```

6. 以对象形式实现跨表操作和以字典形式实现跨表操作的区别
   1. 对象形式实现跨表操作是在拿取QuerySet对象之后再用`外键名`.`字段名`或者 `表名小写_set`.`all()`/`filter()`来实现跨表
   2. 字典或者是元组形式实现跨表是在拿取数据的时候在vlaues(`外建名__字段名`/`表名小写__字段名`),或者values_list(`外建名__字段名`/`表名小写__字段名`)方法的里面实现跨表操作，得到跨表之后的数据，以字典或者元组的形式保存在QuerySet里面

##### 5.ORM的查询表的其他操作

+ 排序（用order_by关键字）

  ```python
  # 按升序排序
  user_list = models.UserInfo.object.all().oredr_by('id')
  # 上面那个语句相当于sql语句中 select * from UserInfo order by id
  # 按降序排序
  user_list = models.UserInfo.object.all().oredr_by('-id')
  # 上面那个语句相当于 select * from UserInfo order by id desc;
  # 可传递多个排序的方式
  user_list = models.UserInfo.object.all().oredr_by('-id'，name)
  ```

+ 分组（annotate关键字的使用)

  ```python 
  # annotate相当于sql语句中的聚合函数
  models.UserInfo.object.values('ut_id').annotate("聚合函数")
  models.UserInfo.object.values('ut_id').annotate(Count('id'))
  # 上面这个转换成sql语句就是 select ut_id，Count('id') from UserInfo group by ut_id
  models.UserInfo.object.values('ut_id').annotate(abc=Count('id'))
  # 上面那个转换成sql语句为 select ut_id, count('id') as acb from UserInfo group by ut_id
  # abc=Count('id') 相当于给Count('id')起了一个别名
  ```

+ 比较语句（`__gt`,`__lt`,`__gte`,`__lte`,`exclude(id=1)`)

  ```python
  models.UserInfo.objects.filter(id__gt=1) # 大于
  models.UserInfo.objects.filter(id__lt=1) # 小于
  models.UserInfo.objects.filter(id__gte=1) # 大于等于
  models.UserInfo.objects.filter(id__lte=1) #小于等于
  models.UserInfo.objects.exclude(id=1) #不等于
  ```

+ 包含语句（`__in`,`__range`,`__startwith`,`__contains`)

  ```python
  models.UserInfo.objects.filter(ut_id__in=[1, 2, 3]) # 是否在列表里面
  models.UserInfo.objects.filter(ut_id__range=[1, 3]) # 是否在这个范围之内
  models.UserInfo.objects.filter(name__startwith='xx') # 名字是否以xx开头
  models.UserInfo.objects.filter(name__contains='xx') # 名字中是否包含xx
  ```

##### 6.ORM**高级查询**中的**F  Q   和  extra 和 原生sql语句查询   raw方法的使用**

###### 1.F查询

+ 导入F模块

  ```python 
  from django.db.models import F
  ```

+ 作用： F的作用就是在更新的时候获取原来字段的值

  ```python
  # F的作用就是在更新的时候获取原来字段的值
  models.UserInfo.objects.all().update(age=F('age') + 1)
  # 相当于 update UserInfo set age=age+1
  ```

###### 2.Q查询

+ 导入Q模块

  ```python 
  from django.db.models import Q
  ```

+ 作用： Q是用来解决一些查询的问题的，用于构造复杂的查询条件

+ 第一种用法（用生成对象的方式进行查询，可以or 也可以是and）

  ```python
  # Q中一个|管道符表示or条件
  result = models.UserInfo.objects.filter(Q(id=1) | Q(name='李四'))
  # Q中&表示and条件
  result1 = models.UserInfo.objects.filter(Q(id=1) & Q(name='张三'))
  print(result[0].id, result[0].name, result[1].id, result[1].name)
  print(result1[0].id, result1[0].name)
  ```

  注意：Q中一个|管道符表示or条件，Q中&表示and条件

+ 第二种用法（调用方法的方式来查询）

  ```python
  # 生成一个Q对象
  q1 = Q()
  # q1.connector = 'OR'，表示q1内部每一个条件用or
  # 下面的三行代码表示 id=1 or id=10 or id=9
  q1.connector = 'OR'
  q1.children.append(('id', 1))
  q1.children.append(('id', 10))
  q1.children.append(('id', 9))
  
  # q2.connector = 'OR'，表示q2内部每一个条件用or
  # 下面的三行代码表示 c1=1 or c1=10 or c1=9
  q2 = Q()
  q2.children.append(('c1', 1))
  q2.children.append(('c1', 10))
  q2.children.append(('c1', 9))
  
  con = Q()
  # 把q1和q2以and的形式加到了con里面
  # 表示((id=1)or(id=10)or(id=9))and((c1=1)or(c1=10)or(c1=9))
  con.add(q1, 'AND')
  con.add(q2, 'AND')
  ```

+ 注意：

  ​	1. q1.connector = 'OR'，表示q1内部每一个条件用or

  		2. q1.children.append(('id', 1)),用children.append()表示增加一个条件
    		3. con.add(q1, 'AND')，表示把q1对象加到con对象里面去加入的形式是and
                  		4. con.add(q1, 'AND')，con.add(q2, 'AND')的意思是((id=1)or(id=10)or(id=9))and((c1=1)or(c1=10)or(c1=9))

+ Q查询第二种用法的简化，用for循环和字典进行简化

  ```python
  # Q是用来解决一些查询的问题的(第二种用法的简化)
  condition1 = {
  	'k1': [1, 2, 3, 4],
  	'k2': [3, 4, 5],
  	'k3': [1, 9, 10]
  	}
  con1 = Q()
  for key, value in condition1.items():
  	q3 = Q()
  	q3.connector = 'OR'
  	for v_list in value:
  		q3.children.append(key, v_list)
  	con1.add(q3, 'AND')
  models.UserInfo.objects.filter(con1)
  ```

  优点：

  1.  增加了代码的可维护行
  
   	2. 可以做多重循环操作

###### 3.extra查询

+ 不需要导入

+ 额外的条件查询和条件规则

+ `select`与`select_param`

  ```python 
  v = models.UserInfo.objects.all().extra(select={'n': "select count(1) from app01_usertype where id>1"})
  # 可以采用占位符
  v1 = models.UserInfo.objects.all().extra(select={'n': "select count(1) from app01_usertype where id>%s and id<%s"}, select_params=[1, 3])
  v2 = models.UserInfo.objects.all().extra(select={'n': "select count(1) from app01_usertype where id>%s and id<%s", 'm': "select count(1) from app01_usertype where id=%s"},select_params=[1, 3, 3])
  # 相当于sql语句中 select *,(select count(1) from usertype) as n from userinfo
  ```

  注意：select中采用占位符，给它传递参数用select_param

+ `where`与`param`

  ```python 
  # extra(第二种where与param)
  v4 = models.UserInfo.objects.extra(where=["id=1 or id=2", "name='张三' or name='李四'"] )
  # where里面也是可以用站位符的
  v5 = models.UserInfo.objects.extra(where=["id=%s or id=%s", "name='张三' or name='李四'"], params=[1, 2])
  # 相当于sql语句中的 select * from userinfo where (id=1 or id=2) and (name='张三' or name='李四')
  ```

  注意：where里面用占位符，给它传递参数用param

+ order_by

  ```python 
  v6 = models.UserInfo.objects.all().extra(order_by=['-id'])
  v6 = models.UserInfo.objects.filter().extra(order_by=['-id'])
  ```

+ tables

  ```python 
  v7 = models.UserInfo.objects.extra(tables=['app01_usertype'])
  # 相当于select * from app01_userinfo, app01usertype 默认是笛卡尔积
  v8 = models.UserInfo.objects.extra(tables=['app01_usertype'], where=['app01_userinfo.ut_id=app01_usertype.id'])
  # 相当于sql语句中的 select * from app01_userinfor,app01_usertype where app01_userinfo.ut_id=app01_usertype.id
  ```

+ 原生的sql语句写入

  + 导入一个模块可以写sql语句

    ```python
    from django.db import connection,connections
    ```

  + 具体使用

    ```python
    # 创建游标
    cursor = connection.cursor()
    cursor = connections['default'].cursor()
    ```

    补充：cursor = connection.cursor() 相当于cursor = connections['default'].cursor()

    ​			Django的setting里面数据库有多个，可以connections(参数) 传递过来参数的变量名，就可以操作指定的数据库

    ```python
    # 用原生的sql查询数据库
    # cursor = connection.cursor() # 相当于cursor = connections['default'].cursor()
    # Django的setting里面数据库有多个，可以connections(参数) 传递过来参数的变量名，就可以操作指定的数据库
    cursor = connections['default'].cursor()
    result = cursor.execute('select * from app01_userinfo')
    user_list = cursor.fetchall()
    # 用原生的sql语句拿到的数据是一个元组类型的数据
    ```


###### 4.调用`raw()`方法，也可以传递原生的sql语句

+ 不需要导入任何一个模块

+ 具体用法(直接调用raw方法，里面传递sql语句)

  ```python
  # raw(原生的sql语句)
  models.UserInfo.objects.raw('insert into app01_usertype(title) values(%s)', ['豪横用户', ])
  ```

##### 7.ORM查询中一些其他的方法

+ `distinct()`函数

+ 作用：去重

  ```python
  # 简单查询中的distinct关键字,distinct后面不能传递参数
  result = models.UserInfo.objects.all().values('id').distinct()
  # 相当于sql语句中的 select distinct id from userinfo
  ```

+ `reserve()`函数

+ 作用：反转排序方式，且只能在`order_by()`之后使用

  ```python 
  # 简单查询中的reverse，reverse前面有order_by的时候才有用
  result = models.UserInfo.objects.all().order_by('id').reverse()
  ```

+ `only(参数)`函数

+ 作用：取出某个表中特定的几个字段，并且取出的数据仍然是以对象的形式保存在QuerySet对象里面

  ```python
  # 简单查询中的only只拿id和name但是还是数据还是以对象的形式保存的
  result = models.UserInfo.objects.all().only('id', 'name')
  for row in result:
      print(row.id, row.name)
  ```

+ `defer(参数)`函数

+ 作用：是拿出了参数以外的所有字段，并且取出的数据仍然是以对象的形式保存在QuerySet对象里面

  ```python
  # 简单查询中的defer(参数），意思是取除了参数里面以外的东西
  result = models.UserInfo.objects.all().defer('id')
  for row in result:
      print(row.name)
  ```

+ `using(参数)`函数

+ 作用：是从指定的数据库中取数据

  ```python
  # 简单查询的using 从指定的数据库里面拿取数据using(参数) using里面的参数是数据库的变量名
  result = models.UserInfo.objects.all().using('default').values('id','name')
  for row in result:
      print(row['name'], row['id'])
  return HttpResponse('ok')
  ```

+ `bulk_create(参数1，参数2)`函数

+ 作用：可以一次性插入多个数据

+ 参数1：是一个包含插入对象的列表，参数2：是一次性最多想数据库中传递的数据

+ 具体用法

  ```python
  # bulk_create() 做批量增加
  objs = [
      models.UserInfo(name='罗', age=22, ut_id=3),
      models.UserInfo(name='艾斯', age=23, ut_id=2),
  ]
  # 第一个参数是要创建的对象的列表，第二个参数是一次最多保存多少个对象
  models.UserInfo.objects.bulk_create(objs, 10)
  ```

+ `get_or_create(参数1，defaults={})`函数

+ 作用：如果数据存在就获取，如果数据不存在就创建

+ 参数1是查询的条件，参数2defaults是如果不存在这个数据，是要创建的内容

+ 具体用法

  ```python
  # get_or_create() 如果存在就获取，如果不存在就创建
  obj是如果查询到或者创建出来的一个对象，created是一个布尔类型的值，如果创建了就返回True，查询到了就返回False
  obj, created = models.UserInfo.objects.get_or_create(name='张四', defaults={'age': 19, 'ut_id': 2})
  print(obj, created)
  ```

+ `get_or_create(参数1，defaults={})`函数

+ 作用：如果数据存在就更新，如果数据不存在就创建

+ 参数1是查询的条件，参数2defaults是当数据存在时是要更新的内容，如果数据不存在时是要创建的内容

+ 具体用法

  ```python
  # update_or_create() 如果存在就更新，如果不存在就创建
  obj, created = models.UserInfo.objects.update_or_create(name='张三', defaults={'age': 56, 'ut_id': 3})
  print(obj.name, obj.age, created)
  ```

##### 8.做联表查询时减少查询次数和提高查询效率的方法

+ 联表查询中出现的问题

  当我们做联表查询的时候，我们想要做反向查询，但是查询的表1没有被关联表2的数据，因此在做反向查询的时候会自动的向数据库中做一次查询操作，这样就会使得查询的次数增多

+ 解决方法（减少查询次数的方法）

  1. `select_related(外键)` 

     + 作用：主动做联表操作

     + 缺点：主动做联表操作会降低查询的效率

     + 具体操作

       ```python
       q = models.UserInfo.objects.all().select_related('ut')
       for row in q:
           print(row.id, row.name, row.ut.title)
       ```

  2. `prefetch_related(外键)`

     + 作用：不做联表查询，做多次查询

     + 机制：在调用`prefetch_related(外键)`的时候会执行下面三个步骤

       1. select  *  from 表1  从表1中拿取所有的数据
       2.  django内部做了去重，去除没有别关联的用户类型，假设表2中的id只有[2,4]被使用
       3. 那么就会在下一步执行select * from 表2 where id in [2,4] 然后从表2中拿取别使用的用户类型的对象
       4. 最后在把这两张表联系起来

     + 具体操作

       ```python
       q = models.UserInfo.objects.all().resolve_expression('ut')
       for row in q:
           print(row.id, row.ut.title)
       ```

##### 9.多表查询

###### 1.先创建三个表相关联

```python
class Boy(models.Model):
    name = models.CharField(max_length=32)


class Girl(models.Model):
    nick = models.CharField(max_length=32)


class Love(models.Model):
    b = models.ForeignKey('Boy', on_delete=models.CASCADE)
    g = models.ForeignKey('Girl', on_delete=models.CASCADE)
```

###### 2.查询表（查询名字是小明的关联的所有女孩）

```python
# 查询和小明有关系的姑娘
# 第一种方法：用boy表先做反向查询，查询到love表，再做正向查询，查询到girl表

# 以字典的形式查询
result = models.Boy.objects.filter(name='小明').values('love__g__nick')
for row in result:
    print(row['love__g__nick'])

# 以对象的形式查询
result1 = models.Boy.objects.filter(name='小明').first().love_set.all().select_related('g')
for row in result1:
    print(row.g.nick)

# 第二种方法：用love表做正向查询，先从boy表中查询到条件，再从girl表中查询数据

# 以对象的形式查询
result2 = models.Love.objects.filter(b__name='小明')
for row in result2:
    print(row.g.nick)

# 以字典的形式查询
result3 = models.Love.objects.filter(b__name='小明').values('g__nick')
for row in result3:
    print(row['g__nick'])
```

###### 3.关于django内部自动生成关联表的操作

+ django内部自动生成关联表（`ManyToManyFiled()`)

  ```python 
  class Boy(models.Model):
      name = models.CharField(max_length=32)
      m = models.ManyToManyField('Girl')
  
  
  class Girl(models.Model):
      nick = models.CharField(max_length=32)
  ```

+ 在生成的关联表中增加关联信息（`对象名`.`关联外键`.`add(参数)`)

  + 步骤

    1. 先通过外键找到要关联的对象
    2. 再调用add()方法，添加要关联的信息
    3. 补充：add()函数里面，可以是一个数字，也可以是一个（num，num2），还可以是*[数据]

  + 具体操作

    ```python
    obj = models.Boy.objects.filter(name='小明').first()
    obj.m.add(3)
    obj.m.add(2, 4)
    obj.m.add(*[1, ])
    ```

+ 在生成的相关联的表中删除关联信息（`对象名`.`关联外键`.`remove(参数)`)

  + 步骤

    1. 先通过外键找到要关联的对象
    2. 再调用remove()方法，添加要关联的信息
    3. 补充：remove()函数里面，可以是一个数字，也可以是一个（num，num2），还可以是*[数据]

  + 具体操作

    ```python
    obj.m.remove(2, 3)
    obj.m.remove(*[1, 4])
    ```

+ 在生成的相关联表中重置数据（`对象名`.`关联外键`.`set(参数)`）

  + 步骤

    1. 先通过外键找到要关联的对象
    2. 再调用set()方法，添加要关联的信息
    3. 补充：set(参数)方法里面的参数，只能是一个列表

  + 具体操作

    ```python
    obj.m.set([2, 4])
    ```

+ 拿到被关联表的所有信息（`对象名`.`关联外键`.`all()`）

  + 具体操作

    ```python
    girl_obj = obj.m.all()  # django实现跨表，拿到的是Girl对象
    ```

+ 清楚所有的关联信息（`对象名`.`关联外键`.`clear()`)

  + 具体操作

    ```python
    obj.m.clear()  # 清空关联所有的数据
    ```

+ 还可以做反向操作（`表名小写_set`.`all()/add()/remove()/clear()/set()`)

  + 步骤

    1. 先通过`表名小写_set`找到要关联的对象
    2. 然后执行`all()/add()/remove()/clear()/set()`等方法即可

  + 具体操作

    ```python 
    obj = models.Girl.objects.filter(nick='小丽').first()  # 拿到girl的一个对象
    obj.boy_set.add(1)
    obj.boy_set.remove([2,4])
    obj.boy_set.set([1,3])
    ```


###### 4.补充：

1. django内部自动生成的关联表只有三列，id,关联表1id，关联表2id，不能再增加其他的列

2. 通过django内部生成的关联表，因为没有类，就没有对象，只能通过间接操作

3. 也可以将django内部和自己写的表结合起来

   ```python
   class Boy(models.Model):
       name = models.CharField(max_length=32)
       # 创建一个外键，连接Girl，且不生成新的表，就通过Love表去连接,连接的是关联的字段分别是b,g
       m = models.ManyToManyField('Girl', through='Love', through_fields=('b', 'g'))
       # 通过m关联起来之后，可以通过这个外键，进行查询和清空
   
   
   class Girl(models.Model):
       nick = models.CharField(max_length=32)
   
   class Love(models.Model):
       b = models.ForeignKey('Boy', on_delete=models.CASCADE)
       g = models.ForeignKey('Girl', on_delete=models.CASCADE)
       time = models.DateTimeField(null=True)
   ```

##### 10.django中的字段

1. 各种字段

   + 字符串类的字段		

     | django中的字段                        | 含义                 |
     | ------------------------------------- | -------------------- |
     | EmailFiled                            | 一个email地址        |
     | FileFiled()                           | 一个可以上传文件的列 |
     | IPAddressFiled(Field)                 |                      |
     | SlugField(CharField)                  |                      |
     | UUIDField(Field)                      |                      |
     | FilePathField(Field)                  |                      |
     | ImageField(Field)                     |                      |
     | CommaSeparatedIntegerField(CharField) |                      |

     + 补充
       + 自己再python中使用代码可以直接使用
       + 在django中的admin采用了正则表达式，在admin中就有了限制

   + 时间类的字段

     | 字段          | 含义     |
     | ------------- | -------- |
     | DatetimeFiled | 创建时间 |

   + 数字类的字段

     | 字段                                              | 含义                   |
     | ------------------------------------------------- | ---------------------- |
     | IntegerFiled                                      | 创建一个整型类型的字段 |
     | FloatField                                        | 创建一个浮点类型的字段 |
     | DecimalField（max_digits=num1,decimal_places=num2 | 创建一个含有精度的字段 |

   + 枚举类的字段

     django类的枚举有点不同

     ```python
     # 先创建一个列表
     color_list = [
     (1,'黑色'),(2,'白色'),(3,'蓝色')
     ]
     color = models.IntegerFiled(color_list)
     ```

     补充：

     1. 可以自己写自己用
     2. django中的admin使用
     3. 不用外键的应用场景
        + 选项固定不变的时候使用
        + foreignkey选项是动态的

2. 上述字段中可以有参数

   + 一般参数

     | 参数                  | 含义             |
     | --------------------- | ---------------- |
     | null=True             | 内容可以为空     |
     | db_index=True         | 创建索引         |
     | default=x             | 设置默认值       |
     | unique=True           | 创建一个唯一索引 |
     | unique_for_data/month | 创建局部索引     |

   + 联合索引参数

     | 参数            | 含义             |
     | --------------- | ---------------- |
     | index_together  | 创建联合索引     |
     | unique_together | 创建联合唯一索引 |

   + 对admin设置的参数

     | 参数                      | 含义                              |
     | ------------------------- | --------------------------------- |
     | blank=True                | 设置django中的admin可以为空       |
     | verbose_name='用户名'     | 设置admin中的提示文字             |
     | editable=False            | 设置admin是否可以编辑             |
     | help_text=’这是一段提示‘  | 注释信息                          |
     | choice=[0,'小花’，'小明'] | 设置admin中的显示选择框内容       |
     | error_messages            | 自定义admin中的错误信息           |
     | validators                | 自定义admin中错误类型（列表类型） |

##### 11.给反向关联取别名

1. 一般情况下反向关联是`表名小写_set`,可以自定义反向关联的名称

2. 具体操作

   1. 建立一张表，男，女的信息都放在同一张表里

      ```python
      class UserInfo(models.Model):
          nickname = models.CharField(max_length=32)
          username = models.CharField(max_length=32)
          password = models.CharField(max_length=64)
          gender_choice = (
              (1, '男'),
              (2, '女'),
          )
          gender = models.IntegerField(choices=gender_choice)
      ```

   2. 建立一张男女生多对多关系的表，因为是在同一张表里面，这时候应该采用related_name

      ```python 
      class UToU(models.Model):
          # 因为外键在同一张表里面，不能实现反向查找，引入related_query_name来定义反向查找的名字
          # 加上related_query_name之后反向查找就由表名小写_set 变成了 a_set
          # g = models.ForeignKey('UserInfo', related_query_name='a')
          # b = models.ForeignKey('UserInfo', related_query_name='b')
      
          # 用related_name更加简单，反向查找的时候直接写a，related_name定义反向查找的名字
          # 定义了反向查找的名字之后，反向查找就由表名小写_set 变成了 a
          g = models.ForeignKey('UserInfo', related_name='girl', on_delete=models.CASCADE)
          b = models.ForeignKey('UserInfo', related_name='boy', on_delete=models.CASCADE)
      ```

      使用related_query_name ，再反向关联的时候，就是related_query_name自定义的变量名_set完成反向查找

      使用related_name，进行反向关联的时候，直接使用related_name自定义的变量名即可

##### 12自关联

###### ManyToMany自关联

1. 举例说明，将男女生信息放在同一张表里，然后生成一个外键是和自己这张表关联的

   ```python
   class UserInfo(models.Model):
       nickname = models.CharField(max_length=32)
       username = models.CharField(max_length=32)
       password = models.CharField(max_length=64)
       gender_choice = (
           (1, '男'),
           (2, '女'),
       )
       gender = models.IntegerField(choices=gender_choice)
       # 生成一个自关联的外键
       m = models.ManyToManyField('UserInfo')
   ```

2. 拿取对象

   ```python
     obj = models.UserInfo.objects.filter(id=1).first()
       # 拿到与男生关联信息的对象
       girl = obj.m.all()
       for row in girl:
           print(row.nickname)
           
       # 查看女生信息
       obj2 = models.UserInfo.objects.filter(id=4).first()
       # 拿到与女生相关联的对象
       boy = obj2.userinfo_set.all()
       for row in boy:
           print(row.nickname)
   ```

3. 自关联生成的表

   + ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200922155533.png)

###### ForeignKey自关联

1. 是用一个外键将一个表的自增id连接起来

2. 具体操作

   + 创建一张表可以关联自己的自增id

     ```python
     class Comment(models.Model):
         """
         评论表
         """
         news_id = models.IntegerField()  # 新闻id
         content = models.CharField(max_length=32)  # 评论的内容
         user = models.CharField(max_length=32)  # 评论者
         reply = models.ForeignKey('Comment', null=True, blank=True, on_delete=models.CASCADE)
     ```

   + foreignkey自关联生成的表

     ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200922172343.png)

     

#### Django提供的分页

##### 1.分批获取数据

+ 语法

  ```python 
  models.UserInfo.object.all()[statr:end]
  ```

##### 2.通过Django自带的功能实现分页

+ 导入Django.core.pagitnator

  ```python
  from django.core.paginator import Paginator, Page
  ```

+ paginator下面的几个方法

  + | paginator下面的几个函数 | 解释               |
    | ----------------------- | ------------------ |
    | per_page                | 每页显示的条目数量 |
    | count                   | 数据的总个数       |
    | num_pages               | 总页数             |
    | page_range              | 总页数的索引范围   |
    | page                    | page对象           |

  + 具体用法（在python代码中应用）

    ```python
    current_page = request.GET.get('page')
    user_list = models.UserInfo.objects.all()
    # 创建一个分页对象
    paginator = Paginator(user_list, 1)
    posts = paginator.page(current_page)
    return render(request, 'index.html', {'posts': posts})
    ```

+ posts = paginator.page(current_page)（其中posts也封装了许多值）

  + | posts对象下面封装的函数 | 解释               |
    | ----------------------- | ------------------ |
    | has_next                | 是由有下一页       |
    | next_page_number        | 下一页页码         |
    | has_previous            | 是否有上一页       |
    | previous_page_number    | 上一页页码         |
    | object_list             | 分页之后的数据列表 |
    | number                  | 当前页             |
    | paginator               | paginator对象      |

  + posts函数的具体用法（在HTML的页面当中）

    ```django
    <body>
        <h1>用户列表</h1>
        <ul>
            {% for user in posts.object_list %}
                <li>{{ user.name }},{{ user.age }}</li>
            {% endfor %}
        </ul>
        <div>
            {% if posts.has_previous %}
            <a href="/app01/index.html/?page={{ posts.previous_page_number }}">上一页</a>
            {% endif %}
            {% for number in posts.paginator.page_range %}
                <a href="/app01/index.html?page={{ number }}">{{ number }}</a>
            {% endfor %}
            {% if posts.has_next %}
            <a href="/app01/index.html?page={{ posts.next_page_number }}">下一页</a>
            {% endif %}
        </div>
    </body>
    ```

  + 注意：

    + Django只适合做上一页和下一页，因为他会把所有的当前页都列出来，不能够分开显示
    + 而且Django自带的分页只能在Django里面应用，其他的不能显示

##### 3.自定义分页

+ 在取数据的时候采用按照一定的数量显示，然后再呈现在HTML的页面当中

  + 定义一个分页的类，每次需要分页的时候直接调用这个方法

    ```python
    # 一个分页的类
    class PageInfo:
        """
        这是一个自定义的分页系统的类,里面含有有关分页的方法
        参数
            self.current.page: 当前页
            numbers：表示总数据个数
            per_page：表示每页显示多少条数据
            base_url:表示的是要跳转的url地址
            show_page_number：表示一个页面最多显示多少个标签（ 1 2 3 4 5）
        函数：
            def start：表示当前页应该从数据库中的第几个数据开始
            def end：表示当前页应该在第几个数据结束
            def pager：处理下面的数字标签，在一个页面中应该显示多少个数字标签，显示标签的样式，等等
        """
        def __init__(self, current_page, numbers, per_page, base_url, show_page_number=5):
            self.current_page = current_page
            try:
                self.current_page = int(self.current_page)
            except TypeError as e:
                self.current_page = 1
            self.per_page = per_page
            a, b = divmod(numbers, per_page)
            if b:
                a += 1
            self.page_numbers = a
            self.show_page_number = show_page_number
            self.base_url = base_url
    
        def start(self):
            """
            当前页应该从数据库的哪个数据开始
            """
            start_data = (self.current_page - 1) * self.per_page
            return start_data
    
        def end(self):
            """
            当前页应在数据库的哪个数据结束
            """
            end_data = self.current_page * self.per_page
            return end_data
    
        def pager(self):
            """
            对页面的数字标签进行处理
            """
            page_list = []
            half = ((self.show_page_number - 1) / 2)
            half = int(half)
            if self.page_numbers < self.show_page_number:
                begin_page = 1
                stop_page = self.page_numbers + 1
            # 如果总页数大于5
            else:
                # 如果当前页数<=3,就让它显示1-5页
                if self.current_page <= half:
                    begin_page = 1
                    stop_page = self.show_page_number + 1
                # 如果当前页>3，就让他显示前面两个和后面两个
                else:
                    if (self.current_page + half) < self.page_numbers:
                        begin_page = self.current_page - half
                        stop_page = self.current_page + half + 1
                    else:
                        begin_page = self.page_numbers - self.show_page_number + 1
                        stop_page = self.page_numbers + 1
            if self.current_page <= 1:
                prev_page = '<li><a href="">上一页</a></li>'
            else:
                prev_page = '<li><a href="%s?page=%s">上一页</a></li>' % (self.base_url, self.current_page - 1)
    
            page_list.append(prev_page)
            for i in range(begin_page, stop_page):
                if i == self.current_page:
                    temp = '<li class="active"><a href="%s?page=%s">%s</a></li>' % (self.base_url, i, i)
                else:
                    temp = '<li><a href="%s?page=%s">%s</a></li>' % (self.base_url, i, i)
                page_list.append(temp)
            if self.current_page >= self.page_numbers:
                next_page = '<li><a href="">下一页</a></li>'
            else:
                next_page = '<li><a href="%s?page=%s">下一页</a></li>' % (self.base_url, self.current_page + 1)
            page_list.append(next_page)
            return ''.join(page_list)
    ```

  + 然后python中调用自己写的分页方法

    ```python
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
    ```

  + 在HTML页面中操作

    ```django
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <link rel="stylesheet" href="/static/plugins/bootstrap-3.3.7-dist/css/bootstrap.css">
    </head>
    <body>
        <h1>用户列表</h1>
        <ul>
            {% for user in user_list %}
                <li>姓名：{{ user.name }}  年龄：{{ user.age }}</li>
            {% endfor %}
        </ul>
        <nav aria-label="Page navigation">
            <ul class="pagination">
                {{ page_info.pager|safe }}
            </ul>
        </nav>
    </body>
    </html>
    ```

#### xss攻击

定义：

​	别人写的评论是一段js代码，然后如果不进行处理就会放到页面中去，这样别会影响到原来的代码结构可能会造成隐私的泄露

​	防范措施：

​	前端慎用safe 和后端慎用make_safe

#### csrf（跨站请求的伪造）

##### 1.在fbv中的使用

1.基本使用

+ 在form表单中添加`{%  csrf_token  %}`

1. 全站禁用

   + 在setting.py 文件中注释掉下面这行代码

     ```python
     # 用来验证csrf，会生成随机的字符串
     # 'django.middleware.csrf.CsrfViewMiddleware',
     ```

2. 局部禁用

   + 在setting.py 文件中 写入下面这行代码

     ```python
     # 用来验证csrf，会生成随机的字符串
     'django.middleware.csrf.CsrfViewMiddleware',
     ```

   + 然后再你想要禁用的函数上方导入一个模块并加上一个装饰器

     ```python 
     from django.views.decorators.csrf import csrf_exempt
     
     
     @csrf_exempt
     def csrf1(request):
         if request.method == 'GET':
             return render(request, 'csrf1.html')
         else:
             value = request.POST.get('user')
             print(value)
             return HttpResponse('ok')
     
     
     ```

3. 局部使用

   + 在setting.py 文件中注释掉下面这行代码

     ```python
     # 'django.middleware.csrf.CsrfViewMiddleware',
     ```

   + 在views.py 中在你想要使用csrf的地方导入一个模块，加上装饰器就ok

     ```python
     from django.views.decorators.csrf import csrf_protect
     
     
     @csrf_protect
     def csrf1(request):
         if request.method == 'GET':
             return render(request, 'csrf1.html')
         else:
             value = request.POST.get('user')
             print(value)
             return HttpResponse('ok')
     ```

##### 2.在cbv的使用

1. 给类中指定的方法添加一个装饰器，来指定是否启动csrf

   ```python
   from django.views import View
   from django.views.decorators.csrf import csrf_exempt
   from django.utils.decorators import method_decorator
   
   @method_decorator(@csrf_exempt, name='get')
   class Foo(View):
   	def get(self,request):
   		pass
   	def post(self,request):
   		pass
   ```

2. 给类中所有的方法添加一个装饰器，来指定是否启动csrf

   ```python 
   @method_decorator(@csrf_exempt, name='dispatch')
   class Foo(View):
   	def get(self,request):
   		pass
   	def post(self,request):
   		pass
   ```

##### 3.ajax在提交数据的时候，携带csrf的两种方式

###### 1.第一种（放在data中传递给数据）

```django
<body>
<form method="post" action="/app01/csrf1.html">
    {% csrf_token %}
    <input id="user" type="text" name="user">
    <input type="submit" value="提交">
    <a onclick="ShowForm()">提交</a>
</form>
<script src="/static/jquery-1.12.4.min.js"></script>
<script>
    function ShowForm(){
        var csrf_value = $('input[name="csrfmiddlewaretoken"]').val()
        var user_value = $('#user').val()
        $.ajax({
            url:'/app01/csrf1.html',
            type:'POST',
            data:{'user':user_value, 'csrfmiddlewaretoken': csrf_value},
            success:function (arg){
                console.log(arg);
            }
        })
    }
</script>
</body>
```

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200920162000.png)

###### 2.第二种方式（放在请求头里面）

```django
<form method="post" action="/app01/csrf1.html">
    {% csrf_token %}
    <input id="user" type="text" name="user">
    <input type="submit" value="提交">
    <a onclick="ShowForm()">提交</a>
</form>
<script src="/static/jquery-1.12.4.min.js"></script>
<script src="/static/jquery.cookie.js"></script>
<script>
 
    function ShowForm(){
        var csrf_value = $.cookie('csrftoken')
        var user_value = $('#user').val()
        $.ajax({
            url:'/app01/csrf1.html',
            type:'POST',
            headers:{'X-CSRFToken':csrf_value},
            data:{'user':user_value},
            success:function (arg){
                console.log(arg);
            }
        })
    }
</script>
</body>
```

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200920172512.png)

#### 模板

##### 1.母版

##### 2.公共的小组件

1. 在HTML页面中用`include`关键字

2. 具体使用

   + 先写一个HTML页面作为组件

     ```django
     <div>
         <h3>漂亮的组件</h3>
         <div class="title">标题：</div>
         <div class="content">内容：</div>
     </div>
     ```

   + 再用include关键字引入这个组件

     ```django
     <body>
     
     {% include 'pub.html' %}
     {% include 'pub.html' %}
     {% include 'pub.html' %}
     
     </body>
     ```

##### 3..函数 --> 会自动执行

##### 4..在模板里面自定义函数

###### 步骤

1. 在app里面创建一个templatetags模块

2. 在templatetags模块里面创建一个任意的py文件

3. 在py文件中执行以下操作

   ```python 
   # 导入一个模块
   from django import template
   
   # register这个变量名不能改变
   register = template.Labiray()
   
   # 装饰你自定义的函数
   @register.filter/@register.simple_tag
   def my_upper(value):
   	return value.upper
   ```

4. 在HTML文件中导入你自定义的模块

   ```django
   {% load 文件名 %}
   ```

5. 在django工程中**一定要注册**app变量名

###### 补充

1. filter装饰器

   1. 在views中的应用

      + ```python
        @register.filter
        def my_upper(value):
        	return value.upper
        ```

   2. 在HTML页面中传递参数的形式如下

      + ```django
        {{arg1|函数名:"arg2"}}
        ```

   2. 传递参数的形式是，第一个参数放在函数的前面，第二个参数放在函数的后面，是函数名:"arg2",并且：与""之间不能有空格
   3. filter 最多可以传递两个参数
   4. filter可以放在if条件判断的后面

2. simple_tag装饰器

   1. 在views中的使用

      + ```python 
        @register.simple_tag
        def my_lower(value):
        	return value.lower()
        
        @register.simple_tag
        def my_first(value,a1,a2,a3)
        	return value+a1+a2+a3
        ```

   2. 在HTML页面中的使用

      + ```django 
        {% 函数名 "arg" %}
        
        {% 函数名 "arg1" "arg2" "arg3" %}
        ```

   3. simple_tag对参数无限制

   4. 不能做条件判断

#### session

##### cookie是什么：

+ 保存在客户端浏览器上的键值对

##### session是什么

###### 定义

+ 保存在服务端的数据（本质是键值对）

###### 应用

+ session的应用依赖cookie

###### 作用

+ 是保持会话（web网站）

###### 使用原理

1. 用户来访问，生成一个随机的字符串，传递给cookie作为唯一标识
2. 在复制一份随机字符串，保存在session里面，里面存放着用户的信息
3. 这样别人就不能够获取到用户的信息，因为cookie只是随机字符串，拿不到用户的相关信息
4. ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200921120952.png)

###### 优点：

1. 不会把敏感信息显示出来

###### 具体操作

+ 在views中的代码书写

  ```python
  def login(request):
      if request.method == 'GET':
          return render(request, 'login.html')
  
      else:
          user = request.POST.get('user')
          password = request.POST.get('password')
          if user == 'alex' and password == '123':
              # 1.生成随机字符串
              # 2.通过cookie发送给客户端
              # 3.服务端保存{'随机字符串':{用户信息}}
              request.session['username'] = 'alex' # 这一段代码就完成了上面三步的操作
              request.session['email'] = 'xxxx@qq.com'
              return redirect('/app01/index.html')
          else:
              return render(request, 'login.html', {'msg': '用户名或者密码错误'})
  ```

  ```python
  def index(request):
      # index做判断
      # 1.获取客户端cookie中的随机字符串
      # 2.去session中查找有没有这个随机字符串
      # 3.去session中对应key的value中是否有username
      v = request.session.get('username')
      if v:
          return HttpResponse('登录成功%s' %v)
      else:
          return redirect('/app01/login.html')
  ```

+ 在HTML页面中的操作

  ```django
  <body>
  <form method="post" action="/app01/login.html">
      {% csrf_token %}
      <input type="text" name="user">
      <input type="text" name="password">
      <input type="submit" value="提交">{{ msg }}
  </form>
  </body>
  ```

###### session中的几个方法

1. 获取，设置，删除session的值	
   + | session方法                           | 含义                                      |
     | ------------------------------------- | ----------------------------------------- |
     | request.session[key]                  | 从session中取值                           |
     | request.session.get(key,none)         | 从session中取值，有就取出，没有就显示None |
     | request.session[key] = value          | 给session设置值                           |
     | request.session.setdefault(key,value) | 给session设置值，存在此键值对就不设置     |
     | del request.session[key]              | 删除session中的一个键值对                 |

2. 所有的键，值，对

   + | session方法                  | 含义                                       |
     | ---------------------------- | ------------------------------------------ |
     | request.session.keys()       | 获取session中所有的key                     |
     | request.session.values()     | 获取session中所有的values                  |
     | request.session.items()      | 获取session中所有的items                   |
     | request.session.iterkeys()   | 用迭代器的方式一个一个获取session中的key   |
     | request.session.itervalues() | 用迭代器的方式一个一个获取session中的value |
     | request.session.iteritems()  | 用迭代器的方式一个一个获取session中的items |

3. 其他方法

   + | session方法                              | 含义                                                         |
     | ---------------------------------------- | :----------------------------------------------------------- |
     | request.session.seesion_key              | 从session表中获取用户的随机字符串                            |
     | request.session.clear_expired()          | 将所有session失效日期小于当前时期的数据删除                  |
     | request.session.exists(用户的随机字符串) | 检查用户session的随机字符串是否在用户中存在                  |
     | request.session.set_expiry(value)        | 如果value是个整数，session会在value秒之后失效<br />如果value是datetime或者timedelta，namesession就会在这个时间失效<br />如果value是0，用户关闭浏览器session就会失效<br />如果value是None，session会依赖全局session失效策略 |
     | request.session.delete(用户随机字符串)   | 删除当前用户所用的session数据                                |

###### session的配置

1. 如果在setting.py中没有写入下面的代码就默认是，我们下面没有改动过的

+ ```python
  STATIC_URL = '/static/'
  SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # 将session中的信息默认放置在数据库
  SESSION_COOKIE_NAME = 'sessionid'  # 控制浏览器cookie中session叫什么名字
  SESSION_COOKIE_PATH = '/'  		   # path=/ 表示在页面的所有的url上都生效
  SESSION_COOKIE_DOMAIN = None 	   # 设置域名，默认是用的当前的域名
  SESSION_COOKIE_SECURE = False      # 是否HTTPS传输cookie
  SESSION_COOKIE_HTTPONLY = True     # 是否只能通过http传输cookie中的session
  SESSION_COOKIE_AGE = 1209600
  SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器的时候让session过期
  SESSION_SAVE_EVERY_REQUEST = False       # 是否每次请求都保存session，默认修改之后才保存
  ```

###### session的放置位置

+ 数据库（默认放置）

  ```python
  SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # 将session中的信息默认放置在数据库
  ```

+ 缓存

  ```python
  SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎设置放在缓存里面，缓存是另一个服务器里面
  SESSION_CACHE_ALIAS = 'default'    # 使用缓存的别名（默认内存缓存，也可以设置）
  # 缓存在使用的时候要配合django的缓存配置
  ```

+ 文件

  ```python
  SESSION_ENGINE = 'django.contrib.sessions.backends.file'  # 引擎设置放在文件中
  SESSION_FILE_PATH = None  # 缓存文件的路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()
  ```

+ 缓存+数据库（一般情况下不会使用）

  ```python
  SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db' # 引擎设置为缓存加数据库
  ```

+ 加密cookie（就相当于设置cookie中的加密，也不采用）

  ```python 
  SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookie'  # 就相当于设置cookie中的加密，也不采用
  ```

###### 伪造点赞请求

+ ```python
  import requests
  requests.post(
  	url='url地址',
  	cookies={'key':'value字符串'},
  )
  ```


#### 中间件

##### 定义

+ 中间件是放在用户请求和url地址之间的类，在请求传递给url的时候会经历中间件

##### 一次完整的http请求

+ ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200922212001.png)

##### 中间件的工作原理

+ ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200922212344.png)

##### 中间件的几个方法和执行流程

+ 五大方法

  | 中间件方法             | 作用                                                         | 当有返回值值时方法的执行流程                                 |
  | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | progress_request       | 当一个请求发来的时候会首先执行每一个中间件的request方法      | 当有返回值时就不会就再执行下一个中间件的request方法，而是执行当前中间件的response方法，再依次向上执行，返回给客户端 |
  | progress_response      | 当请求到达视图函数时，会将视图函数的返回值在按倒叙返回给每一个中间件，最后返回给浏览器客户端 | 必须要有一个返回值，因为response方法，在返回数据的时候要经历每一个中间件，每一个中间件都需要response方法 |
  | progress_view          | 在每一个中间件的request请求结束之后，不先执行中间件的response方法，而是再跳到第一个中间件的view方法，一次执行每一个中间件的view方法，拿到指定的视图函数 | 当有返回值的时候，就会直接跳转到最后的中间件，执行他的response方法，依次向上传递，最会把view返回值传递给用户 |
  | progress_exception     | 只有当出现错误时，中间件的exception方法才会执行              | 直接跳转到最后的response，最后把返回值值呈现给用户           |
  | progress_template_view | 只有当视图函数里面含有render方法时，才会执行这个方法         |                                                              |

+ progress_view里面参数的介绍

  + callback：接收的是一个视图函数
  + callback_args:接收的是视图函数里面的参数
  + callback_kwargs：也是视图函数里面的参数

+ progress_template_response的介绍

  + 只有视图函数里面有render方法progress_template_view方法才会执行

##### 中间件的应用

1. 应用场景
   + 适用于对所有请求或者一部分请求做处理的时候，使用中间件

#### Form验证

##### 作用

+ 对用户提交的数据进行验证
+ 生成HTML标签
+ 保留上次输入内容

##### 不使用Form验证的时候出现的问题

1. 无法记住上次提交内容，刷新页面数据消失
2. 重复进行用户数据校检：正则，长度，是否为空等

##### django提供的Form组件

1. 先定义规则

   + ```python 
     # 导入Form，fields模块
     from django.forms import Form,fields
     # 定义一个继承Form的类
     class xxx(Form):
     	xx = fields(required=True,....)
     	.......
     ```

2. 使用Form组件

   + ```python 
     # 从页面得到数据
     request.POST
     # 把得到的数据放在写好的类里面，生成一个校检对象
     obj = class xxx(request.POST)
     # 对页面拿到的数据进行匹配看是否符合规则， valid匹配是通过HTML页面中的name和类中字段名字一一对应的
     obj.is_valid() # 如果符合匹配规格，就返回True，如果不符合匹配规则，就返回False
     # 拿到所有的正确信息
     obj.cleaned_data
     # 拿到所有的错误信息，拿到的数据类型是一个字典类型
     dict2 = obj.errors
     ```

   + 在HTML页面中的应用

     ```django
     <body>
     <form method="post" action="/login/">
         {% csrf_token %}
         <p>
             用户：<input type="text" name="username" >{{ dict2.username.0 }}
         </p>
         <p>
             密码：<input type="text" name="password">{{ dict2.password.0 }}
         </p>
         <input type="submit" value="提交">{{ msg }}
     </form>
     </body>
     ```

##### 内部原理

1. Form组件执行`is_vaild()`方法时的原理
   + ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200923170619.png)
   
2. 继承Form组件的类，可以创建的字段类型

   + | 字段名称              | 作用和含义                             | 字段中可传递的参数                                           |
     | --------------------- | -------------------------------------- | ------------------------------------------------------------ |
     | CharFiled             | 判断输入的内容是否是一个字符串         | max_length   min_length    errors_message     required       |
     | IntegerField          | 判断输入的内容是否全是整数             | max_value   min_value    errors_message     required         |
     | EmailField            | 判断输入的内容是否是一个email格式      | max_length   min_length    errors_message     required       |
     | URLField              | 判断输入的内容是否是url格式            | max_length   min_length    errors_message     required       |
     | GenericIPAddressField | 判断输入的内容是否是ip地址格式         | max_length   min_length    errors_message     required       |
     | DateTimeField         | 判断输入的内容是否是一个日期，时间格式 | max_length   min_length    errors_message     required       |
     | DataField             | 判断输入的内容是否是一个日期           | max_length   min_length    errors_message     required       |
     | SlugField             | 判断输入的内容是否由字母下划线等组成   | max_length   min_length    errors_message     required       |
     | RegexField            | 自己自定义正则表达式                   | 第一个参数必须是自定义的正则匹配规则，max_length   min_length    errors_message     required |

3. 关于Field 和 CharField

   + 简介

     + Field是所有字段的种类，CharField都是继承自Field

   + 关于CharField

     + ```python
       class CharField(Field):
           def __init__(self, *, max_length=None, min_length=None, strip=True, empty_value='', 				**kwargs):
               pass
       ```

     + CharField的参数

       | 参数            | 含义           |
       | --------------- | -------------- |
       | max_length=None | 最大长度       |
       | min_length=None | 最小长度       |
       | strip=True      | 是否自动去空格 |
       | empty_value=''  | 空值处理       |

     + 继承CharField的字段

       1. EmailField
       2. URLField
       3. GenericIPAddressField
       4. DateTimeField
       5. DataField
       6. SlugField
       7. RegexField

   + 关于Field

     + ```python 
       class Field:
       	def __init__(self, *, required=True, widget=None, label=None, initial=None,
                        help_text='', error_messages=None, show_hidden_initial=False,
                        validators=(), localize=False, disabled=False, label_suffix=None):
       ```

     + Field的各个参数

       + 用于生成HTML标签的参数

         | 参数                                                         | 含义                                                         |
         | ------------------------------------------------------------ | ------------------------------------------------------------ |
         | **widget=None**<br />**widget =wigets.Select**生成一个select标签 | HTML插件，用来规定生成的标签是什么类型，当你使用这个参数的时候要导入widgets模块 |
         | label=None                                                   | 用于生成label标签或者显示内容                                |
         | initial=None                                                 | 初始值                                                       |
         | help_text=''                                                 | 帮助信息（在标签旁边显示）                                   |
         | show_hidden_initial=False                                    | 是否在当前插件后面再加一个隐藏的且具有默认值的插件（用于检验两次输入是否一致） |
         | disabled=False                                               | 是否可以编辑                                                 |
         | label_suffix=None                                            | label内容后缀                                                |

       + 用来做验证的参数

         | 参数                | 含义                                                         |
         | ------------------- | ------------------------------------------------------------ |
         | required=True       | 是否为空                                                     |
         | error_messages=None | 错误信息                                                     |
         | validators=()       | 自定义验证规则，需要导入validators模块中的RegexValidator模块 |
         | localize=False      | 是否支持本地化                                               |

     + 继承Field的字段

       1. IntegerField

##### 用Form组件生成HTML标签

1. 生成HTML标签的准备工作

   1. 可能会用到的参数（下面的这些参数是用来帮助生成HTML的）
      + widget=None，
      + label='用户名',
      + initial=666，
      + help_text='这是一个帮助文档'，
      +  disabled=False
      + label_suffix=':',

2. Form组件生成HTML标签时views中的具体代码

   + ```python
     class TestForm(Form):
         t1 = fields.CharField(
             # 下面的六行代码放在一起使用，会自动生成HTML标签
             widget=None,
             label='用户名',
             initial=666,
             help_text='这是一个帮助文档',
             disabled=False,
             label_suffix=':',
             # validators=[],这里面是自定义正则表达式
             required=True,
             max_length=8,
             min_length=2,
             error_messages={
                 'max_length': '最大长度不能超过8',
                 'min_length': '最小长度不能少于2',
                 'required': '不能为空'
             }
         )
         
         
     def test(request):
         if request.method == 'GET':
             # 生成一个TestForm类的对象，对象里面有关于生成HTML标签时用到的参数
             obj = TestForm()
             # 将生成的HTML标签返回给页面
             return render(request, 'test.html', {'obj': obj})
         else:
             obj = TestForm(request.POST)
             if obj.is_valid():
                 print(obj.cleaned_data)
             else:
                 print(obj.errors)
             return render(request, 'test.html', {'obj': obj})
     ```

3. 生成HTML标签时在HTML文件中的具体操作

   + ```django
     <body>
     <form action="/test/" method="post">
         {% csrf_token %}
         {# 在test方法中拿到类生成的对象，直接生成t1字段 #}
         <p>
             {{ obj.t1.label }}{{ obj.t1.label_suffix }}
             {{ obj.t1 }}{{ obj.t1.help_text }}
         </p>
         <input type="submit" value="提交">
     </form>
     </body>
     ```

4. 用Form组件实现HTML中form表单提交保留上次数据

   + 在views中的具体操作

     + ```python
       class TestForm(Form):
           t1 = fields.CharField(
               # 下面的六行代码放在一起使用，会自动生成HTML标签
               widget=None,
               label='用户名',
               disabled=False,
               label_suffix=': ',
               # validators=[],这里面是自定义正则表达式
               required=True,
               max_length=8,
               min_length=2,
               error_messages={
                   'max_length': '最大长度不能超过8',
                   'min_length': '最小长度不能少于2',
                   'required': '不能为空'
               }
           )
           t2 = fields.EmailField() 
           # 当obj = TestForm() 生成对象的时候，t2内部执行的操作是<input type="text" name="t2">
           # 当obj = TestForm(request.POST)生成对象的时候，t2内部执行的操作是<input type="text" name="t2" value="你输入的值">
           
       def test(request):
           if request.method == 'GET':
               obj = TestForm() 
               return render(request, 'test.html', {'obj': obj})
           else:
               obj = TestForm(request.POST)
               if obj.is_valid():
                   print(obj.cleaned_data)
               else:
                   print(obj.errors)
               return render(request, 'test.html', {'obj': obj})
       ```

   + 在HTML页面中的具体做法

     + ```django
       <body>
       <form action="/test/" method="post">
           {% csrf_token %}
           {# 在test方法中拿到类生成的对象，直接生成t1字段 #}
           <p>
               {# 用django内部的Form组件来生成一个HTML标签 #}
               {{ obj.t1 }}{{ obj.t1.errors.0 }}
           </p>
           <p>
               {{ obj.t2 }}{{ obj.t2.errors.0 }}
           </p>
           <input type="submit" value="提交">
       </form>
       ```



#### WSGI（web服务网关接口协议）

##### 什么是MVC,MTV

1. MVC
   + models(数据库，模型)
   + views（HTML模板）
   + controllers（业务逻辑）
2. MTV
   + models（数据库，模型）
   + template（HTML模板）
   + views（业务逻辑）
   + django采用的的是MTV
3. 作用：
   + 就是分类处理功能



