from entities.contact import Contact
from db_connection import get_db_connection


class ContactRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()

        return [Contact(row["first_name"],
                        row["last_name"],
                        row["email"],
                        row["phone"],
                        row["role"]) for row in rows]


contact_repository = ContactRepository(get_db_connection())
contacts = contact_repository.find_all()
