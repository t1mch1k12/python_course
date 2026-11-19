from flask import Flask, request, redirect, render_template_string
from database import Database

app = Flask(__name__)


@app.route("/")
def index():
    return render_template_string("""
        <h2>Авторизация</h2>
        <form action="/login" method="POST">
            <input type="text" name="username"
                   placeholder="Логин" required>
            <br><br>
            <input type="password" name="password"
                   placeholder="Пароль" required>
            <br><br>
            <button type="submit">Войти</button>
        </form>
    """)


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    try:
        db = Database()
        user = db.get_user(username)

        if user and user["user_password"] == password:
            return redirect("/success")

        return "Неверный логин или пароль", 401

    except Exception:
        app.logger.exception("Ошибка базы данных")
        return "Ошибка подключения к базе данных", 500


@app.route("/success")
def success():
    return "Авторизация прошла успешно!"


if __name__ == "__main__":
    app.run(debug=True)
