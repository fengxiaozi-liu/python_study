#####  Django的框架

 1. 为什么选用框架

    ​	框架就是在别人写好的基础上，实现自己的业务

	2. 创建的文件对应关系

    ```python
    # 里面存放的是创建的Django的设置
    settings.py
    # 里面存放是是url地址和函数的对应关系
    urls.py
    # 里面存放的是一个socket连接  web服务网关接口
    wsgi.py
    # 管理网站的文件
    manage.py
     
    ```

    ```shell
    # 在终端启动创建自己的网站
    python manage.py runserver
    ```

	3. Django程序目录

    	1. manage.py 

        1. 作用

           以后对Django程序的所有操作都是基于manage.py的

        2. 具体操作

           ```shell
           python manage.py runserver/etc.
           ```

    	2. 同名文件加下的配置文件

        	1. settings.py 
                 	1. Django的配置文件
        	2. urls.py
                 	1. 路由系统  url和函数的对应关系
        	3. wsgi.py
                 	1. 用于定义Django用什么socket，wsgiref，uwsgi

    3. Django中返回一个界面给用户

       1. django中导入一个函数，并返回的方法

          ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200908153240.png)

       2. django中返回一个静态页面给用户

          ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200908170405.png)

          ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200908170500.png)

       3. Django中返回一个动态的页面给用户

          ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200908171244.png)

          ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200908171343.png)

    

    ##### 创建Django的project的步骤

    1. 创建一project

    2. 配置

       1. 模板路径

          ```python
          EMPLATES = [
              {
                  'BACKEND': 'django.template.backends.django.DjangoTemplates',
                  # 这是一个render回复请求时，找的文件地址
                  'DIRS': [os.path.join(BASE_DIR, r'C:\Users\19693\Desktop\Django学习HTML页面')],
                  'APP_DIRS': True,
                  'OPTIONS': {
                      'context_processors': [
                          'django.template.context_processors.debug',
                          'django.template.context_processors.request',
                          'django.contrib.auth.context_processors.auth',
                          'django.contrib.messages.context_processors.messages',
                      ],
                  },
              },
          ]
          ```

          

       2. 静态文件路径

          ```python
          # 使用时的前缀是什么
          STATIC_URL = '/static/'
          # 真实的目录在什么下面，加入进去，以后要STATIC_URL和STATICFILES_DIRS中配合使用
          STATICFILES_DIRS = (
              os.path.join(BASE_DIR, r'C:\Users\19693\Desktop\Django学习HTML页面'),
          )
          ```

       3. 额外配置

          ```python
          MIDDLEWARE = [
              'django.middleware.security.SecurityMiddleware',
              'django.contrib.sessions.middleware.SessionMiddleware',
              'django.middleware.common.CommonMiddleware',
              # 把下面的一行代码注释掉
              # 'django.middleware.csrf.CsrfViewMiddleware',
              'django.contrib.auth.middleware.AuthenticationMiddleware',
              'django.contrib.messages.middleware.MessageMiddleware',
              'django.middleware.clickjacking.XFrameOptionsMiddleware',
          ]
          ```
      
       4. url 的对应关系
      
          1. /login/ 	login
      
             ```python
             def login(request):
                 # request里面的方法
             	request.method
             	request.GET # GET从请求头的URl中取值
             	request.POST # POST从请求体中取值
                 return HttpResponse('内容')
             	return render(request,'路径地址',{...})
               	return redirect('要跳转的网址')
             ```
             
            ```python 
             > 发**GET**请求的时候，只有GET里面有值
             > 如果用**POST**发送请求的时候，GET和POST里面都有可能值
             ```
    
    ##### 基于Django搭建的一个用户登录页面
    
    ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200908174632.png)
    
    ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200908174643.png)
    
    ![](C:\Users\19693\Desktop\Django学习图片\QQ截图20200908174845.png)
    
    









