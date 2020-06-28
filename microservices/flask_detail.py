#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/28 10:31'


"""
# P25
python flask_detail.py
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# @app.route("/api")
@app.route("/api",methods=['POST','DELETE',"GET"])
def my_microservice():
    print(request)
    print("=" * 33)
    print(request.environ)
    print("="*33)
    response = jsonify({"Hello": "World!"})
    print(response)
    print(response.data)
    return response

if __name__ == '__main__':
    print(app.url_map)
    app.run()