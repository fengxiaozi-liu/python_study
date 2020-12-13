from flask import blueprints, render_template, session, redirect

home = blueprints.Blueprint('home', __name__)


@home.route('/index', methods=['GET', 'POST'])
def index():
    if session.get('user_info'):
        print(session['user_info'])
        return 'index'
    return redirect('/login')


@home.route('/test', methods=['GET', 'POST'])
def test():
    if session.get('user_info'):
        print(session['user_info'])
        return 'test'
