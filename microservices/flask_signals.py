# coding=utf-8
'''
DATE: 2020/08/31
AUTHOR: Yanxi Li

P36 事件是blinker.signal类的实例，被创建时有一个唯一标签
注册特定事件，调用connect方法
当代码调用了信号的send方法时，会触发信号
'''

from flask import Flask, jsonify, g, request_finished
from flask.signals import signals_available

if not signals_available:
    raise RuntimeError("pip install blinker")

app = Flask(__name__)


def finished(sender, response, **extra):
    print("About to send a Response")
    print(response)


# register event
request_finished.connect(finished)


@app.route('/api')
def my_microservice():
    return jsonify({"Hello": 'Flask'})


if __name__ == '__main__':
    app.run()
