from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from database import Database

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-secret-key-before-deployment"
db = Database()


@app.route("/", methods=["GET"])
def index():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", username=session.get("username"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = db.get_user(username)
        if user and check_password_hash(user["user_password"], password):
            session["user_id"] = user["id"]
            session["username"] = user["user_name"]
            return redirect(url_for("index"))

        return render_template("login.html", error="Неверное имя пользователя или пароль.")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            return render_template("register.html", error="Заполните имя пользователя и пароль.")

        if len(username) > 100:
            return render_template("register.html", error="Имя пользователя должно быть не длиннее 100 символов.")

        if len(password) < 6:
            return render_template("register.html", error="Пароль должен содержать не менее 6 символов.")

        if db.get_user(username):
            return render_template("register.html", error="Пользователь с таким именем уже существует.")

        password_hash = generate_password_hash(password)
        user_id = db.create_user(username, password_hash)

        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            return redirect(url_for("profile"))

        return render_template("register.html", error="Не удалось создать пользователя. Попробуйте ещё раз.")

    return render_template("register.html")


@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("profile.html", username=session.get("username"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
