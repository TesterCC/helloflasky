# coding=utf-8
'''
DATE: 2020/09/01
AUTHOR: Yanxi Li
'''

# P37-38

from flask import Flask, jsonify, request
import json


class XFFMiddleware:
    def __init__(self, app, real_ip='1.1.1.1'):
        # 1.1.1.1 is a invalid ip, set it just for debug
        self.app = app
        self.real_ip = real_ip

    def __call__(self, environ, start_response):
        if 'HTTP_X_FORWARDED_FOR' not in environ:
            values = '%s, 10.3.4.5, 127.0.0.1' % self.real_ip
            environ['HTTP_X_FORWARDED_FOR'] = values
        return self.app(environ, start_response)


app = Flask(__name__)
app.wsgi_app = XFFMiddleware(app.wsgi_app)

# curl 127.0.0.1:5000/api
@app.route('/api')
def my_microservice():
    if "HTTP_X_FORWARDED_FOR" in request.headers:
        ips = [ip.strip() for ip in request.headers['HTTP_X_FORWARDED_FOR'].split(',')]
        ip = ips[0]
    else:
        ip = request.remote_addr
    return jsonify({"Detect IP address": ip})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
