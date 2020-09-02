# coding=utf-8
'''
DATE: 2020/09/02
AUTHOR: Yanxi Li
'''

# P86-87 在Jinjia 2模板中使用for语句

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def goods_info():
    goods = [
        {"name": "Fluent Python", "price": "110.00"},
        {"name": "Python Cookbook, 3rd Edition", "price": "91.50"},
        {"name": "The Go Programming Language", "price": "125.5"}
    ]

    return render_template('shop.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
