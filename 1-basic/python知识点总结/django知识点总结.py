django知识点总结(url路由系统，模板，Form组件，中间件，seession,cookie,xss,csrf)

url路由系统
	一个url地址对应一个url函数
	url一般放在url.py文件中
	from django.urls import path, re_path,include 导入定义url的函数
	from app01 import views 导入一个视图函数， 里面放置着对应的函数
	path('test/', views.test, name='test')

	re_path('^test.html/(？P<args>\d+)$', views.test, name='test')
		使用re_path可以利用正则表达式,()里面表示传递一个参数

	path('app01/', include('app01.url'))
		将app里面的一个url导入到总的视图函数里面以便可以调用

	反生成url
		在视图函数中的操作
			from django import reserve
			url = reservr('test',arg=(1,))
		在HTML页面中的操作
			{% url 'test' 变量i %}


视图函数
	from django.shourct import render, HttpResponse, redirect
	def test(request,arg):
		return render(request, 'test.html', {}) 
		return redirect('/test/') 
		return HttpResponse('ok') 
	request参数一定要有，里面包含了请求的所有信息，包括form表单提交或者是ajax提交
	arg是一个参数，里面是接收来自正则表达的url的参数
	'test.html' 表示指定返回哪个页面
	{} 里面是放置要渲染的数据，要传递给前端的HTML页面
	redirect('/test/') 表示要跳转到哪个页面
 	HttpResponse('ok') 里面放置什么内容就会返回什么内容，一般是传递一个json对象，配合ajax使用


