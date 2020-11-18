#####  1. 目标：利用Django和pymysql做学员管理

 1. 表

    + 班级
    + 学生
    + 老师

    里面有单表和多表，有一对一，一对多和多对多的样式

	2. 单表

    	1. 增
    	2. 删
    	3. 改
    	4. 查

	3. 一对多表的操作

    	1. 增
    	2. 删
    	3. 改
    	4. 查

	4. 多对多表操作

       1. 增
       2. 删
       3. 改
       4. 查

##### 2. 利用到的知识

 	1. Django基础
 	2. 前端知识（复习）
      	1. HTML
      	2. css
      	3. js
      	4. jquery

##### 3. 内容回顾一

 1. web框架的本质

    + 就是socket服务端和客户端进行通信

    + 遵循的规则是http协议，短连接和无状态
      	+ 发送的时候有请求头和请求体	
      	+ 返回的时候是响应头和响应头
      	+ 模板引擎的渲染是服务端	
      	+ 请求和返回的内容都是字符串，可以放在一个文件里

    2.Django

     1. 安装

        Django-admin startproject  <file-name>

    2. 创建Django的步骤

      1. 配置

          	1. 模板路径
             	2. 静态文件
                	3. CSRF的注释掉

      2. url.py

          	1. url对应函数

            1. 函数至少有一个参数request里面包含了用户请求的所有信息

               ```python
               def index(request):
               	request.method
                   request.GET
                   request.POST
                   return HttpResponse
               	return render(request,'文件件路径(模板的路径)',{要渲染的变量})
               	return redirect('跳转的网址url')
               ```

            2. 模板的渲染

           ```html
           <!---获取到单个值的写法 --->
           <h1>
               {{变量名}}
           </h1>
           <!--- for 循环语句 --->
           {% for item in `列表名` %}
           	{{item}}
           {% endfor %}
           
           ```

##### 4. 用Django创建学生管理系统时出的错误

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200909171230.png)

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200909171443.png)

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200909171613.png)

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200909171828.png)

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200909172225.png) ​![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200909175918.png)

##### 5. 处理一对多的关系时总结

  2. ###### 模态对话框

  3. ###### 引入ajax

  4. ###### 处理一对多的时候，出错的地方

     ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200910102905.png)

     ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200910103059.png)

     ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200910103211.png)

     ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200910102804.png)

     ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200910114111.png)

     ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200910114317.png)

     

 	5. ###### 注意：

     现在写的网页没有对用户提交的数据做出判断

     后面会在views中引入Form组件来对用户提交的数据进行判断

  6. ###### 关于form表单

     ​		form表单提交，页面会刷新，因为action是把数据返回给指定的url，我们使用了什么样的url就会返回到什么地方

  7. ###### ajax的回顾

     + 总结

       + 模态对话框中提交数据要用到ajax

       + 原因：ajax在不刷新页面的情况下把数据提交给后台

         ```jinja2
         
         <script src="/static/jquery-1.12.4.js"></script>
         <script>
         	{# showModal方法当调用这个方法的时候，取出容器标签的隐藏属性，让它显示出来 #}
             function showModal(){
                 document.getElementById('shadow').classList.remove('hide');
                 document.getElementById('modal').classList.remove('hide');
             }
             {# ConcleSend方法，当调用这个方法的时候就让给容器标签添加隐藏样式，让它隐藏起来 #}
             function ConcleSend(){
                 document.getElementById('shadow').classList.add('hide');
                 document.getElementById('modal').classList.add('hide');
             }
             {# 定义提交数据时候的函数，里面要引入ajax，目的就是为了让它在不刷新页面的情况下将数据传递给后台 #}
             function AjaxSend(){
             {#有几点必须指定，提交到哪，提交的数据类型，提交的数据，提交成功之后做什么，提交失败之后做什么#}
             	{# $符号是jquery中特有的标记，当看到$符号时就是需要引入jquery #}
             	{# $.ajax 就是引入jquery中的ajax，ajax里面必须指定url:将数据传递到哪，这样后台才能根据指定的		url来调用相关的函数，进行判断操作,type:传递数据的方式是GET还是POST，后台应该以什么method方式		 去,data:是要向后台传递的数据，是以键值对的形式传递的,success:当传递成功后执行，后台返回数据要执		行的函数 #}
                 $.ajax({
                     url:'/modal_add_class/', {# 提交到哪 #}
                     type:'POST', {# 以什么方式提交 #}
                     {# data必须是键值对，因为后台取数据是通过key来获取的 #}
                     {# $.('#title')是指向名为title的容器 #}
                     {# $.('#title').val()是拿到名为title容器的value值，是容器要传递给后台的的值 #}
                     data:{'title':$('#title').val()},
                     {# data必须传入进取作为一个参数 #}
                     success:function (data){
                     {#  当服务端处理完成后，返回数据之后，函数会自动调用  #}
                     {# data是服务端返回的值 #}
                         console.log(data);
                         if(data =='ok'){
                             {# ajax怎么都不会跳转，他返回的是一个字符串，如果想要跳转必须写js #}
                             {# form表单会自动跳转，ajax返回字符串怎么都不会跳转 #}
                             location.href='/class';  {# 这里就是js中的跳转方法 #}
                         }else{
                             $('#errormsg').text(data);
                         }
                     },
                 })
             };
         </script>
         ```

     + 模态对话框（一般与ajax联系）和 新url

       + 模态对话框
         + 一般是是少量的输入框或者数据少的时候就用模态对话框
         + 最常用的是登录
       + 新url
         + 一般是数据量较多的时候使用
         + 最常用的就是博客，其中京东就是新url

