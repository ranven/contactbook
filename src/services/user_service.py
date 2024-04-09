from ..repositories.user_repository import user_repository
from ..entities.user import User


class UserService:
    def __init__(
            self,
            user_repository=user_repository):
        self._user = None
        self._user_repository = user_repository

    def get_users(self):
        return self._user_repository.find_all()

    def get_current(self):
        return self._user

    def create(self, username, password):
        # todo: check for existing user
        user = self._user_repository.create(User(username, password))
        self._user = user
        return user

    def logout(self):
        self._user = None

    # todo: login
