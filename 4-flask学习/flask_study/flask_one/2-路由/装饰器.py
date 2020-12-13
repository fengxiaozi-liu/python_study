from flask import Flask, render_template, request, redirect, session
import functools

app = Flask(__name__)
app.secret_key = 'ufasdgs'


def wrapper(func):
    @functools.wraps(func)  # 让内部的函数名与func的函数名相同不在是inner
    def inner(*args, **kwargs):
        if session.get('user_info'):
            return func(*args, **kwargs)
        else:
            return redirect('/login')

    return inner


@app.route('/index', methods=['GET', 'POST'])
# 当用route装饰的时候如果wrapper没有调用functools来进行装饰，那么endpoint的每一个值都是inner，不能完成反向调用
@wrapper
def index():
    return 'index'


@app.route('/login', methods=['GET', 'POST'])
def login():
    session['user_info'] = '12315'
    return 'login'


if __name__ == '__main__':
    app.run()
