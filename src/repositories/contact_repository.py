from entities.contact import Contact
from db_connection import get_db_connection
from services.user_service import user_service


class ContactRepository:
    """Luokka joka vastaa kontakteihin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args: 
            connection: tietokantayhteyden connection-olio
        """

        self._connection = connection

    def find_all(self, user_id):
        """Palauttaa kaikki käyttäjän luomat kontaktit.

        Args:
            user_id: käyttäjän id

        Returns:
            Palauttaa listan Contact-olioita

        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM contacts WHERE user = ?", (user_id, ))
        rows = cursor.fetchall()

        return [Contact(row["id"],
                        row["first_name"],
                        row["last_name"],
                        row["email"],
                        row["phone"],
                        row["role"],
                        row["created_at"],
                        row["user"]) for row in rows]

    def find_one(self, contact_id):
        """Palauttaa kontaktin annetun id'n perusteella.

        Args:
            contact_id: haettavan kontaktin id

        Returns:
            Palauttaa Contact-olion mikäli kontakti löytyy, muuten palauttaa None

        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id, ))
        row = cursor.fetchone()

        return Contact(row["id"],
                       row["first_name"],
                       row["last_name"],
                       row["email"],
                       row["phone"],
                       row["role"],
                       row["created_at"],
                       row["user"]) if row else None

    def delete_all(self, user_id):
        """Poistaa kaikki käyttäjän luomat kontaktit.

        Args:
            user_id: käyttäjän id, jonka luomat kontaktit poistetaan

        """

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM contacts WHERE user = ?", (user_id, ))
        self._connection.commit()

    def delete_one(self, user_id, contact_id):
        """Poistaa yhden kontaktin annetun id'n perusteella.

        Args:
            user_id: käyttäjän id, jonka luoma kontakti poistetaan
            contact_id: poistettavan kontaktin id 
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "DELETE FROM contacts WHERE id = ? AND user = ?", (contact_id, user_id, ))
        self._connection.commit()

    def create(self, contact):
        """Luo uuden kontaktin.

        Args:
            contact: tallennettava kontakti Contact-oliona

        Returns:
            Palauttaa luodun kontaktin Contact-oliona.

        """
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO contacts (id, first_name, last_name, email, phone, role, user)"
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (contact.id, contact.first_name, contact.last_name, contact.email,
             contact.phone, contact.role, contact.user))
        self._connection.commit()
        return contact


contact_repository = ContactRepository(get_db_connection())
user = user_service.get_current_user()
contacts = contact_repository.find_all(user.id if user else None)
