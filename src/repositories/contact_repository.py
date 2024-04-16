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

        return [Contact(row["first_name"],
                        row["last_name"],
                        row["email"],
                        row["phone"],
                        row["role"],
                        row["created_at"],
                        row["user"]) for row in rows]


contact_repository = ContactRepository(get_db_connection())
user = user_service.get_current()
contacts = contact_repository.find_all(user.id)
