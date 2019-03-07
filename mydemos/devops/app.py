#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/10/18 15:33'

"""
DevOps(Simple)

需求：
1.访问是需要先认证
2.认证后GET请求一个接口，将外网IP写入white.txt
3.要判断txt中内容不能大于N行，以便控制白名单数量
"""
import os

from flask import Flask
from flask import request, abort, make_response

app = Flask(__name__)

"""
Flask Web开发  dog book P46
2.8.1 应用请求和上下文
"""


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your Browser/User-Agent is <h3>{}</h3></p>'.format(user_agent)


@app.route('/get_public_ip')
def get_public_ip():
    ip = request.remote_addr
    return '<p>Your Public IP is : <h3>{}</h3></p>'.format(ip)


@app.route('/get_white_ip_list')
def get_white_ip_list():
    base_dir = os.path.dirname(__file__)
    print(base_dir)
    target_path = base_dir + "/" + "white_ip_list.txt"
    print(target_path)

    with open(target_path, 'r') as f:
        white_ips = f.read()

    response = make_response(white_ips)
    response.headers["Content-type"] = "text/plan;charset=UTF-8"

    return response


@app.route('/set_white_ip/<user_name>/<auth_code>')
def set_white_ip(user_name, auth_code):
    """
    http://0.0.0.0:9999/set_white_ip/HDJ_DEVOPS/3.141692653
    :param user_name:
    :param auth_code:
    :return:
    """
    if user_name == 'HDJ_DEVOPS' and auth_code == '3.141692653':
        print("Login to set white ip list...")
        base_dir = os.path.dirname(__file__)
        print(base_dir)
        target_path = base_dir + "/" + "white_ip_list.txt"

        # target_path = "/Users/TesterCC/Development/workspace_flask/helloflasky/mydemos/devops/white_ip_list.txt"
        print(target_path)

        public_ip = request.remote_addr

        with open(target_path, 'rU') as fc:
            count = len(fc.readlines())  # 文件行数 int

        if count == 0 or count > 2:
            os.system("echo '{}' > {}".format(public_ip, target_path))  # coverage
        elif 0 < count <= 2:
            # FIXME issue:第3次访问总要多写入一次相同的IP，以后debug下
            with open(target_path, 'r') as flist:
                white_ips_lines = flist.readlines()
                print(white_ips_lines)

            for white_ip in white_ips_lines:
                if public_ip.strip() != white_ip.strip():
                    os.system("echo '{}' >> {}".format(public_ip, target_path))  # add to
        else:
            print("Count error!")

        with open(target_path, 'r') as f:
            white_ips = f.read()

        response = make_response(white_ips)
        response.headers["Content-type"] = "text/plan;charset=UTF-8"

        return response

    else:
        print("Auth error!")
        abort(400)


if __name__ == '__main__':
    app.run(debug=False, port=9999)  # default: debug=None