##### 6. 内容回顾（关于web框架的本质：基于socket的服务端和客户端的交互）

1. 浏览器（socket客户端）

   + 作用：发送ip和端口
   + get请求和post请求：
     + 相同点：都有请求头和请求体
     + 不同点：get请求中的数据一般是在请求头中，post请求的数据一般是在请求体里面

2. 服务端（socket服务端）

   + 作用：1. 启动并监听ip和端口 2.接收请求进行处理，返回

3. 关于响应

   + 响应头：返回状态码

   	+ 响应体：返回的字符串内容

4. 响应的类型

   + 普通相应：页面直接显示
   + 重定向响应：再一次请求url

5. 关于重定向

1. 响应头：里面含有要跳转的url地址

   location：‘https://www.baidu.com

2. 响应体

   	1. 重定向的时候无响应体
      	2. 对于重定向来说，请求和相应都是浏览器做的，服务端只是提供返回的数

##### 7. 利用ajax操作对话框（重点和难点）

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200911115952.png)

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200911120307.png)

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200911120901.png)

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200911121042.png)

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200911121417.png)

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200912000159.png)

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200912000425.png)

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200912000725.png)

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200912000859.png)

##### 8. 多对多表操作知识点（重点）

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200912110128.png)

![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200912110518.png)

##### 9. Bootstrap

1. ###### 简介

   + 包含css和js 的代码库

2. ###### 包含内容

   + 样式

   + 响应式

     + 响应式布局：根据页面的大小改变布局 

     + 响应式体现：主要依赖于@media关键字

     + 代表性

       + 导航条
       + 栅格式布局

     + ```jinja2
       {# 是否允许对页面进行缩放 #}
       <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
       ```

3. ###### 根据项目做布局

   1. 后台管理布局（最常用的一类）

      **固定住菜单栏和内容栏，并且给内容栏添加滚轮**

      ```jinja2
      <style>
              body{
                  margin: 0;
              }
              .page-header{
                  height: 48px;
                  {# 最小宽度当大于等于1190时占页面的100%，当小于1190时才会出现滚动条 #}
                  min-width: 1190px;
                  background-color: #204d74;
              }
              .menus{
                  width: 200px;
                  {# 绝对定位 #}
                  position: absolute;
                  {# 距离上下左右的位置 #}
                  left: 0;
                  top: 48px;
                  right: 0;
                  bottom: 0;
                  background-color: #269abc;
              }
              .content{
                  position: absolute;
                  left: 200px;
                  top: 48px;
                  right: 0;
                  bottom: 0;
                  background-color: #a94442;
                  {# 当溢出的时候出现滚轮 #}
                  overflow: scroll;
              }
      
          </style>
      ```

##### 10. 关于母版的问题（重点）

	1. 母版的使用

+ ```jinja2
  {# 母版是的继承用 {% extends ’母版文件名‘ %} #}
  {# 在母版的哪一个地方写上 {% block 变量名}{% endblock %} #}
  {# 在引入的时候，哪个地方写上 {% block 变量名}内容{% endblock %} #}
  /*
  中间内容一般是写你想要传递的东西，标签，样式 或者是js等
  */
  ```

+ 模板样式写法

