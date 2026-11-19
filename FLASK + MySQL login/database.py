import os
import pymysql
from pymysql.cursors import DictCursor


class Database:
    def __init__(self):
        self.config = {
            "host": os.getenv("DB_HOST", "localhost"),
            "user": os.getenv("DB_USER", "root"),
            "password": os.getenv("DB_PASSWORD", ""),
            "database": os.getenv("DB_NAME", "flask_auth"),
            "charset": "utf8mb4",
            "cursorclass": DictCursor,
        }

    def get_user(self, username):
        connection = pymysql.connect(**self.config)
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, user_name, user_password FROM users WHERE user_name = %s",
                    (username,),
                )
                return cursor.fetchone()
        finally:
            connection.close()
