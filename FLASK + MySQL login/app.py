import os
from flask import Flask, render_template, request, redirect, url_for, session
from pymysql import MySQLError
from werkzeug.security import check_password_hash
from database import Database

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "development-only-change-me")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return redirect(url_for("index"))

    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")
    if not username or not password:
        return render_template("index.html", error="Заполните все поля", username=username), 400

    try:
        user = Database().get_user(username)
        if user and check_password_hash(user["user_password"], password):
            session.clear()
            session["user_id"] = user["id"]
            session["username"] = user["user_name"]
            return redirect(url_for("login_page"))
    except MySQLError:
        app.logger.exception("Ошибка MySQL")
        return render_template("index.html", error="Ошибка подключения к базе данных", username=username), 500

    return render_template("index.html", error="Неверное имя пользователя или пароль", username=username), 401


@app.route("/login_page")
def login_page():
    if "user_id" not in session:
        return redirect(url_for("index"))
    return render_template("login.html", username=session["username"])


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