+ ```jinja2
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <link rel="stylesheet" href="/static/plugins/bootstrap-3.3.7-dist/css/bootstrap.css">
      <link rel="stylesheet" href="/static/plugins/font-awesome-4.7.0/css/font-awesome.css">
      <link rel="stylesheet" href="/static/my_css/student_manager.css">
      <title>Title</title>
      {% block css %}{% endblock %}
  </head>
  <body>
  {# =============================一般网页的布局是分成头部和中间部分，其中中间部分又可以分成左边和右边============================= #}
  
  {# ==================网页的头部======================== #}
  <div class="page-header">
  
      <div class="logo left">老男孩后台管理</div>
      <div class="avatar right" style="position: relative">
          <img style="width: 40px;height: 40px" src="/static/image/佐助.jpg" alt="">
          <div class="user-info">
              <a style="color: white">个人资料</a>
              <a style="color: white">注销</a>
          </div>
      </div>
      <div class="rmenus right">
          <a class="fa fa-commenting-o">消息</a>
          <a><i class="fa fa-envelope" aria-hidden="true"></i>邮件</a>
      </div>
  
  </div>
  
  {# ================网页的中间部分======================= #}
  <div class="page-body">
  
      {# ======网页的菜单栏========== #}
      <div class="menus">
          <a href="/class/"><i class="fa fa-list-ul" aria-hidden="true"></i>班级管理</a>
          <a href="/students/"> <i class="fa fa-list-ul" aria-hidden="true"></i>学生管理</a>
          <a href="/teacher"><i class="fa fa-list-ul" aria-hidden="true"></i>老师管理</a>
      </div>
  
      {# =======网页的内容栏========= #}
      <div class="content left">
          {# 这里面引入了一个模板的概念 当用block时，标签里面的内容就会在新的页面显示 #}
          {# 同时引入这个layout模板需要再要引用的页面写上{% extend 文件名 %} #}
          {# {% extend 文件名 %}表示引用哪个模板 #}
          {% block new_content %}{% endblock %}
      </div>
  </div>
  {% block js %}{% endblock %}
  </body>
  </html>
  ```

+ 关于子版的页面写法

