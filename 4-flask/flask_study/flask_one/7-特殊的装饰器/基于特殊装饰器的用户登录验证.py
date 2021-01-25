from flask import Flask, session, request, redirect

app = Flask(__name__)
app.secret_key = 'asdfasdfsa'


# 相当于django中间件的process_request
@app.before_request
def check_login():
    if request.path == '/login':
        return None
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    session['user_info'] = 'user_info'
    return 'login'


@app.route('/index', methods=['GET', 'POST'])
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
