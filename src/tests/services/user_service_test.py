import unittest
from repositories.user_repository import user_repository
from services.user_service import UserService, InvalidCredentialsError, UsernameTakenError
from entities.user import User


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


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService(FakeUserRepository())

    def test_create_user(self):
        self.user_service.create_user('testuser', 'testpassword')
        users = self.user_service.get_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, 'testuser')

    def test_create_user_with_too_short_username(self):
        with self.assertRaises(InvalidCredentialsError):
            self.user_service.create_user('aaa', 'testpassword')

    def test_create_user_with_too_short_password(self):
        with self.assertRaises(InvalidCredentialsError):
            self.user_service.create_user('testuser', 'aaa')

    def test_create_user_with_existing_username(self):
        self.user_service.create_user('existinguser', 'password')

        with self.assertRaises(UsernameTakenError):
            self.user_service.create_user('existinguser', 'newpassword')

    def test_login_with_invalid_username(self):
        self.user_service.create_user('testuser', 'testpassword')

        with self.assertRaises(InvalidCredentialsError):
            self.user_service.login('invaliduser', 'testpassword')

    def test_login_with_invalid_password(self):
        self.user_service.create_user('testuser', 'testpassword')

        with self.assertRaises(InvalidCredentialsError):
            self.user_service.login('testuser', 'invalidpassword')

    def test_login_with_valid_username_and_password(self):
        self.user_service.create_user('testuser', 'testpassword')
        user = self.user_service.login('testuser', 'testpassword')

        self.assertEqual(user.username, 'testuser')

    def test_logout(self):
        self.user_service.create_user('testuser', 'testpassword')
        self.user_service.logout()

        self.assertIsNone(self.user_service.get_current_user())
