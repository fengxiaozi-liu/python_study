from flask import Flask, session, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'sdfasdfxc'

"""
闪现的原理就是
    把数据保存在session里面，然后取数据的时候用session中pop方法，取出数据后删除
    可以用flash和get_flashed_messages方法共同实现
"""


@app.route('/index', methods=['GET', 'POST'])
def index():
    flash('我也不知道', category='x1')
    flash('我也不知道2', category='x2')
    return 'index'


@app.route('/order', methods=['GET', 'POST'])
def order():
    print(get_flashed_messages(category_filter=['x1']))
    return 'order'


if __name__ == '__main__':
    app.run()
