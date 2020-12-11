# coding=utf-8
"""
DATE:   2020/12/9
AUTHOR: Yanxi Li

P45

curl http://127.0.0.1:5000/api     500

curl http://127.0.0.1:5000/apis    404

为了应用针对4xx 和 50x 都能返回JSON格式错误，需要将函数注册到每个错误马上
"""

from flask import Flask, jsonify, abort
from werkzeug.exceptions import HTTPException, default_exceptions


def JsonApp(app):
    def error_handling(error):
        if isinstance(error, HTTPException):
            result = {
                'code': error.code,
                'description': error.description,
                'message': str(error)}
        else:
            description = abort.mapping[500].description
            result = {
                'code': 500,
                'description': description,
                'message': str(error)
            }

        resp = jsonify(result)
        resp.status_code = result['code']
        return resp

    for code in default_exceptions.keys():
        app.register_error_handler(code, error_handling)

    return app


# app = Flask(__name__)
app = JsonApp(Flask(__name__))


@app.route('/api')
def my_microservice():
    raise TypeError("Some Exception")


if __name__ == '__main__':
    app.run(debug=True)