+ ```jinja2 
  {# 继承母版 #}
  {% extends 'layout.html' %}
  
  {# 插入样式 #}
  {% block css %}
      <style>
          .hide {
              display: none;
          }
  
          {# 遮罩层的创建遮住 #}
          .shadow {
              position: fixed;
          {# fixed是固定在某个地方相对于窗口来说的 #} left: 0;
              top: 0;
              right: 0;
              bottom: 0;
              z-index: 999;
              background: black;
              opacity: 0.4;
          }
  
          .modal1 {
              z-index: 1000;
              position: fixed;
              left: 50%;
              top: 50%;
              background: white;
              height: 300px;
              width: 400px;
              margin-left: -200px;
              margin-top: -150px;
          }
      </style>
  {% endblock %}
  
  {# 插入内容 #}
  {% block new_content %}
      <ul class="nav nav-tabs">
          <li role="presentation" class="active"><a href="#">首页</a></li>
          <li role="presentation"><a href="#">学生管理</a></li>
          <li role="presentation"><a href="#">学生添加</a></li>
      </ul>
      <div>
          <a href="/add_student/">添加</a>
          <a id="addModal">对话框添加</a>
          {# ==============================新url方式操作学生====================== #}
          <table class="table table-striped table table-bordered table table-hover">
              <thead>
              <tr>
                  <td>id</td>
                  <td>学生姓名</td>
                  <td>学生所属班级</td>
                  <td>操作</td>
              </tr>
              </thead>
              <tbody>
              {% for student in student_list %}
                  <tr>
                      <td>{{ student.id }}</td>
                      <td>{{ student.name }}</td>
                      <td cls_id="{{ student.class_id }}">{{ student.title }}</td>
                      <td>
                          <a href="/del_student/?nid={{ student.id }}">删除</a>
                          <a href="/edit_student/?nid={{ student.id }}">编辑</a>
                          <a class="editModal">对话框编辑</a>
                          <a class="delModal">对话框删除</a>
                      </td>
                  </tr>
              {% endfor %}
              </tbody>
          </table>
  
          {# 网页分页 #}
          <nav aria-label="Page navigation">
              <ul class="pagination">
                  <li>
                      <a href="#" aria-label="Previous">
                          <span aria-hidden="true">&laquo;</span>
                      </a>
                  </li>
                  <li><a href="#">1</a></li>
                  <li><a href="#">2</a></li>
                  <li><a href="#">3</a></li>
                  <li><a href="#">4</a></li>
                  <li><a href="#">5</a></li>
                  <li>
                      <a href="#" aria-label="Next">
                          <span aria-hidden="true">&raquo;</span>
                      </a>
                  </li>
              </ul>
          </nav>
  
          {# =========================================模态对话框操作学生======================================== #}
          <div id="shadow" class="shadow hide"></div>
  
          {# =================模态对话框添加学生================== #}
          <div id="add_modal" class="modal1 hide">
              <h3>增加学生信息对话框</h3>
              <p>
                  姓名：<input id="add_name" type="text" name="name" placeholder="姓名">
              </p>
              <p>
                  班级:
                  <select id="add_class_id" name="class_id">
                      {% for class in class_list %}
                          <option value="{{ class.id }}">{{ class.title }}</option>
                      {% endfor %}
                  </select>
              </p>
              <input id="btn_add" type="button" value="提交"><span id="add_error"></span>
              <input type="button" value="取消" onclick="concle_modal()">
          </div>
  
          {# =========================模态对话框编辑学生=========================== #}
          <div id="edit_modal" class="modal1 hide">
              <h3>编辑学生信息对话框</h3>
              <p>
                  <input id="edit_id" type="text" name="id" style="display: none">
                  姓名：<input id="edit_name" type="text" name="name">
              </p>
              班级：
              <select id="edit_class_id" name="class_id">
                  {% for class in class_list %}
                      <option value="{{ class.id }}">{{ class.title }}</option>
                  {% endfor %}
              </select>
              <p>
              </p>
              <input id="btn_edit" type="button" value="确认更新"><span id="edit_error"></span>
              <input type="button" value="取消" onclick="concle_modal()">
          </div>
  
          {# ===============模态对话框删除学生======================== #}
          <div id="del_modal" class="modal1 hide">
              <h3>删除学生对话框</h3>
              <p>
                  <input id="del_id" type="text" name="id" style="display: none">
                  姓名：<input id="del_name" type="text" name="name">
              </p>
              <p>
                  班级：
                  <select id="del_class_id" name="class_id">
                      {% for class in class_list %}
                          <option value="{{ class.id }}">{{ class.title }}</option>
                      {% endfor %}
                  </select>
              </p>
              <input id='btn_del' type="button" value="确认删除"><span id="del_error"></span>
              <input type="button" value="取消" onclick="concle_modal()">
          </div>
      </div>
  {% endblock %}
  
  {# 插入js #}
  {% block js %}
  {# =======================用jquery中的ajax添加点击事件================== #}
  <script src="/static/jquery-1.12.4.js"></script>
  <script>
  
      {# ==================遮罩层隐藏起来的函数====================== #}
  
      function concle_modal() {
          document.getElementById('shadow').classList.add('hide');
          document.getElementById('add_modal').classList.add('hide');
          document.getElementById('edit_modal').classList.add('hide');
          document.getElementById('del_modal').classList.add('hide');
      }
  
      {# ==================等页面加载出来后利用jquery操作学生的函数(里面函数让遮罩层显示出来和利用ajax发送数据的方法)================ #}
      $(function () {
  
          {# =======一个点击事件让添加学生标签的遮罩层显示出来======= #}
          $('#addModal').click(function () {
              $('#shadow,#add_modal').removeClass('hide');
          });
  
          {# ========ajax添加学生：利用ajax向后台发送数据并进行页面刷新=============== #}
          $('#btn_add').click(function () {
              $.ajax({
                  url: '/modal_add_student/',
                  type: 'POST',
                  data: {'name': $('#add_name').val(), 'class_id': $('#add_class_id').val()},
                  success: function (arg) {
                      arg = JSON.parse(arg);
                      if (arg.status) {
                          location.reload();
                      } else {
                          $('#add_error').text(arg.message);
                      }
                  }
              })
          });
  
          {# =============一个点击事件可以让编辑学生的遮罩层显示出来============== #}
          $('.editModal').click(function () {
              $('#shadow,#edit_modal').removeClass('hide');
              /*
              1.获取当前标签是$(this)
               */
              var row = $(this).parent().prevAll();
              var student_name = $(row[1]).text();
              var student_id = $(row[2]).text();
              var class_id = $(row[0]).attr('cls_id');
              $('#edit_id').val(student_id);
              $('#edit_name').val(student_name);
              $('#edit_class_id').val(class_id);
  
          });
  
          {# ============ajax编辑学生：利用ajax向后台发送数据并且进行页面刷新===================== #}
          $('#btn_edit').click(function () {
              $.ajax({
                  url: '/modal_edit_student/',
                  type: 'POST',
                  data: {
                      'id': $('#edit_id').val(),
                      'name': $('#edit_name').val(),
                      'class_id': $('#edit_class_id').val()
                  },
                  dataType: 'JSON',
                  success: function (arg) {
                      if (arg.status) {
                          location.reload();
                      } else {
                          $('#edit_error').text(arg.message);
                      }
                  }
              })
          });
  
          {# =============一个点击事件可以让删除学生达到遮罩层显示出来============== #}
          $('.delModal').click(function () {
              $('#del_modal,#shadow').removeClass('hide');
              var row = $(this).parent().prevAll();
              var student_id = $(row[2]).text();
              var student_name = $(row[1]).text();
              var class_id = $(row[0]).attr('cls_id');
              $('#del_id').val(student_id);
              $('#del_name').val(student_name);
              $('#del_class_id').val(class_id);
          });
  
          {# =================ajax删除学生: 利用ajax删除学生向后台发送数据再进行页面刷新 #}
          $('#btn_del').click(function () {
              $.ajax({
                  url: '/modal_del_student/',
                  type: 'POST',
                  dataType: 'JSON',
                  data: {'id': $('#del_id').val()},
                  success: function (arg) {
                      if (arg.status) {
                          location.reload();
                      } else {
                          $('#del_error').text(arg.message);
                      }
                  }
              })
          })
      })
  </script>
  {% endblock %}
  ```

