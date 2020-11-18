from flask import Flask, session, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'sdfasdfxc'


@app.route('/index', methods=['GET', 'POST'])
def index():
    return 'index'


@app.route('/order', methods=['GET', 'POST'])
def order():
    return 'order'


"""
flask的中间件原理是重写一个wsgi_app,在wsgi_app()执行之前，对原生的请求做操作
可以用来做黑名单，在处理请求之前，我们处理原生的请求
"""


class Middleware:
    def __init__(self, old_wsgi_app):
        """
        服务打算启动的时候自动执行
        :param old_wsgi_app:
        """
        self.old_wsgi_app = old_wsgi_app

    def __call__(self, *args, **kwargs):
        """
        每次用户不同请求到来的时候执行
        :param args:
        :param kwargs:
        :return:
        """
        return self.old_wsgi_app(*args, **kwargs)


if __name__ == '__main__':
    app.wsgi_app = Middleware(app.wsgi_app)
    app.run()
