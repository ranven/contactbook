import uuid
from repositories.contact_repository import contact_repository
from entities.contact import Contact
from services.user_service import user_service


class NoUserError(Exception):
    pass


class ContactService:
    def __init__(
            self,
            contact_repo=contact_repository):
        self._contact_repository = contact_repo
        self.contacts = None

    def get_contacts(self, user_id):
        if user_id is None:
            raise NoUserError("No user is logged in.")
        return self._contact_repository.find_all(user_id)

    def create_contact(self, first_name, last_name, email, phone, role, user_id):
        if user_id is None:
            raise NoUserError("No user is logged in.")

        new_contact = Contact(
            contact_id=uuid.uuid4().hex,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            role=role,
            created_at=None,
            user=user_id)

        return self._contact_repository.create(new_contact)

    def delete_all(self, user_id):
        if user_id is None:
            raise NoUserError("No user is logged in.")

        return self._contact_repository.delete_all(user_id)


contact_service = ContactService()
