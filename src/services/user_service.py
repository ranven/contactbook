import uuid
from repositories.user_repository import user_repository
from entities.user import User


class InvalidCredentialsError(Exception):
    pass


class UsernameTakenError(Exception):
    pass


class UserService:
    def __init__(
            self,
            user_repo=user_repository):
        self._user = None
        self._user_repository = user_repo

    def get_users(self):
        return self._user_repository.find_all()

    def get_current(self):
        return self._user

    def create(self, username, password):
        existing_user = self._user_repository.find_one(username)
        if existing_user:
            raise UsernameTakenError((f"Username {username} already exists"))

        if len(username) < 4:
            raise InvalidCredentialsError(
                "Username should be at least 4 characters long")
        if len(password) < 4:
            raise InvalidCredentialsError(
                "Password should be at least 4 characters long")

        user = self._user_repository.create(
            User(username, password, uuid.uuid4().hex))
        self._user = user
        return user

    def logout(self):
        self._user = None

    def login(self, username, password):
        user = self._user_repository.find_one(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user
        return user


user_service = UserService()
