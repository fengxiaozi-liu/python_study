from flask import Flask, request, render_template, redirect, jsonify, make_response

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    # 请求相关的
    # request.args  拿到get请求头里面的数据
    # request.form  拿到form表单里面的数据
    # request.method 请求的方法
    # request.full_path 请求的全部路径

    # 响应相关的
    # return render_template()  返回模板
    # return jsonfy()   返回json处理后的数据
    # return redirect()  重定向
    return '4-请求和响应'

    # 设置响应头响应体和cookie
    # response = make_response(render_template('index.html'))   设置响应的模板
    # response.delete_cookie('key')              删除cookie
    # response.set_cookie('key', 'value')       设置cookie
    # response.headers['x-something'] = 'a value'  设置响应头
    # return response  返回


if __name__ == '__main__':
    app.run()
