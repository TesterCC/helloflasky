#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-01-09 21:37'

import requests

"""
本地和远端都可以用，注意修改IP
"""

SET_WHITE_IP_URL = "http://0.0.0.0:9999/set_white_ip/HDJ_DEVOPS/3.141692653"

GET_WHITE_IP_URL = "http://0.0.0.0:9999/get_white_ip_list"

def set_white_ip():
    response = requests.get(SET_WHITE_IP_URL)
    return response.text

def get_white_ip():
    response = requests.get(GET_WHITE_IP_URL)
    return response.text

if __name__ == '__main__':
    print(set_white_ip())