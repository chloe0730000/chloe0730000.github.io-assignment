# session guide: https://www.youtube.com/watch?v=iIhAfX4iek0
# javascript flask course: https://www.udemy.com/course/javascript-es6-react-redux/

from flask import Flask, request, redirect, render_template, session
import json


app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/static")
app.secret_key = "test123"  # for session


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/signin", methods=["POST", "GET"])
def validate_pass():
    if request.method == "POST":
        user = request.form["account"]
        pw = request.form["pass"]

        session["user"] = user

        if user == "test" and pw == "test":
            return redirect("/member/")
        else:
            return redirect("/error/")


@app.route("/error/")
def error_page():
    return render_template("fail.html")


@app.route("/member/")
def success_page():
    if "user" in session:
        user = session["user"]
        print(f"{user} 已登入")
        return render_template("success.html")
    else:
        return render_template("login.html")


@app.route("/signout")
def signout():
    session.pop("user", None)
    print("未登入")
    return render_template("login.html")


app.run(port=3000)
