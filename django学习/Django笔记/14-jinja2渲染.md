#####  用jinja2第三方工具进行渲染

1. python中的相关代码

```python
from jinja2 import Template
template = Template(data)
# render 就是渲染
data = template.render(user_list=user_list)
```

2. 用jinjia2提取数据库的数据

```jinja2
<tbody>
{% for row in use_list %}
	<tr>
		<td>{{row.id}}</td>
		<td>{{row.username}}</td>
		<td>{{row.password}}</td>
	</tr>
{% end for%}
</tbody>
```

##### 创建网站时的总结

1. http是无状态，短连接

2. 浏览器（socket客户端）

   网站（socket服务端）

3. 自己写网站

   1. socket服务端

   2. 根据url的不同返回不同的内容

      路由系统

      ​	url --> 函数

   3. 字符串返回给用户

      静态网站是不变的

      动态网站是改变的

      ​	HTML充当模板

      ​	自己创建创造任意数据

      ​	通过模本引擎的渲染

      ​	最后返回一个字符串

4. web框架

   1.框架种类

     + 第一种
        	+ 需要写socket客户端，还需要写路由系统和渲染数据
             	+ tornado就是这种框架
     + 第二种
        	+ 不需要自己写socket，需要写路由和渲染数据的工作
             	+ 其中Django就是这一种框架，他可以使用wsgiref来调用别人的socket服务端
   + 第三种
     + 只需要写路由系统，不需要写socket服务端，也不需要渲染数据
     + flask就是这种形式框架

   5.其他种类的分类

    + Django框架
      	+ 设计一个网站功能比较多选用Django
    + 其他
      	+ 要设计一个小的不需要选用Django



​	