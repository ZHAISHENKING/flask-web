from flask import Flask, request, make_response, abort
from flask import render_template, session,\
redirect, url_for, flash
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    """
    响应设置cookie
    :return:
    """
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


if __name__ == '__main__':
    manager.run()