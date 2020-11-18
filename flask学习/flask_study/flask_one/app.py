from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)  # 创建一个flask类的对象
app.debug = True
app.secret_key = 'usfsdkf'  # 给session签名，就是给session加密
user_dict = {
    '1': {'name': '张三', 'age': 18},
    '2': {'name': '李四', 'age': 28},
    '3': {'name': '王五', 'age': 38},
}


# flask写路由是用装饰器，让url与函数对应关系
@app.route('/login', methods=['GET', 'POST'])
def login():
    print('请求到来')
    # flask的一大特点是当请求到来的时候不是通过参数传递的,是放在request模块中的
    if request.method == 'GET':
        return render_template('login.html')
    # request.form就是从表单里面拿数据 request.args就是从url中获取get传递的参数
    user = request.form.get('user')
    pwd = request.form.get('password')
    if user == 'alex' and pwd == '123':
        # 用户登录成功之后，把用户信息放入session
        # flask中的session是默认放到浏览器中cookie里面，不帮忙保存
        session['user_info'] = user
        return redirect('/index')
    else:
        # flask渲染有两种方式第一种方式，传递一个字典
        # return render_template('login.html', **{'msg': '用户名或者密码错误'})

        # 第二种方式 传递一个参数的形式
        return render_template('login.html', msg='用户名或者密码错误')


@app.route('/index')
def index():
    if not session.get('user_info'):
        return redirect('/login')

    return render_template('index.html', user_list=user_dict)


@app.route('/detail')
def detail():
    if not session.get('user_info'):
        return redirect('/login')
    else:
        nid = request.args.get('nid')
        user_info = user_dict[nid]
        return render_template('detail.html', users=user_info)


@app.route('/layout')
def layout():
    del session['user_info']
    return redirect('/login')


if __name__ == '__main__':
    app.run()
