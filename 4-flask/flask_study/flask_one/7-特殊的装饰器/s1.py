from flask import Flask, session

app = Flask(__name__)


# 相当于django中间件的process_request
@app.before_request
def xxx():
    print('执行前')


# 相当于django中间件的process_response
@app.after_request
def ttt(request):
    print('执行后')
    print(request)
    return request


@app.route('/index', methods=['GET', 'POST'])
def index():
    print('视图函数index')
    return 'index'


@app.route('/order', methods=['GET', 'POST'])
def order():
    print('视图函数order')
    return 'order'


if __name__ == '__main__':
    app.run()
