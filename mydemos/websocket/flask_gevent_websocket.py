# coding=utf-8
'''
DATE: 2020/09/08
AUTHOR: Yanxi Li

ref: error
https://www.cnblogs.com/jayxuan/p/11385240.html
'''

from flask import Flask, request, abort
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket  # 语法提示

app = Flask(__name__)


@app.route("/conn")
def index():
    # 获取请求原始数据
    user_socket = request.environ
    print("print environ: \n{}".format(user_socket))
    # 获取Websocket对象
    #websocket_obj = user_socket['wsgi.websocket']  # FIXME KeyError: 'wsgi.websocket'
    websocket_obj = request.environ.get('wsgi.websocket')

    if not websocket_obj:
        abort(400, 'Expected WebSocket request.')

    while True:  # 循环监听
        # 监听链接，接收数据
        msg = websocket_obj.receive()
        print(msg)
        websocket_obj.send(msg + 'to you')


if __name__ == '__main__':
    # app.run()
    # 在APP外封装websocket
    http_serve = WSGIServer(("0.0.0.0", 5000), app, handler_class=WebSocketHandler)

    # 启动服务
    http_serve.serve_forever()
