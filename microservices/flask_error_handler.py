# coding=utf-8
"""
DATE:   2020/12/9
AUTHOR: Yanxi Li

P44

curl http://127.0.0.1:5000/api     500

curl http://127.0.0.1:5000/apis    404
"""

from flask import Flask, jsonify

app = Flask(__name__)

# 500时，返回JSON格式错误
@app.errorhandler(500)
def error_handling(error):
    return jsonify({'Error': str(error)},500)

@app.route('/api')
def my_microservice():
    raise TypeError("Some Test Exception")

if __name__ == '__main__':
    app.run()