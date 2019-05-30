#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/12 22:36'

'''
Flask Web开发--狗书 P12-13
程序上下文的使用方法
'''

from hello import app
from flask import current_app

# print(current_app.name)   # will report error
# 未激活程序上下文之前调用current_app.name会报错

app_ctx = app.app_context()    # 获得一个程序上下文
app_ctx.push()      # 推送程序上下文
print(current_app.name)     # 可以正常调用
app_ctx.pop()

