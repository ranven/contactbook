from entities.user import User
from db_connection import get_db_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        return [User(row["username"], row["password"], row["id"]) for row in rows]

    def find_one(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username, ))
        row = cursor.fetchone()

        return User(row["username"], row["password"], row["id"]) if row else None

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()

    def create(self, user):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (id, username, password) VALUES (?, ?, ?)",
                       (user.id, user.username, user.password))
        self._connection.commit()
        return user


user_repository = UserRepository(get_db_connection())
users = user_repository.find_all()
