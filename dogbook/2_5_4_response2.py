#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/21 19:40'

from flask import Flask
from flask import make_response

"""
Flask Web开发--狗书 P14
2-5-4 响应
如果不想返回由 1 个、2 个或 3 个值组成的元组,
Flask 视图函数还可以返回 Response 对象。
make_response() 函数可接受 1 个、2 个或 3 个参数(和视图函数的返回值一样),
并返回一个 Response 对象。
"""

app = Flask(__name__)


@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

if __name__ == '__main__':
    app.run(debug=True)