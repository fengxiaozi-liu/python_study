"""
flask-session的作用是将原来session的数据放入到redis数据库里面
导入flask-session，导入redis
让session的设置变成由RedisSessionInterface设置

"""
from flask import Flask, session
from flask_session import Session
from redis import Redis

app = Flask(__name__)
app.secret_key = 'dsfjsadvsd'
# 设置redis保存session有两种方式
# 方式1：
# from flask_session import RedisSessionInterface
# app.session_interface = RedisSessionInterface(
#     redis=Redis(host='127.0.0.1', port=6379),
#     key_prefix='flaskxxx'
# )

# 方式2：
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis(host='127.0.0.1', port=6379)
Session(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    session['user_info'] = 123
    return 'login'


@app.route('/index', methods=['GET', 'POST'])
def index():
    v = session.get('user_info')
    print(v)
    return 'index'


if __name__ == '__main__':
    app.run()
