from getpass import getpass
from werkzeug.security import generate_password_hash
import pymysql
from database import Database

username = input("Имя пользователя: ").strip()
password = getpass("Пароль: ")
if not username or not password:
    raise SystemExit("Имя и пароль не должны быть пустыми")
if len(username) > 64:
    raise SystemExit("Имя пользователя слишком длинное")

connection = pymysql.connect(**Database().config)
try:
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (user_name, user_password) VALUES (%s, %s)",
            (username, generate_password_hash(password)),
        )
    connection.commit()
    print("Пользователь создан")
except pymysql.IntegrityError:
    print("Пользователь с таким именем уже существует")
finally:
    connection.close()
