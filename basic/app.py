#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-30 14:40'


"""
Flask入门教程   
https://read.helloflask.com/c3-template

按照默认设置，Flask会从程序实例所在模块同级目录的templates文件中寻找模版

查看Jinja2所有可用的过滤器
http://jinja.pocoo.org/docs/2.10/templates/#list-of-builtin-filters

run in terminal:
cd ~//helloflasky/basic
python app.py


在 Flask 中，我们需要创建一个 static 文件夹来保存静态文件，它应该和程序模块、templates 文件夹在同一目录层级。
Favicon（favourite icon） 是显示在标签页和书签栏的网站头像。
你需要准备一个 ICO、PNG 或 GIF 格式的图片，大小一般为 16×16、32×32、48×48 或 64×64 像素。
"""


name = 'Lily Li'
movies = [
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
]

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

@app.route('/about')
def about_me():
    username = 'Lily'
    bio = 'human'
    return render_template('about_me.html', username=username, bio=bio)

if __name__ == '__main__':
    app.run(debug=True, port=5555)