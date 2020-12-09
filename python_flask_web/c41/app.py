# coding=utf-8
"""
DATE:   2020/12/9
AUTHOR: Yanxi Li
"""

from flask import Flask, url_for

app = Flask(__name__)

"""
在Flask应用中，路由是指 用户请求的URL 和 视图函数 之间的映射。
Flask将 HTTP请求的URL在路由表中 匹配 预定义的URL规则 ，找到对应的视图函数，将视图函数的执行结果返回给服务器
"""

print("1>>>", app.url_map)

"""
@app.route 将URL和执行的视图函数的关系保存到app.url_map属性上

endpoint参数，给这个URL命名；但是一旦使用了endpoint参数，则在使用 url_for()反转时就不能使用视图函数名，而要用定义的URL名称，如这里的"index"

实际上 @app.route 也是用 add_url_rule() 进行视图函数和URL绑定的
"""
@app.route("/")
def hello_world():
    return "hello world"

print("2>>>", app.url_map)

@app.route("/v2", endpoint="index")
def hello_v2():
    return "hello world2"

with app.test_request_context():
    print(url_for("hello_world"))    # 这里 使用的是视图函数名
    print(url_for("index"))          # 注意，这里就不能使用 url_for("hello_v2") 了。

# 1>>> Map([<Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>])
# 2>>> Map([<Rule '/' (GET, OPTIONS, HEAD) -> hello_world>,


#  当模块被直接运行时，代码将被执行
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="7777", debug=True)