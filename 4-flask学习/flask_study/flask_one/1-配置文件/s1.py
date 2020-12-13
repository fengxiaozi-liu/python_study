from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.config.from_object('setting.DevelopmentConfig')  # 从settings里面拿到一个开发环境放到配置文件中


@app.route('/index', methods=['GET', 'POST'])
def index():
    return 'hello'


if __name__ == '__main__':
    app.run()
