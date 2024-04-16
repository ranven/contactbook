import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_one = User('one', 'password', "123")
        self.user_two = User('two', 'password', "456")

    def test_create(self):
        user_repository.create(self.user_one)
        user = user_repository.find_one(self.user_one.username)

        self.assertEqual(user.username, self.user_one.username)
        self.assertEqual(user.password, self.user_one.password)

    def test_find_all(self):
        user_repository.create(self.user_one)
        user_repository.create(self.user_two)
        all_users = user_repository.find_all()
        self.assertEqual(len(all_users), 2)

    def test_find_one(self):
        user_repository.create(self.user_one)
        user = user_repository.find_one(self.user_one.username)
        self.assertEqual(user.username, self.user_one.username)
        self.assertEqual(user.password, self.user_one.password)

    def test_delete_all(self):
        user_repository.delete_all()
        all_users = user_repository.find_all()
        self.assertEqual(len(all_users), 0)
