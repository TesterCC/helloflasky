#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/21 19:40'

from flask import Flask
from flask import redirect

"""
Flask Web开发--狗书 P15
2-5-4 响应
重定向经常使用 302 状态码表示,指向的地址由 Location 首部提供。
重定向响应可以使用 3 个值形式的返回值生成,也可在 Response 对象中设定。
不过,由于使用频繁,Flask 提供了 redirect() 辅助函数,用于生成这种响应
"""

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('http://fullstackpentest.com')

if __name__ == '__main__':
    app.run(debug=True)