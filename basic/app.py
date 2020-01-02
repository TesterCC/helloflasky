#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-30 14:40'

"""
Flask入门教程   
https://read.helloflask.com/c3-template

Watchlist 程序

按照默认设置，Flask会从程序实例所在模块同级目录的templates文件中寻找模版

查看Jinja2所有可用的过滤器
http://jinja.pocoo.org/docs/2.10/templates/#list-of-builtin-filters

run in terminal:
cd ~//helloflasky/basic
python app.py


在 Flask 中，我们需要创建一个 static 文件夹来保存静态文件，它应该和程序模块、templates 文件夹在同一目录层级。
Favicon（favourite icon） 是显示在标签页和书签栏的网站头像。
你需要准备一个 ICO、PNG 或 GIF 格式的图片，大小一般为 16×16、32×32、48×48 或 64×64 像素。

use .flaskenv launch
flask run

# create data.db
from basic.app import db
db.create_all()

"""

import os
import sys

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# name = 'Lily Li'
# movies = [
#     {'title': 'My Neighbor Totoro', 'year': '1988'},
#     {'title': 'Dead Poets Society', 'year': '1989'},
#     {'title': 'A Perfect World', 'year': '1993'},
#     {'title': 'Leon', 'year': '1994'},
#     {'title': 'Mahjong', 'year': '1996'},
#     {'title': 'Swallowtail Butterfly', 'year': '1996'},
#     {'title': 'King of Comedy', 'year': '1999'},
#     {'title': 'Devils on the Doorstep', 'year': '1999'},
#     {'title': 'WALL-E', 'year': '2008'},
#     {'title': 'The Pork of Music', 'year': '2012'},
# ]


"""
如果你使用 Windows 系统，上面的 URI 前缀部分需要写入三个斜线（即 sqlite:///）。
在本书的示例程序代码里，做了一些兼容性处理，另外还新设置了一个配置变量
如果你固定在某一个操作系统上进行开发，部署时也使用相同的操作系统，那么可以不用这么做，直接根据你的需要写出前缀即可
"""

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)

# 写入了一个 SQLALCHEMY_DATABASE_URI 变量来告诉 SQLAlchemy 数据库连接地址
# print(app.root_path)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

# 在扩展类实例化前加载配置  REF: https://read.helloflask.com/c5-database
db = SQLAlchemy(app)


class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字
    email = db.Column(db.String(120), unique=True)  # 邮箱


class Book(db.Model):  # 表名将会是 book
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 书籍标题
    year = db.Column(db.String(4))  # 书籍年份


# 和 flask shell类似，我们可以编写一个自定义命令来自动执行创建数据库表操作
import click

"""
默认情况下，函数名称就是命令的名字，现在执行 flask initdb 命令就可以创建数据库表
使用 flask initdb --drop 选项可以删除表后重新创建
"""


@app.cli.command()  # 注册为命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息


"""
因为有了数据库，我们可以编写一个命令函数把虚拟数据添加到数据库里。下面是用来生成虚拟数据的命令函数
"""


@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    # 全局的两个变量移动到这个函数内
    name = 'Lily Li'
    books = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
        {'title': 'Fluent Python', 'year': '2015'},
        {'title': 'Python Cookbook 3rd Edition', 'year': '2013'},
        {'title': 'DevOps in Python', 'year': '2019'}
    ]

    user = User(name=name)
    db.session.add(user)
    for b in books:
        book = Book(title=b['title'], year=b['year'])
        db.session.add(book)

    db.session.commit()
    click.echo('Done.')


@app.route('/')
def index():
    user = User.query.first()  # 读取用户记录
    books = Book.query.all()  # 读取所有书籍记录
    return render_template('index.html', user=user, movies=books)


@app.route('/about')
def about_me():
    username = 'Lily'
    bio = 'human'
    return render_template('about_me.html', username=username, bio=bio)


"""
用 app.errorhandler() 装饰器注册一个错误处理函数，它的作用和视图函数类似，
当 404 错误发生时，这个函数会被触发，返回值会作为响应主体返回给客户端
"""


@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    user = User.query.first()
    return render_template('404.html', user=user), 404  # 返回 模板 和 状态码

# 和我们前面编写的视图函数相比，这个函数返回了状态码作为第二个参数，普通的视图函数之所以不用写出状态码，是因为默认会使用 200 状态码，表示成功。

# 对于多个模板内都需要使用的变量，我们可以使用 app.context_processor 装饰器注册一个模板上下文处理函数
# 这个函数返回的变量（以字典键值对的形式）将会统一注入到每一个模板的上下文环境中，因此可以直接在模板中使用。
@app.context_processor
def inject_user():   # 函数名可以随意修改
    user = User.query.first()
    return dict(user=user)    # 需要返回字典，等同于return {'user': user}



if __name__ == '__main__':
    app.run(debug=True, port=5555)
