# coding=utf-8
'''
DATE: 2020/09/08
AUTHOR: Yanxi Li

ref:
https://gitlab.com/noppo/gevent-websocket

pip install gevent-websocket

gunicorn -k "geventwebsocket.gunicorn.workers.GeventWebSocketWorker" wsgi:websocket_app

'''

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler


def websocket_app(environ, start_response):
    if environ["PATH_INFO"] == '/echo':
        ws = environ["wsgi.websocket"]
        message = ws.receive()
        ws.send(message)


server = pywsgi.WSGIServer(("", 8000), websocket_app,
                           handler_class=WebSocketHandler)
server.serve_forever()
