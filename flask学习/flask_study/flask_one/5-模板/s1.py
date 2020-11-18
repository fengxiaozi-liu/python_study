from flask import Flask, render_template, redirect, request, jsonify, make_response, Markup

app = Flask(__name__, template_folder='../5-模板/templates')


# 使用template_global装饰器可以让函数变成一个变量，让每个模板都可以使用，变量名就是函数名
@app.template_global()
def get_input(value):
    return Markup('<input value="%s">' % value)


@app.route('/index', methods=['GET', 'POST'])
def index():
    context = {
        'k1': 123,
        'k2': [11, 22, 33],
        'k3': {'name': 'jack', 'age': 18},
        'k4': lambda x: x + 1,
        'k5': get_input,
    }
    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.run()
