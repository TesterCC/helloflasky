# coding=utf-8
'''
DATE: 2020/09/08
AUTHOR: Yanxi Li

ref:
https://gitlab.com/noppo/gevent-websocket

pip install gevent-websocket

gunicorn -k "geventwebsocket.gunicorn.workers.GeventWebSocketWorker" wsgi:websocket_app
'''

from geventwebsocket import WebSocketServer, WebSocketApplication, Resource
from collections import OrderedDict


class EchoApplication(WebSocketApplication):
    def on_open(self):
        print("Connection opened")

    def on_message(self, message):
        self.ws.send(message)

    def on_close(self, reason):
        print(reason)


WebSocketServer(
    ('', 8000),
    Resource(OrderedDict([('/', EchoApplication)]))
).serve_forever()
