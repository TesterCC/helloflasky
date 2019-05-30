from flask import Flask

app = Flask(__name__)

'''
Flask Web开发--狗书 P10-11
动态路由
'''


@app.route('/user/<name>')    # http://127.0.0.1:5000/user/name
def user(name):
    return '<h1>Welcome to Login, %s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)    # default: debug=None
