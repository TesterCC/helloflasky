from flask import Flask
from flask import request

'''
Flask Web开发--狗书 P12
动态路由
'''

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your broser is %s</p>' % user_agent

# Falsk 使用上下文让特定的变量在一个线程中全局 可访问,与此同时却不会干扰其他线程。

if __name__ == '__main__':
    app.run(debug=True)    # default: debug=None

