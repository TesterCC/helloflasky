# coding=utf-8
"""
DATE:   2020/12/10
AUTHOR: Yanxi Li
"""
# 5.2.1 使用Flask上传文件的简单实现

import hashlib
import os
import platform
import random
import sys
import time
import traceback

import uuid

from flask import Flask, render_template, request, jsonify

# rand_str = "abcdefghijklmnopqrstuvwxyz0123456789"

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

# print(f'[+] platform system: {platform.system()}')

# 兼容 windows和linux，其实一般都是部署在 Linux 上
# slash = ''
# if platform.system() == 'Windows':
#     slash='\\'
# elif platform.system() == 'Linux':
#     slash = '/'

DIR_PATH = 'static/upload/'
UPLOAD_PATH = os.path.curdir + DIR_PATH
# print(os.path.curdir)  # .
print(f"[+] upload path is {UPLOAD_PATH}")


def check_upload_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    data, code, err = None, 0, None

    if request.method == 'GET':
        return render_template('upload.html')
    else:

        # 没有指定的DIR_PATH目录就创建目录
        if not os.path.exists(DIR_PATH):
            os.makedirs(DIR_PATH)

        f = request.files['file']  # get file stream
        # print(f.headers)
        print(f.content_type)
        # print(f.content_length)  # 前端不传的话就是0
        size = len(f.read())  # 文件指针会指到最后读取内容
        f.seek(0)  # 重新定义指针的文件开头，不然save()会保存为空。
        convert_size = size / 1024 / 1024
        # print(convert_size)   # 单位是M
        # print(size)  #  float, 单位是字节 byte, 1M = 1024 KB = 1024 * 1024 Byte = 1024 * 1024 * 8 bit
        if convert_size > 2:
            code, err = 99, '文件超出最大限制'

        else:
            if f and check_upload_file(f.filename):
                # 注意：自行统一处理上传文件名
                # 可以使用 用户名+时间戳 的md5值 作为文件名
                # 可以使用 时间戳的md5值 + N位随机字符 作为文件名
                # print("file: ", f)

                # # method 1：don't recommend
                # ext = f.filename.rsplit('.', 1)[1]  # get suffix
                #
                # # 用python内置的uuid模块生成随机文件名的random_filename()函数
                # filename = hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()[:13] + "".join(
                #     random.sample(rand_str, 2)) + '.' + ext

                # method 2:
                filename = random_filename(f.filename)
                print(filename)

                f.save(os.path.join(DIR_PATH, filename))  # Noted: DIR_PATH 注意slash位置
                print(
                    DIR_PATH + filename)  # url path ： http://127.0.0.1:5000/static/upload/1ec04f8610b44bcd85a89c86aaa7bac8.png

                code = 1
                err = 'upload success'

            else:
                code, err = 99, 'invalid file'

        return jsonify({
            'code': code,
            'msg': err,
            'data': data
        })


if __name__ == '__main__':
    app.run(debug=True)
