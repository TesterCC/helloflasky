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

差异：Movie 等于 Book
"""

import os
import sys

from flask import Flask, render_template, request,url_for, redirect, flash
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
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'flask@2020'   # 等同于app.secret_key = 'flask@2020' 不设置的话POST会报错。这个密钥的值在开发时可以随便设置。基于安全的考虑，在部署时应该设置为随机字符，且不应该明文写在代码里， 在部署章节会详细介绍。

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


# @app.route('/')
@app.route('/', methods=['GET', 'POST'])    # 默认只接受 GET 请求
def index():
    if request.method == 'POST':
        # Flask 会在请求触发后把请求信息放到 request 对象里, 比如请求的路径（request.path）、请求的方法（request.method）、表单数据（request.form）、查询字符串（request.args）等等
        title = request.form.get('title')   # 传入表单对应输入字段的 name 值。request.form 是一个特殊的字典，用表单字段的 name 属性值可以获取用户填入的对应数据
        year = request.form.get('year')

        # 验证数据
        # 通过在 <input> 元素内添加 required 属性实现的验证（客户端验证）并不完全可靠，我们还要在服务器端追加验证
        # 提示:在真实世界里，你会进行更严苛的验证，比如对数据去除首尾的空格。一般情况下，我们会使用第三方库（比如 WTForms）来实现表单数据的验证工作。
        if not title or not year or len(year) > 4 or len(title) > 60:
            flash('Invalid input!!!')  # 显示错误提示。flash() 函数在内部会把消息存储到 Flask 提供的 session 对象里。session 用来在请求间存储数据，它会把数据签名后存储到浏览器的 Cookie 中，所以我们需要设置签名所需的密钥。
            return redirect(url_for('index'))  # 重定向回主页

        # 保存表单数据到数据库
        movie = Book(title=title, year=year)  # 创建记录
        db.session.add(movie)  # 添加到数据库会话
        db.session.commit()  # 提交数据库会话
        flash('Item created successfully.')  # 显示成功创建的提示
        return redirect(url_for('index'))  # 重定向回主页

    user = User.query.first()  # 读取用户记录
    books = Book.query.all()  # 读取所有书籍记录
    return render_template('index.html', user=user, movies=books)


@app.route('/book/edit/<int:movie_id>', methods=['GET', 'POST'])
def edit(movie_id):
    book = Book.query.get_or_404(movie_id)

    if request.method == 'POST':  # 处理编辑表单的提交请求
        title = request.form['title']
        year = request.form['year']

        if not title or not year or len(year) > 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('edit', movie_id=movie_id))  # 重定向回对应的编辑页面

        book.title = title  # 更新标题
        book.year = year  # 更新年份
        db.session.commit()  # 提交数据库会话
        flash('Item updated.')
        return redirect(url_for('index'))  # 重定向回主页

    return render_template('edit.html', movie=book)  # 传入被编辑的电影/书籍记录


# 为了安全的考虑，我们一般会使用 POST 请求来提交删除请求，也就是使用表单来实现（而不是创建删除链接）
@app.route('/movie/delete/<int:movie_id>', methods=['POST'])  # 限定只接受 POST 请求
def delete(movie_id):
    movie = Book.query.get_or_404(movie_id)  # 获取电影记录
    db.session.delete(movie)  # 删除对应的记录
    db.session.commit()  # 提交数据库会话
    flash('Item deleted.')
    return redirect(url_for('index'))  # 重定向回主页


@app.route('/about')
def about_me():
    username = 'Lily'
    bio = 'human'
    return render_template('about_me.html', username=username, bio=bio)

@app.route('/simple_form')
def simple_form():
    return render_template('simple_form.html')


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
