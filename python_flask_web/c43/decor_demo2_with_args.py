# coding=utf-8
"""
DATE:   2020/12/10
AUTHOR: Yanxi Li
"""

# 4.3.2 对带参数的函数使用装饰器

# def func(*args,**kwargs):
#     print(len(args),args)
#     for i in kwargs:
#         print(kwargs[i])
#
# func(1,'a',2,username='z3',score=98)

from flask import Flask
from functools import wraps

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def user_login(func):
    @wraps(func)  # 使用wraps在装饰器的函数上对传进来的函数进行包裹，这样就不会丢失原始函数
    def inner(*args, **kwargs):
        print("登录时操作")  # 打印模拟登录操作
        func(*args, **kwargs)  # user_login()接收到的函数

    return inner


@user_login
def news():
    print(news.__name__)
    print("There is news detail.")


news()
print(news.__name__)

print("-" * 33)


@user_login
def news_list(*args):
    page = args[0]
    print(news_list.__name__)
    print("This is news list page " + str(page))


news_list(7)

if __name__ == '__main__':
    app.run()
