from flask import Flask
import time

app = Flask(__name__)


@app.route('/index')
def index():
    print('第一个视图')
    time.sleep(2)
    return 'hello word'


@app.route('/demo')
def demo():
    print('第二个视图')
    time.sleep(2)
    return 'hello demo'


@app.route('/func')
def func():
    print('第三个视图')
    time.sleep(2)
    return 'hello func'


if __name__ == '__main__':
    app.run()
