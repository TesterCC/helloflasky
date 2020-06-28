#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/28 10:31'


"""
# P23-24
python flask_basic.py
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api")
def my_microservice():
    return jsonify({"Hello": "World!"})

if __name__ == '__main__':
    app.run()