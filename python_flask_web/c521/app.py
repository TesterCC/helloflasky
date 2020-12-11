# coding=utf-8
"""
DATE:   2020/12/10
AUTHOR: Yanxi Li
"""
# 5.2.1 使用Flask上传文件的简单实现

import hashlib
import os
from os import path
import platform
import random
import sys
import time
import traceback

from flask import Flask,render_template,request,jsonify

rand_str = "abcdefghijklmnopqrstuvwxyz0123456789"

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024

# print(f'[+] platform system: {platform.system()}')

# 兼容 windows和linux，其实一般都是部署在 Linux 上
# slash = ''
# if platform.system() == 'Windows':
#     slash='\\'
# elif platform.system() == 'Linux':
#     slash = '/'

UPLOAD_PATH = os.path.curdir + '/static/'
# print(f"[+] upload path is {UPLOAD_PATH}")

def check_upload_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST','GET'])
def upload():
    data, code, err = None, 0, None

    if request.method == 'GET':
        return render_template('upload.html')
    else:

        # 没有目录就创建目录
        if not os.path.exists(UPLOAD_PATH):
            os.makedirs(UPLOAD_PATH)

        f = request.files['file']                # get file stream

        if f and check_upload_file(f.filename):
            # 统一处理上传文件名
            # 可以使用 用户名+时间戳 的md5值 作为文件名
            # 可以使用 时间戳的md5值 + N位随机字符 作为文件名
            # print("file: ", f)
            ext = f.filename.rsplit('.', 1)[1]  # get suffix

            filename = hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()[:13] + "".join(
                random.sample(rand_str, 2)) + '.' + ext

            f.save(path.join('static',filename))     # Noted: 指定一级目录，可减少处理slash的逻辑
            code = 1
            err = 'upload success'

        else:
            err = 'There is some error.'

        return jsonify({
            'code':code,
            'msg':err,
            'data': data
        })

if __name__ == '__main__':
    app.run(debug=True)