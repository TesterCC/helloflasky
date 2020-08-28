# coding=utf-8
'''
DATE: 2020/08/28
AUTHOR: Yanxi Li

# P31

python flask_auth
curl http://127.0.0.1:5000/ --user tarek:pass
curl http://127.0.0.1:5000/ -u tester:pass
'''

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def auth():
    print("The raw Authorization header")
    print(request.environ["HTTP_AUTHORIZATION"])
    print("Flask's Authorization header")
    print(request.authorization)
    return ""


if __name__ == '__main__':
    app.run()
