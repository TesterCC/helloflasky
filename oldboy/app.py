# coding=utf-8
'''
DATE: 2020/09/02
AUTHOR: Yanxi Li
'''

# ref:
# https://www.cnblogs.com/DragonFire/p/9259999.html
# https://www.cnblogs.com/DragonFire/

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/allstudent")
def all_student():
    STUDENT = {'name': 'Alice', 'age': 38, 'gender': '中'},

    STUDENT_LIST = [
        {'name': 'Alice', 'age': 38, 'gender': '中'},
        {'name': 'Bob', 'age': 73, 'gender': '男'},
        {'name': 'Chris', 'age': 84, 'gender': '女'}
    ]

    STUDENT_DICT = {
        1: {'name': 'Alice', 'age': 38, 'gender': '中'},
        2: {'name': 'Bob', 'age': 73, 'gender': '男'},
        3: {'name': 'Chris', 'age': 84, 'gender': '女'},
    }

    return render_template("all_student.html", **{"student": STUDENT,
                                                  "student_list": STUDENT_LIST,
                                                  "student_dict": STUDENT_DICT})


if __name__ == '__main__':
    app.run(debug=True)
