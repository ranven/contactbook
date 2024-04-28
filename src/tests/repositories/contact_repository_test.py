import unittest
import uuid
from repositories.contact_repository import contact_repository
from repositories.user_repository import user_repository
from entities.user import User
from entities.contact import Contact


class TestContactRepository(unittest.TestCase):
    def setUp(self):
        users = user_repository.find_all()
        for user in users:
            contact_repository.delete_all(user.id)

        self.user_one = User('one', 'password', "123")
        self.user_two = User('two', 'password', "456")

        self.contact_one = Contact(
            uuid.uuid4().hex, "one", "two", "one@two.com", "050", "test", "", "123")
        self.contact_two = Contact(
            uuid.uuid4().hex, "two", "one", "two@one.com", "040", "tester", "", "123")
        self.contact_three = Contact(
            uuid.uuid4().hex, "three", "th", "three@two.com", "030", "testing", "", "456")

    def test_create(self):
        contact_repository.create(self.contact_one)
        contact = contact_repository.find_one(self.contact_one.id)

        self.assertEqual(contact.id, self.contact_one.id)
        self.assertEqual(contact.first_name, self.contact_one.first_name)
        self.assertEqual(contact.last_name, self.contact_one.last_name)
        self.assertEqual(contact.phone, self.contact_one.phone)
        self.assertEqual(contact.email, self.contact_one.email)
        self.assertEqual(contact.role, self.contact_one.role)
        self.assertEqual(contact.user, self.contact_one.user)

    def test_find_all(self):
        contact_repository.create(self.contact_one)
        contact_repository.create(self.contact_two)
        all_contacts = contact_repository.find_all("123")
        self.assertEqual(len(all_contacts), 2)

    def test_find_one(self):
        contact_repository.create(self.contact_one)
        contact = contact_repository.find_one("1")
        self.assertEqual(len([contact]), 1)

    def test_delete_all(self):
        contact_repository.create(self.contact_one)
        contact_repository.create(self.contact_three)

        contact_repository.delete_all("123")
        all_contacts_one = contact_repository.find_all("123")
        self.assertEqual(len(all_contacts_one), 0)
        all_contacts_two = contact_repository.find_all("456")
        self.assertEqual(len(all_contacts_two), 1)

    def test_delete_one(self):
        contact_repository.create(self.contact_one)
        contact_repository.delete_one(self.user_one.id, self.contact_one.id)
        contact = contact_repository.find_one(self.contact_one.id)
        self.assertEqual(contact, None)
