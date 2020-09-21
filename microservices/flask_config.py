# coding=utf-8
'''
DATE: 2020/09/21
AUTHOR: Yanxi Li
'''

# P40 config

from flask import Flask


class Config:
    DEBUG = False
    USER_MODE = "auto"


app = Flask(__name__)
app.config.from_object('microservices.flask_config.Config')  # 注意路径
# app.config.from_json()   # 读取json配置文件
print(app.config)
