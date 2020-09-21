# coding=utf-8
'''
DATE: 2020/09/21
AUTHOR: Yanxi Li
Blue Print Simple Demo
'''

from flask import Flask
from microservices.bp.teams import teams   # 注意导入的是teams.py中的teams变量

app = Flask(__name__)

app.register_blueprint(teams)

if __name__ == '__main__':
    app.run()
