from repositories.contact_repository import contact_repository
from entities.contact import Contact


class ContactService:
    def __init__(
            self,
            contact_repo=contact_repository):
        self._contact_repository = contact_repo

    def get_users(self):
        return self._contact_repository.find_all()


contact_service = ContactService()
