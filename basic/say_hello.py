#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-01-06 17:56'

"""
简单单元测试用例
ref:https://read.helloflask.com/c9-test
"""

def sayhello(to=None):
    if to:
        return 'Hello, %s!' % to
    return 'Hello!'