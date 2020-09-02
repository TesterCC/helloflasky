# coding=utf-8
'''
DATE: 2020/09/02
AUTHOR: Yanxi Li
'''

# Python Flask Web开发入门与项目实战
#  curl http://127.0.0.1:7777/rand

from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/rand")
def get_rand():
    rand_num = random.randint(0, 1)
    return render_template('index.html', name=rand_num)


#  当模块被直接运行时，代码将被执行
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="7777", debug=True)
