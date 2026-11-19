import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="flask_auth",
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_user(self, username):
        try:
            with self.connection.cursor() as cursor:
                sql = """
                    SELECT * FROM users
                    WHERE user_name = %s
                """
                cursor.execute(sql, (username,))
                return cursor.fetchone()
        finally:
            self.connection.close()
