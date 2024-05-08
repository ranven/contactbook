import unittest
import uuid
from entities.user import User
from services.contact_service import ContactService, NoUserError, PhoneNumberError, ContactCreationError


class FakeUser:
    def __init__(self, uid):
        self.id = uid


class FakeContactRepository:
    def __init__(self):
        self.contacts = []

    def create(self, contact):
        contact.id = uuid.uuid4().hex
        self.contacts.append(contact)
        return contact

    def find_all(self, user_id):
        return [contact for contact in self.contacts if contact.user == user_id]

    def delete_all(self, user_id):
        self.contacts = [
            contact for contact in self.contacts if contact.user != user_id]

    def delete_one(self, user_id, contact_id):
        self.contacts = [
            contact for contact in self.contacts if not (contact.user == user_id and contact.id == contact_id)]


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

    def test_get_all_contacts(self):
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

    def test_create_contact_with_incorrect_phone_number(self):
        user = User('testusername', 'testpassword', '123')

        with self.assertRaises(PhoneNumberError):
            self.contact_service.create_contact(
                'Pekka', 'Pouta', 'pekka@pouta.fi', 'not a numerical value', 'Meteorologi', user.id)

        contacts = self.contact_service.get_contacts(user.id)
        self.assertEqual(len(contacts), 0)

    def test_create_contact_with_too_long_input(self):
        user = User('testusername', 'testpassword', '123')

        with self.assertRaises(ContactCreationError):
            self.contact_service.create_contact(
                'Pekka', 'Pouta', 'pekka@pouta.fi', '123456789', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean commodo ligula eget dolor', user.id)

        contacts = self.contact_service.get_contacts(user.id)
        self.assertEqual(len(contacts), 0)

    def test_delete_all_contacts(self):
        user = User('testusername', 'testpassword', '123')
        self.contact_service.create_contact(
            'Pekka', 'Pouta', 'pekka@pouta.fi', '123456789', 'Meteorologi', user.id)
        self.contact_service.create_contact(
            'Ville', 'Valo', 'ville@valo.fi', '987654321', 'Muusikko', user.id)

        self.contact_service.delete_all_contacts(user.id)
        contacts = self.contact_service.get_contacts(user.id)
        self.assertEqual(len(contacts), 0)

    def test_delete_one_contact(self):
        user = User('testusername', 'testpassword', '123')
        contact = self.contact_service.create_contact(
            'Pekka', 'Pouta', 'pekka@pouta.fi', '123456789', 'Meteorologi', user.id)

        self.contact_service.delete_one_contact(user.id, contact.id)

        contacts = self.contact_service.get_contacts(user.id)
        self.assertEqual(len(contacts), 0)

    def test_create_contact_without_user(self):
        with self.assertRaises(NoUserError):
            self.contact_service.create_contact(
                'Pekka', 'Pouta', 'pekka@pouta.fi', '123456789', 'Meteorologi', None)

    def test_delete_all_contacts_without_user(self):
        with self.assertRaises(NoUserError):
            self.contact_service.delete_all_contacts(None)

    def test_delete_one_contact_without_user(self):
        with self.assertRaises(NoUserError):
            self.contact_service.delete_one_contact(None, "1")

    def test_get_all_contacts_without_user(self):
        with self.assertRaises(NoUserError):
            self.contact_service.get_contacts(None)
