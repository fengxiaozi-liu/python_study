"""
session的设置流程
    1.请求第一次到来的时候
        ctx = RequestContext() 创建一个RequestContext对象
            两个参数
            -request  放置请求的内容
            -6-session=None 一个空的session
        ctx.push() 在调用push方法的时候其实是调用了session_interface是SecureCookieSessionInterface的一个对象
            执行ctx.6-session = SecureCookieSessionInterface.open_session
    2.执行视图函数
    3.请求结束的时候
        执行SecureCookieSessionInterface.save_session把session写到cookie里面去
"""
from flask import Flask, session
import uuid


app = Flask(__name__)

app.secret_key = str(uuid.uuid4())

# 使用template_global装饰器可以让函数变成一个变量，让每个模板都可以使用，变量名就是函数名


@app.route('/index', methods=['GET', 'POST'])
def index():
    session['k1'] = 123
    return 'index'


@app.route('/order', methods=['GET', 'POST'])
def order():
    print(session.get('k1'))
    return 'order'


if __name__ == '__main__':
    app.run()
    # app.__call__()
    """
    app.__call__ 请求到来执行call方法
    调用wsgi_app
    """
