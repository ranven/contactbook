from entities.contact import Contact
from db_connection import get_db_connection
from services.user_service import user_service


class ContactRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self, uid):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM contacts WHERE user = ?", (uid, ))
        rows = cursor.fetchall()

        return [Contact(row["id"],
                        row["first_name"],
                        row["last_name"],
                        row["email"],
                        row["phone"],
                        row["role"],
                        row["created_at"],
                        row["user"]) for row in rows]

    def create(self, contact):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO contacts (id, first_name, last_name, email, phone, role, user) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (contact.id[0], contact.first_name, contact.last_name, contact.email,
             contact.phone, contact.role, contact.user))
        self._connection.commit()
        return contact


contact_repository = ContactRepository(get_db_connection())
user = user_service.get_current()
contacts = contact_repository.find_all(user.id if user else None)