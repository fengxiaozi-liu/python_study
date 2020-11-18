from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)
app.debug = True


# 自定义正则表达式
class RegexConverter(BaseConverter):
    # 拿到正则匹配的字符
    def __init__(self, map, regex):
        super(RegexConverter, self).__init__(map)
        self.regex = regex

    # 通过python进行转化
    def to_python(self, value):
        return value

    # 反向生成url
    def to_url(self, value):
        val = super(RegexConverter, self).to_url(value)
        return val


# 让flask知道有这个转化器
app.url_map.converters['regex'] = RegexConverter  #


# 在flask里面添加路由有两种方式，第一种方式就是调用一个装饰器
# 第二种方式就是调用一个add_url_rule方法将对应的视图函数传递进去

# 方式1建立路由
# endpoint是给路由取一个别名用于反向生成，如果不写就是函数名, 用url_for来反向生成
# 可以在后面传递参数，也可以自定制正则表达式
@app.route('/index/<regex("\d+"):nid>', methods=['GET', 'POST'], redirect_to='/new')
def index(nid):
    print(nid, type(nid))
    x = url_for('index', nid=999)
    print(x)
    return 'index'


@app.route('/new', methods=['GET', 'POST'])
def new():
    return 'new'


# 方式2建立路由
@app.route('/login', methods=['GET', 'POST'], endpoint='n2')
def login():
    return 'login'


@app.route('/layout', methods=['GET', 'POST'], endpoint='n3')
def layout():
    return 'layout'


if __name__ == '__main__':
    app.run()