2. 使用母版和子版时的注意事项

   + 模板在引入的时候只有四个板块，没有了head和body

   		1. **继承模板**：{% extends `模板`  %}

   		2. **插入css样式**：{% block `css`  %}{% endblock %}

           		3. **插入内容**：{% block `content`  %}{% endblock %}
          + 这里不管你写几个，只要不是css样式和js函数，都算是插入内容

   		4. **插入js样式**：{% block `js `  %}{% endblock %}

##### 11. cookie

1. ###### 定义

   + cookie是保存在浏览器端的键值对
   + 服务端可以向用户浏览器端写cookie
   + 客户端每次发送请求时，会携带cookie去

2. ###### 作用

   + 解决浏览器无状态的特性

   + 存放一些用户登录的凭证

3. ###### 应用

   + 投票
   + 用户登录

4. ###### cookie的具体用法

   1. 给一个网页设置cookie

      ```python
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
                  # 在返回网页之前，弄一个记录，语法可以用set_cookie
                  objc.set_cookie('ticket', 'qwert')
                  return objc
              else:
                  return HttpResponse('用户名或者密码错误')
      ```

   2. 可以给cookie设置超时时间

      1. 第一种方式（推荐使用这一种方式）

         + ```python
           objc = redirect('/class/')
           objc.set_cookie('ticket', 'qwert',max_age=10)
           ```

      2. 第二种方式

         + ```python 
           import datetime
           from datetime import timedelta
           # ct是当前的时间
           ct = datetime.datetime.now()
           # timedelta是设置时间的可以是小时，秒，分钟或者星期等等
           v = timedelta(seconds=10)
           # value是当前时间加上一个你设置的时间 也就是多长时间后的一个具体时间
           value = ct + v
           objc.set_cookie('ticket', 'qwer', expires=value)
           ```

      3. cookie的一般获取方式：

         + ```python 
           # 无签名的cookie的获取方式
           tk = request.COOKIES.get('ticket')
           # 有签名的cookie获取方式
           tk = request.get_singed_cookie
           ```

   3. set_cookie中一些其他的参数

      ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200914232148.png)

      ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200914232611.png)

   4. cookie的签名方式

      1. 用set_signed_cookie进行加密处理（可以自己定义签名）

      + ```python
        # 在返回页面之前进行加密
        objc.set_signed_cookie('ticket', '1234', salt='jjjj')
        # 在拿取数据的时候要进行解密
        tk = request.get_signed_cookie('ticket', salt='jjjj')
        ```

      2. 定义一个内置函数让每一个页面都能获得cookie

      + ```python
        def dec_cookie(fn):
            def inner(request):
                tk = request.COOKIES.get('ticket')
                if not tk:
                    return redirect('/login/')
                return fn(request)
            return inner
        ```

        