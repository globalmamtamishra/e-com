from db import get_connection

class User:

    @staticmethod
    def create(username, password, email):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            sql = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, password, email))
            connection.commit()
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_id(user_id):
        connection = get_connection()
        try:
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT * FROM users WHERE id = %s"
            cursor.execute(sql, (user_id,))
            user = cursor.fetchone()
            return user
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_all():
        connection = get_connection()
        try:
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            users = cursor.fetchall()
            return users
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update(user_id, username=None, password=None, email=None):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            updates = []
            params = []

            if username:
                updates.append("username = %s")
                params.append(username)
            if password:
                updates.append("password = %s")
                params.append(password)
            if email:
                updates.append("email = %s")
                params.append(email)

            if not updates:
                return False

            params.append(user_id)
            sql = f"UPDATE users SET {', '.join(updates)} WHERE id = %s"
            cursor.execute(sql, tuple(params))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete(user_id):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            sql = "DELETE FROM users WHERE id = %s"
            cursor.execute(sql, (user_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()