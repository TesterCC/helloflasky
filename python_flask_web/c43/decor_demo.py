# coding=utf-8
"""
DATE:   2020/12/10
AUTHOR: Yanxi Li
"""

# 4.3.1 装饰器的定义和基本使用  函数不带参数

def user_login(func):
    def inner():
        print("登录时操作")  # 打印模拟登录操作
        func()              # user_login()接收到的函数
    return inner


def news():
    print("There is news detail.")

show_news = user_login(news)  # 将news作为user_login()的参数

show_news()     # 调用函数执行
print(show_news.__name__)    # 由此可知实际上调用的是inner()函数

print("-"*20)

# 既然是装饰器，就可以用这样的语法糖
@user_login
def news_v2():
    print("There is news v2 detail.")

news_v2()
print(news_v2.__name__)