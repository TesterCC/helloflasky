#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-01-07 16:27'

"""
https://read.helloflask.com/c9-test
"""

import unittest
from say_hello import sayhello   # 这样import虽然在pycharm中报错，但是在命令行中可以正常执行
# cd ~/helloflasky/basic
# python test_say_hello.py


# 测试用例
class SayHelloTestCase(unittest.TestCase):  # 测试用例继承 unittest.TestCase 类，在这个类中创建的以 test_ 开头的方法将会被视为测试方法。

    # 测试固件
    def setUp(self):
        # setUp() 方法会在每个测试方法执行前被调用
        pass

    # 测试固件
    def tearDown(self):
        # tearDown() 方法则会在每一个测试方法执行后被调用
        pass

    # 每一个测试方法（名称以 test_ 开头的方法）对应一个要测试的函数/功能/使用场景。
    # first test
    def test_sayhello(self):
        rv = sayhello()
        self.assertEqual(rv, 'Hello!')

    # second test
    def test_sayhello_to_somebody(self):
        rv = sayhello(to="Lily")
        self.assertEqual(rv, 'Hello, Lily!')

if __name__ == '__main__':
    unittest.main()


"""
常用的断言方法：
assertEqual(a, b) 
assertNotEqual(a, b) 
assertTrue(x) 
assertFalse(x) 
assertIs(a, b) 
assertIsNot(a, b) 
assertIsNone(x) 
assertIsNotNone(x) 
assertIn(a, b) 
assertNotIn(a, b) 
"""