ORM操作
	orm的两大功能是操作表和操作数据行

	orm配置数据库
		django中默认使用的数据库是SQLite，我们还有可能使用到mysq
		1.orm配置mysql数据库
			在__init__.py文件中写入代码
				import pymysql
				pymysql.install_as_MYSQLdb()
			在setting.py文件中写入一个数据库
				DATABASES = [
					'default': {
						'ENGINE':'djang.db.backends.pymysql',
						'HOST':'127.0.0.1',
						'PORT':3306,
						'USER':'liu'
						'PASSWORD':'lh284259'
						'NAME': 'python_study'
					}
				]
			在setting.py文件中注册app
		2.orm对表的操作
			1.用orm创建一张表(在models.py模块中使用)
				class UserInfo(model.MODEL):
					username = models.CharField(max_length=32) 定义一个字符串字段
					password = models.CharField(max_length=64)
					gender_list = ((1,'男')，(2,'女'))
					gender = models.IntegerField(choices=gender_list) 定义一个枚举类型的字段
					ut = models.Forerignkey('表名'，on_delete=models.CASAD) 和一张表建立外建关联
					ut = model.ManyTOMany('表名'， on_delete=models.CASAD) 
						建立一个多对多关系的关联，会自动的生成一张新的表，里面存放多对多的关系

				字段中可以设置的属性
					max_length, 最大长度
					min_length, 最小长度
					default,  默认值是多少
					null,  是否可以为空
					unique, 唯一索引
					db.index 是否可以有索引
					class Meta:
						index_together = [('b','g')] 联合索引
						unique_together = [('b','g')] 联合唯一索引

				给外键命名
					boy = models.Forerignkey('UserInfo', related_name='boy')
						通过给外键命名可以不使用表名_set来找到对象了

			2.orm对表中数据的操作
				1.向表内添加数据
					在views.py文件中导入from app01 import models

					models.UserInfo.object.create(name='zhangsan') 添加一个数据
					user_list = {name:'zhangsan', age:18}
					models.UserInfo.object.create(**user_list) 可以传递一个字典类型的数据

					add_list = [
						models.UserInfo(name=lisi)
						models.UserInfo(name=wangwu)
					]
					models.UserInfo.object.bulkcreate(add_list) 可以一次性添加多个数据

				2.删除表中的某个数据
					model.UserInfo.object.filter(id=1).delete()

				3.表的更改
					models.UserInfo.object.filter(id=1).update(name='lisi') 更改一条数据
					update_list={name:'lisi',age:18}
					models.UserInfo.object.filter(id=2).update(**update_list) 
						可以传递一个字典更改多条数据

				4.表的查询操作
					a. 单表的查询
						拿取全部的数据
							model.UserInfo.object.all() 查询表中的所有数据Queryse列表里面存放的是对象
							model.UserInfo.object.all().only('id','name')
								只查询表中的id,name字段，	Queryset列表里面还是一个对象
						条件筛选数据		
							model.UserInfo.object.filter(id=1,name='zhangsan').first() 
								根据条件筛选，并且filter里面的条件是and连接
							filter_list = {'id':1,'name':'zhangsan'}
							model.UserInfo.object.filter(**filter_list).first() 
								传递进来一个字典查询，字典里面的条件是and连接
						比较符筛选
							models.UserInfo.object.filter(id__gt=1) 筛选出id>1的数据
							model.UserInfo.object.filter(id__lt=1) 筛选出id<1的数据
							model.UserInfo.object.filter(id_gte=1)
							model.UserInfo.object.filter(id__lte=2)
							model.UserInfo.object.exclude(id=1) 拿取除了id=1的全部数据
						范围筛选
							models.UserInfo.object.filter(id__in=[1,2,3]) 是否在里面
							models.UserInfo.object.filter(id__range=[1,3]) 是否在这个范围之内
							models.UserInfo.object.filter(name__startwith='xx') 是否以xx开头
							model.UserInfo.object.filter(name__contains='xx') 里面是否包含xx
						排序
							models.UserInfo.object.all().order_by('id') 按id正向排序
							models.UserInfo.object.all().order_by('-id') 按id反向排序
						分组
							models.UserInfo.object.all().value('id').annotate(Count(1))
				5.特殊查询
					F查询(from django.db.models import F)
						F的作用是拿到原来字段的值一般用于更新数据
						model.UserInfo.object.all().update(F('age')+1) 对表中所有的年龄+1
					Q查询(from django.db.models import Q)
						Q的作用是用来做查询的，用于构造复杂的查询条件，一般他有两种用法
						第一种用法(用生成对象的方式来调用)：
							model.UserInfo.object.filter(Q(id=1)&Q(name='lisi')) 做合并查询
							models.UserInfo.object.filter(Q(id=1)|Q(name='zhangsan')) 做或者查询
						第二种用法(生成方法的方式来进行查询)：
							con = Q() 生成一个Q对象
							q1 = Q()	升成一个Q对象
							q1.connector = 'OR' 中间用or的方式来连接
							q1.childern.append('id',1)
							q1.childern.append('id',2)

							q2 = Q() 生成第二个Q对象
							q2.connector = 'OR'
							q2.childern.append('name','zhangsan')
							q2.childern.append('name','lisi')

							con.add(q1,'AND')
							con.add(q2,'AND')
							models.UserInfo.object.filter(con) 传递进来查询的条件 
					extra查询
						model.UserInfo.object.all().extra(
							select={'n':'select count(1) from usertype'}, 增加选择
							select_param=[1,],
							where=['id=%s or id=%s','name=%s'], 增加条件判断
							param=[1,2,'zhangsan'], 给where传递参数
							order_by=['id'] 按照id进行排序
							)
					raw查询(可以传递原生的sql语句)
						models.UserInfo.objects.raw('select * from student where id=%s',[1,])

					导入原生的sql进行查询
						from django.db import connect,connections
						cursor = connect().cursor()
						cursor = connections['default'].cursor()
						cursor.excute('insert into student(name) values(%s)',[zhangsan,])

				6.联表查询操作
					联表查询会用到外键或者是表名小写_set
						obj = models.UserInfo.objects.filter(id=1).first()
						obj.ut.title 拿到被关联表的title字段
						obj.usertype_set.all() 反向查询拿到关联表的字段

					查询过程中返回不同的数据类型
						obj = models.UserInfo.objects.all() 列表里面是对象
						obj = models.UserInfo.objects.all().value('id','name','ut__title','usertype__girl') 
							列表里面是字典,ut__title是通过外键拿取关联表的数据，usertype__girl是反向拿取数据
						obj = models.UserInfo.objects.all().value_list('id','name') 列表里面的数据是元组


