from flask import blueprints, render_template, request, session, redirect
from wtforms import Form, validators, widgets
from wtforms.fields import simple, core
import uuid

ac = blueprints.Blueprint('ac', __name__)


class LoginForm(Form):
    username = simple.StringField(
        validators=[
            validators.DataRequired(message='用户名不能为空'),
            validators.Regexp('A(\w+)', message='以大写字母A开头')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    passwd = simple.StringField(
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.length(min=6, max=12, message='密码必须是6-12位')
        ],
        widget=widgets.TextInput(),
        render_kw={'type': 'password', 'class': 'form-control'}
    )


class RegisterForm(Form):
    username = simple.StringField(
        validators=[
            validators.DataRequired(message='用户名不能为空'),
            validators.Regexp(r'(\w+)', message='以大写字母A开头')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'},
        label='用户名',
    )
    passwd = simple.PasswordField(
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.length(min=6, max=12, message='密码必须是6-12位')
        ],
        render_kw={'class': 'form-control'},
        label='密码',
    )
    favor = core.SelectField(
        choices=((1, '男'), (2, '女')),
        label='爱好',
        coerce=int,
    )

    # 实现字段实时更新
    # def __init__(self, *args, **kwargs):
    #     super(RegisterForm, self).__init__(*args, **kwargs)
    #     self.favor.choices = models.userinfo.objects.values_list('id', 'name')

    # 钩子函数
    # def validate_name(self, field):
    #     obj = models.userinfo.objects.filter(name=field.data).first().name
    #     if obj:
    #         raise validators.ValidationError('用户已经存在')


@ac.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        forms = LoginForm()
        return render_template('login.html', forms=forms)
    else:
        forms = LoginForm(formdata=request.form)
        if forms.validate():
            if forms.data['username'] == 'Alex' and forms.data['passwd'] == '123456':
                uid = str(uuid.uuid4())
                session['user_info'] = 'sadfsdcs'
                return redirect('/index')
        return render_template('login.html', forms=forms)


@ac.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        forms = RegisterForm()
        return render_template('register.html', forms=forms)
