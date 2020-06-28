#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/28 10:50'

"""
P29
python flask_converter.py 

curl localhost:5000/api/person/1
"""

from flask import Flask, jsonify, request
from werkzeug.routing import BaseConverter,ValidationError

_USERS = {'1':'Tarek',
          '2':'Freya',
          '3':'Lily'}

_IDS = {val:id for id,val in _USERS.items()}

# 创建自定义转换器，但注意实际开发中不要过多依赖转换器
class RegisteredUser(BaseConverter):

    def to_python(self, value):
        '''将值转换成视图中用到的python对象
        :param value:
        :return:
        '''
        if value in _USERS:
            return _USERS[value]
        raise ValidationError()

    def to_url(self, value):
        '''执行反向url_for
        :param value:
        :return:
        '''
        return _IDS[value]

app = Flask(__name__)
app.url_map.converters['registered'] = RegisteredUser


@app.route("/api/person/<registered:name>")
def person(name):
    response = jsonify({'Hello visitor ': name})
    return response

if __name__ == '__main__':
    app.run()