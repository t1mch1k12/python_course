import os
import pymysql
from pymysql.cursors import DictCursor


class Database:
    """Небольшой слой доступа к MySQL через PyMySQL."""

    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = int(os.getenv("DB_PORT", "3306"))
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")
        self.database = os.getenv("DB_NAME", "flask_users")

    def _connect(self):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset="utf8mb4",
            cursorclass=DictCursor,
            autocommit=False,
        )

    def create_user(self, name, password_hash):
        """Добавляет пользователя и возвращает его ID; при ошибке — None."""
        connection = self._connect()
        try:
            with connection.cursor() as cur:
                cur.execute(
                    "INSERT INTO users (user_name, user_password) VALUES (%s, %s)",
                    (name, password_hash),
                )
                connection.commit()
                return cur.lastrowid
        except pymysql.err.IntegrityError:
            connection.rollback()
            return None
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def get_user(self, name):
        connection = self._connect()
        try:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT id, user_name, user_password FROM users WHERE user_name = %s",
                    (name,),
                )
                return cur.fetchone()
        finally:
            connection.close()
