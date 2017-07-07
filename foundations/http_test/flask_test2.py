# encoding:utf-8
from flask import Flask, request, render_template

# 初始化flask对象
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def sign_in_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def sign_in():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('sign-ok.html', username=username)
    else:
        #直接跳转了
        return '<h2>Invalid username or password</h2>'


if __name__ == '__main__':
    app.run(port=8080)
