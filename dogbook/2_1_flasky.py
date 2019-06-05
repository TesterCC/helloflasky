from flask import Flask

app = Flask(__name__)

'''
Flask Web开发--狗书 P8
2-1 Basic Demo
'''

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run(debug=True, port=9898)    # default: debug=None
    # 如果是命令行中运行该文件，优先走9898端口
