# coding=utf-8
'''
DATE: 2020/09/21
AUTHOR: Yanxi Li
'''

# P39-40 use Jinja generate email

from datetime import datetime
from jinja2 import Template
from email.utils import format_datetime


def render_email(**data):
    with open('email_template.eml') as f:
        template = Template(f.read())
    return template.render(**data)


data = {
    'date': format_datetime(datetime.now()),
    'to': 'testerlyx@foxmail.com',
    'from': 'test@fullstackpentest.com',
    'subject': 'Test Flask Jinja2 Template by Email',
    'name': 'TesterCC',
    'items': [
        {'name': 'Fluent Python', 'price': 29.99},
        {'name': 'Python Cookbook', 'price': 18.78},
        {'name': 'Go in Action', 'price': 11.54},
    ]
}

if __name__ == '__main__':
    print(render_email(**data))