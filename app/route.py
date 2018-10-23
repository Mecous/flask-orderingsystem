from flask import Flask
from flask import render_template,redirect,url_for,request
from forms import LoginForm,RegisterForm
from . import app

#视图函数
#登录
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',form = form)


#注册
@app.route("/register")
def regist():
    from = RegisterForm()
    return redirect(url_for())