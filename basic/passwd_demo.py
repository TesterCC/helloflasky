#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-01-04 22:00'

"""
ref:
https://read.helloflask.com/c8-login

Flask 的依赖 Werkzeug 内置了用于生成和验证密码散列值的函数，
werkzeug.security.generate_password_hash() 用来为给定的密码生成密码散列值，
而 werkzeug.security.check_password_hash() 则用来检查给定的散列值和密码是否对应。
"""

from werkzeug.security import generate_password_hash,check_password_hash

pw_hash = generate_password_hash('cat')   # 为密码 cat 生成密码散列值
print(pw_hash)    # pbkdf2:sha256:150000$P0LrrdgN$888a0273921e6f12f348f167fb8413a7a9600d854ef9ec4a64b7aa5cd98dba5d

print(check_password_hash(pw_hash, 'cat'))  # 检查散列值是否对应密码 cat
print(check_password_hash(pw_hash, 'dog'))  # 检查散列值是否对应密码 dog