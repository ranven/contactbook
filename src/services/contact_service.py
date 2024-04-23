import uuid
from repositories.contact_repository import contact_repository
from entities.contact import Contact
from services.user_service import user_service


class ContactService:
    def __init__(
            self,
            contact_repo=contact_repository):
        self._contact_repository = contact_repo
        self.contacts = None

    def get_contacts(self):
        user = user_service.get_current()
        return self._contact_repository.find_all(user.id)

    def create_contact(self, first_name, last_name, email, phone, role):
        user = user_service.get_current()
        new_contact = Contact(
            contact_id=uuid.uuid4().hex,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            role=role,
            created_at=None,
            user=user.id)

        return self._contact_repository.create(new_contact)

    def delete_all(self):
        user = user_service.get_current()
        return self._contact_repository.delete_all(user.id)


contact_service = ContactService()
