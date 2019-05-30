#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/10/18 15:33'

from flask import Flask

app = Flask(__name__)


"""
“使用 app.route 装饰器注册视图函数是首选方法，但不是唯一的方法”

摘录来自: [美] 米格尔 • 格林贝格. “Flask Web开发：基于Python的Web应用开发实战（第2版）”。

run in terminal：
cd ~/...../hello/
flask run

other usage:
cd ~/...../hello/
flask shell

填坑：
IsADirectoryError: [Errno 21] Is a directory: '/Users/XXXX/.env'
这个报错是因为本地~/.env有这么一个文件夹，而这个文件夹又限于.flaskenv文件被加载。

当安装了python-dotenv时，Flask在加载环境变量的优先级是：手动设置的环境变量>.env中设置的环境变量>.flaskenv设置的环境变量。

解决方法：
不用.flaskenv，改成.env 中写flask相关配置
"""


# the minimal Flask application
@app.route('/')
def index():
    return '<h1>Hello, World! -- by <i>MFC</i></h1>'


@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# P76-77 Flask Web开发实战入门、进阶与原理解析    # 因为flask也自带转义，所以也没那么容易被注入
@app.route('/greet/', defaults={'name': 'Pen Tester'})   # 不加后面的斜杠，127.0.0.1:5555/greet/访问会报错
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, <i>%s</i>!</h1>' % name


# extend P55 Flask Web开发
@app.route('/user/<name>/<int:age>')
def user(name, age):
    return '<h1>Hello, {} . {} years old.</h1>'.format(name, age)


# the other router   P53 Flask Web开发
def other_router():
    return '<h1>Hello, other router!</h1>'


app.add_url_rule('/other', 'other_router', other_router)

if __name__ == '__main__':
    app.run(debug=True, port=7777)  # default: debug=None
