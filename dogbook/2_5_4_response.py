#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/21 19:40'

from flask import Flask
from flask import request

"""
Flask Web开发--狗书 P14
2-5-4 响应
"""

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Bad Request test</h1>', 400

if __name__ == '__main__':
    app.run(debug=True)