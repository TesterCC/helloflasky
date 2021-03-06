# coding=utf-8
'''
DATE: 2020/09/21
AUTHOR: Yanxi Li
'''

# P42-43 Blueprint

"""
curl http://127.0.0.1:5000/teams/
curl http://127.0.0.1:5000/teams/1
curl http://127.0.0.1:5000/test/
"""

from flask import Blueprint, jsonify

teams = Blueprint('teams', __name__)

_DEVS = ['Eric', 'Lily']
_OPS = ['Bill']
_TEAMS = {1: _DEVS, 2: _OPS}


@teams.route('/teams/')
def get_all():
    return jsonify(_TEAMS)


@teams.route('/teams/<int:team_id>')
def get_team(team_id):
    return jsonify(_TEAMS[team_id])


@teams.route('/test/')
def get_test():
    content = {
        "code": 1,
        "msg": "success",
        "data": None
    }
    return jsonify(content)
