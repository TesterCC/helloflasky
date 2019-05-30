#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/12 22:35'


from flask import Flask

app = Flask(__name__)

'''
Flask Web开发--狗书 P8
2-1 Basic Demo
'''


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run(debug=True)    # default: debug=None