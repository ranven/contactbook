from entities.user import User
from db_connection import get_db_connection


class UserRepository:
    """Luokka joka vastaa käyttäjiin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args: 
            connection: tietokantayhteyden connection-olio
        """

        self._connection = connection

    def find_all(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            Palauttaa listan User-olioita
        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        return [User(row["username"], row["password"], row["id"]) for row in rows]

    def find_one(self, username):
        """Palauttaa käyttäjän annetun käyttäjänimen perusteella.

        Args:
            username: haettavan käyttäjän käyttäjänimi

        Returns:
            Palauttaa User-olion mikäli käyttäjä löytyy, muuten palauttaa None

        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username, ))
        row = cursor.fetchone()

        return User(row["username"], row["password"], row["id"]) if row else None

    def delete_all(self):
        """Poistaa kaikki käyttäjät. 
        """

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()

    def create(self, user):
        """Luo uuden käyttäjän.

        Args:
            user: tallennettava kontakti User-oliona

        Returns:
            Palauttaa luodun käyttäjän User-oliona.

        """

        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (id, username, password) VALUES (?, ?, ?)",
                       (user.id, user.username, user.password))
        self._connection.commit()
        return user


user_repository = UserRepository(get_db_connection())
users = user_repository.find_all()
