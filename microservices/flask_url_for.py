#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/28 11:13'

# P30 url_for
from flask_converter import app
from flask import url_for

with app.test_request_context():
    print(url_for('person',name='Tarek'))   # /api/person/1