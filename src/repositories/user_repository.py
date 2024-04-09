from ..entities.user import User
from ..db_connection import get_db_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        return [User(row["username"], row["password"]) for row in rows]

    def find_one(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username, ))
        row = cursor.fetchone()

        return User(row["username"], row["password"]) if row else None

    def create(self, user):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (user.username, user.password))
        self._connection.commit()
        return user


user_repository = UserRepository(get_db_connection())
users = user_repository.find_all()