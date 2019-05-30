#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/21 19:40'

from flask import Flask
from flask import abort

"""
Flask Web开发--狗书 P15
2-5-4 响应
还有一种特殊的响应由 abort 函数生成,用于处理错误。
在下面这个例子中,如果 URL 中, 动态参数 id 对应的用户不存在,就返回状态码 404
"""

app = Flask(__name__)


@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)     # not install load_user,nee install Flask-Login
    if not user:
        abort(404)
    return '<h1>Hello, %s</hi>' % user.name

if __name__ == '__main__':
    app.run(debug=True)