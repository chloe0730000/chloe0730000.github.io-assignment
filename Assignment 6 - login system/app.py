# session guide: https://www.youtube.com/watch?v=iIhAfX4iek0
# javascript flask course: https://www.udemy.com/course/javascript-es6-react-redux/
# mysql: https://pynative.com/python-mysql-database-connection/
# use this in terminal before connecting mysql db using python => GRANT SELECT ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
# ref: https://codeshack.io/login-system-python-flask-mysql/


from flask import Flask, request, redirect, render_template, session, url_for
import json
from mysql.connector import connect, Error

# connect with local mysql database
try:
    db_connection = connect(
        host= "localhost",
        user= "root",
        password= "abcd", # need to change
        database="website")
    print(db_connection)
except Error as e:
    print(e)


app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/static")
app.secret_key = "test123"  # for session


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/signup", methods=["POST", "GET"])
def validate_pass():
    if request.method == "POST":
        username = str(request.form["re_name"])
        useraccount = str(request.form["re_account"])
        pw = str(request.form["re_pass"])

        db_cursor = db_connection.cursor()
        sql = "select * from user where username='"+useraccount+"'"
        db_cursor.execute(sql)
        res = db_cursor.fetchall()


        if len(res)>0:
            err_msg = "帳號已經被註冊"
            return redirect(url_for("error_page", message=err_msg))
        else:
            sql_insert = "insert into user (name, username ,password) values ('" + username+"','"+ useraccount+"','"+pw+"')"
            db_cursor.execute(sql_insert)
            db_connection.commit()
            return redirect(url_for("index"))




@app.route("/signin", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        useraccount = str(request.form["account"])
        pw = str(request.form["pass"])

        db_cursor = db_connection.cursor(buffered=True , dictionary=True) # to get res['name']
        sql = "select * from user where username='"+useraccount+ "' and password = '" + pw+"'"
        db_cursor.execute(sql)
        res = db_cursor.fetchone()
        print(res)

        try:
             if len(res)>0:
                session["user"] = res['name']
                return redirect(url_for("success_page"))
        except:
            return redirect(url_for('error_page', message="帳號或密碼輸入錯誤"))


 


@app.route("/member/")
def success_page():
    if "user" not in session:
        return render_template("login.html")
    else: 
        return render_template("member.html", welcome_name=session["user"])


@app.route("/error/")
def error_page():
    err_msg = request.args.get("message", "帳號或密碼輸入錯誤")
    return render_template("fail.html", error_message=err_msg)


@app.route("/signout")
def signout():
    session.pop("user", None)
    print("未登入")
    return render_template("login.html")


app.run(port=3000)
