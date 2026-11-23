# Flask + MySQL — регистрация пользователя

Готовый учебный проект по заданию с изображения. Реализованы маршруты `GET /register` и `POST /register`, добавление пользователя через PyMySQL, сессия, страница профиля и обработка ошибок.

## Состав проекта

- `app.py` — Flask-приложение: регистрация, вход, профиль, выход.
- `database.py` — методы `create_user()` и `get_user()` для MySQL.
- `schema.sql` — создание базы и таблицы `users`.
- `templates/` — HTML-страницы `register.html`, `login.html`, `profile.html`, `index.html`.
- `static/style.css` — оформление.
- `requirements.txt` — зависимости.

## Установка и запуск

Требуются Python 3.10+ и запущенный MySQL Server.

1. Создайте базу и таблицу, выполнив `schema.sql` в MySQL Workbench.
2. В терминале перейдите в папку проекта и установите зависимости:

   ```bash
   python -m venv .venv
   # Windows:
   .venv\\Scripts\\activate
   # macOS/Linux:
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Задайте параметры подключения к MySQL через переменные окружения. Например, в PowerShell:

   ```powershell
   $env:DB_HOST="localhost"
   $env:DB_PORT="3306"
   $env:DB_USER="root"
   $env:DB_PASSWORD="ваш_пароль"
   $env:DB_NAME="flask_users"
   ```

4. Запустите приложение:

   ```bash
   python app.py
   ```

5. Откройте `http://127.0.0.1:5000/register`.

## Проверка задания

- `GET /register` отображает форму регистрации.
- `POST /register` принимает `username` и `password` из `request.form`.
- Пустые поля и слишком короткий пароль отклоняются.
- Повторное имя пользователя вызывает сообщение об ошибке и повторный показ `register.html`.
- `Database.create_user()` выполняет параметризованный `INSERT INTO users (user_name, user_password) VALUES (%s, %s)` и вызывает `commit()`.
- При успешной регистрации ID и имя сохраняются в `session`, затем открывается `profile.html`.
- После регистрации можно выйти и проверить вход через `/login`.

## Важное замечание о паролях

Вместо хранения пароля в открытом виде приложение сохраняет хеш, созданный `generate_password_hash()`. При входе используется `check_password_hash()`. Это безопаснее, чем записывать исходный пароль в базу.

Перед реальным развёртыванием замените `SECRET_KEY` в `app.py` на секретное значение из переменной окружения и отключите `debug=True`.
