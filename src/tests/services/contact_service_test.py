import unittest
import uuid
from entities.user import User
from services.contact_service import ContactService, NoUserError
from entities.contact import Contact
from services.user_service import UserService


class FakeUser:
    def __init__(self, uid):
        self.id = uid


class FakeContactRepository:
    def __init__(self):
        self.contacts = []

    def create(self, contact):
        self.contacts.append(contact)

    def find_all(self, user_id):
        return [contact for contact in self.contacts if contact.user == user_id]

    def delete_all(self, user_id):
        self.contacts = [
            contact for contact in self.contacts if contact.user != user_id]


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_all(self):
        return self.users

    def find_one(self, username):
        matching_users = filter(
            lambda user: user.username == username, self.users)
        matching_users_list = list(matching_users)
        return matching_users_list[0] if len(matching_users_list) > 0 else None

    def create(self, user):
        self.users.append(user)
        return user

    def delete_all(self):
        self.users = []


class TestContactService(unittest.TestCase):
    def setUp(self):
        self.contact_repo = FakeContactRepository()
        self.contact_service = ContactService(contact_repo=self.contact_repo)

    def test_get_contacts(self):
        user = User('testusername', 'testpassword', '123')

        self.contact_service.create_contact(
            'Pekka', 'Pouta', 'pekka@pouta.fi', '123456789', 'Meteorologi', user.id)
        self.contact_service.create_contact(
            'Ville', 'Valo', 'ville@valo.fi', '987654321', 'Muusikko', user.id)

        contacts = self.contact_service.get_contacts(user.id)
        self.assertEqual(len(contacts), 2)

    def test_create_contact(self):
        user = User('testusername', 'testpassword', '123')
        self.contact_service.create_contact(
            'Pekka', 'Pouta', 'pekka@pouta.fi', '123456789', 'Meteorologi', user.id)
        self.contact_service.create_contact(
            'Ville', 'Valo', 'ville@valo.fi', '987654321', 'Muusikko', user.id)

        contacts = self.contact_service.get_contacts(user.id)
        self.assertEqual(len(contacts), 2)

    def test_delete_all(self):
        user = User('testusername', 'testpassword', '123')
        self.contact_service.create_contact(
            'Pekka', 'Pouta', 'pekka@pouta.fi', '123456789', 'Meteorologi', user.id)
        self.contact_service.create_contact(
            'Ville', 'Valo', 'ville@valo.fi', '987654321', 'Muusikko', user.id)

        self.contact_service.delete_all(user.id)
        contacts = self.contact_service.get_contacts(user.id)
        self.assertEqual(len(contacts), 0)

    def test_create_contact_without_user(self):
        with self.assertRaises(NoUserError):
            self.contact_service.create_contact(
                'Pekka', 'Pouta', 'pekka@pouta.fi', '123456789', 'Meteorologi', None)

    def test_delete_all_without_user(self):
        with self.assertRaises(NoUserError):
            self.contact_service.delete_all(None)

    def test_get_contacts_without_user(self):
        with self.assertRaises(NoUserError):
            self.contact_service.get_contacts(None)