模板知识点总结(母版，公共的组件，在模板里面自定义函数)

母版
	母版就是先写好公共的地方，让其他的HTML页面可以继承他
	{% extend 母版名称 %} 继承一个母版
	一个母版一般由网页头部，网页的中间部分组成
	<html>
		<head>
			{% block css %}{% endblock %} 一般用来继承css样式
		</head>
		<body>
			<div class="page-header">
			</div>
			<div class="page-body">
				<div class="menus">
				</div>
				<div class="content left">
					{% block content %}{% endblock %}
				</div>
			</div>
			{% block js %}{% endblock %}
		</body>
	</html>
公共的组件
	include关键字来使用公共的组件
	<div>
		<h3>组件</h3>
		<div class="title">标题：</div>
		<div class="content"> 内容：</div>
	</div>
	{% include 'pub.html' %} 调用这个组件

在模块里面自定义函数
	1.现在app文件中建一个文件名为templatetags的文件
	2.在文件内写入一个py文件
	3.在py文件内部写入下面的代码
		from django import template
		register = template.Libary()
		@register.filter
		def myfunc(value):
			return upper(value)
	4.在HTML文件中调用这个函数
	{% load xx %}
	{{arg|函数名}} 调用自己定义的函数

Form组件(Form组件有三大功能，1.做用户验证，2.生成HTML标签，3.保留上次输入的内容)
	1.创建一个Form验证的类
		from djang.form import Form,fields 导入可以用来生成Form验证的模块
		创建一个类，这个类必须继承Form
		class LoginForm(Form):
			定义一个字段 
			username = fields.CharField(max_length=32,min_length=12,required=True)
			email = fields.EmailField()

		自定义的Form验证的类常用的字段
			CharField() 用来验证一个字符串类型的字段
			IntegerField() 用来验证是否是一个整型的字段
			URLFields() 用来验证是否是一个url字段
			IPAddressField() 用来验证是否是一个ip地址
			DateTimeField() 验证输入的内容是否是一个日期时间
			DateField() 验证输入的内容是否是一个日期
			SlugField() 验证输入的内容是否是字母数字或者下划线组成
			RegexField(正则表达式,)自定义正则规则验证，第一个参数必须是正则表达式

		字段中的参数
			一般参数
				max_length 定义最大长度
				min_length 定义最小长度
				max_value	定义最大值 在IntegerField里面使用哪个
				min_value	定义最小值 在IntegerField里面使用
				required=True 定义是否为空
				errors_message={} 定义错误信息提示

			生成标签相关的参数
				from django.form import widgets 导入生成标签的模块
				widget=None/widgets.Select(choices=[()]) 
					定义标签的类型,默认是input标签
					当变成select框之后choices里面传递的是一个元组
				label='用户名' 定义提示文字
				label_suffix=': '在提示文字的后面加上冒号
				help_tex="说明信息" 用来说明这段文字的内容
				initial=666 生成一个默认值
				from django.core.Validators import RegexValidator 
				Validators=[RegexValidator('正则规格'，'错误时的提示信息')] 这里可以自定义正则表达式

	2.用Form做验证
		在views.py中做验证：
			def test(request):
				obj = TestForm() 如果不加参数，里面是没有值的，可以用来生成HTML标签
				obj = TestForm(request.POST) 里面含有请求信息，
				if obj.is_vaild():判断是否符合Form规则验证，符合就返回True，不符合就返回False
					obj.cleaned_data 拿到前端提交的正确的信息，是用字典的形式进行保存的
				else:
					obj.errors 拿到一个错误的信息，是一个对象

		在HTML标签中生成标签和，返回错误信息
			{{obj.t1}}生成HTML标签 {{obj.errors.t1.0}}如果有错误返回HTML标签里面的错误

	3.用Form组件来保留上一次输入的信息
		{{obj.cleaned_data.t1}


cookie和session：
	cookie
		定义和作用：
			cookie是保存在浏览器客户端的键值对，是解决用户登录和浏览器无状态的
		一般使用设置cookie：
			def test(request):
				if request.method == 'GET':
					obj = render(reqeust,'test.html')

					cookie的设置要在返回页面之前进行
					obj.set_cookie('ticket', 'qwert',max_age=100) 
						设置一般的cookie，没有附加签名状态
					obj.set_signed_cookie('ticket', 'qwert', max_age=100, salt='jjj')
						设置签名后的cookie，一般是用来加盐的，可以起到一定的保护措施，但是不大

					return obj
		一般使用之获取cookie
			tk = request.COOKIES.get('ticket') 获取没有加盐的cookie
			tk = request.get_signed_cookie('ticket',salt='jjj') 获取加盐的cookie

			if tk:如果这个cookie存在，就返回一个页面
				return render(request,'test.html')
			else: 否则跳转到登录页面
				return redirect('/login/')

	session
		定义
			session是保存在服务端的数据，本质也是键值对，不过他能指定保存的地址，是缓存还是文件等
		作用:
			session依赖于cookie而存在，他的作用是保持会话

		session的使用之创建session
			def login(request):
				if request.method == 'POST':
					obj = LoginForm(request.POST)
					username = obj.cleaned_data['username']
					passwd = ojc.cleaned_data['password']
					user = models.UserInfo.objects.filter(user=user,password=passwd).first()
					if user:
						request.session['userinfo'] = obj.cleaned_data 设置session
						在这个过程中session执行了三个操作
							1.生成随机的字符串
							2.通过cookie发送给客户端
							3.服务端保存随机的字符串
					return redirect('/index/')
		session使用之获取session
			def index(request):
				user_info = request.session.get('user_info')
				if not user_info:
					return redirect('/index/')
				else:
					if request.method == 'GET':
						return render(request,'index.html')
					else:
						pass

		session中的方法：
			设置session的方法
				requset.session[key]=value  给session设置值会完成三个步骤 最常用的设置session的方法
					1.生成随机的字符串
					2.将随机的字符串通过cookie发送到客户端
					3.将随机的字符串保存到服务daunt
				request.session.setdefault(key,value) 给一个键值对设置值，如果此键值对存在就不设置

				del request.session[key] 删除一个session随机的字符串以及相关的数据

			获取session的方法
				request.session.keys()   获取session的key值
				request.session.values() 获取session的value值
				request.session.items()  获取session中的key和value值

				request.session.session_key 获取设置的用户随机字符串
				request.session.delete(session_key) 删除当前用户所有的数据，在服务端删除
				request.session.clear() 清空session数据只是前端清空
				request.session.set_expiry(value) 设置失效时间
					 value = datatime.datatime().now()+timedelta(day=3) 设置三天后失效

		session中的配置
			SESSION_ENGINE='django.contrib.session.backends.db'
			SESSION_COOKIE_NAME = 'gtdx' 设置session在前端显示的名字
			SESSION_COOKIE_PATH = '/'  设置页面上url生效的范围
			SESSION_SAVE_EVERY_REQUEST=False 是否每次请求都刷新一次session

	xss攻击和csrf
		xss攻击：
		定义：
			xss攻击是指别人在你的HTML页面上写了一段代码，这段代码被保存在数据库中
			当你从数据库中取数据渲染到你的HTML页面上，这段代码就会生效，影响你原有的代码
		解决办法：
			1.在HTML页面渲染的时候尽量的不要使用safe关键字
			2.在views.py文件中尽量的不要是用mark_safe 
		csrf:
			定义：
				csrf中文全称是跨站请求伪造，就是别人自己写了一个网站，在网站的某个地方是访问你url地址的，
				窃取后端的信息

			解决办法：
				1.保证账户退出
				2.在HTML页面中{% csrf_token %}
				3.在后端打开csrf保护

			关于csrf的一些操作：
				局部打开csrf
					from django.views.decorates.csrf import csrf_exempt, csrf_protect
					@csrf_protect
					def func(request):
						pass

				局部关闭
					@csrf_exempt
					def func(reqeust):
						pass

				在cbv中的使用：
					from django.views import View 
					@method_decorator(@csrf_exempt,name='get')
					class Foo(View):
						def get(self, reqeust):
							pass













 
				

