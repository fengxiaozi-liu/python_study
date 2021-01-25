"""
蓝图的框架
    project
        project
            static  存放静态文件的地方
            templates 存放模板的地方
            views    存放视图函数的地方
                account.py
                admin.py
                __init__.py
            manage.py


蓝图中各个文件的书写
    在manage.py 文件中写上
        from project import app
        if __name__=__main__:
            app.run()

    在init文件中写上
        from flask import Flask  在init文件中生成一个app
        app = Flask(__name__)


        from .views import account 导入视图函数
        from .views import admin

        app.register_blueprint(account.ac)  让app关联视图函数
        app.register_blueprint(admin.ad)
    在account.py文件中写上
       from flask import Blueprint    导入蓝图
       ac = Blueprint('ac',__name__)
       @ac.route('/login')       用蓝图管理url与视图函数的对应关系
       def login():
        return 'login

蓝图的作用
    蓝图可以指定静态文件和模板的地址，但是会先从init文件中找，没有再到指定的蓝图里面去找
    给指定的蓝图设定好before_request请求之后，只要调用这个蓝图的url就会执行这个方法
    可以给指定的蓝图添加前缀url  url_prefix='/account'

蓝图的三大作用；
    目录结构的划分
    url的划分
    before_request
"""

