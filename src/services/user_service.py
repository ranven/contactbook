import uuid
from repositories.user_repository import user_repository
from entities.user import User


class InvalidCredentialsError(Exception):
    """Luokka joka epäkelvon käyttäjänimen ja/tai salasanan aiheuttamasta virheestä"""


class UsernameTakenError(Exception):
    """Luokka joka vastaa jo käytössä olevan käyttäjänimen rekisteröinnin aiheuttamasta virheestä"""


class UserService:
    """Luokka joka vastaa käyttäjiin liittyvästä sovelluslogiikasta.
    """

    def __init__(
            self,
            user_repo=user_repository):
        """Luokan konstruktori.

        Args: 
            user_repo: luokka josta kutsua käyttäjiin liittyvien tietokantaoperaatioiden metodeja
        """
        self._user = None
        self._user_repository = user_repo

    def get_all_users(self):
        """Kutsuu user_repositoryn find_all-metodia hakeakseen kaikki käyttäjät.

        Returns:
            Palauttaa listan User-olioita

        """
        return self._user_repository.find_all()

    def get_current_user(self):
        """Hakee kirjautuneen käyttäjän tiedot.

        Returns:
            Palauttaa kirjautuneen käyttäjän User-oliona.
        """
        return self._user

    def create_user(self, username, password):
        """Tarkistaa user_repositoryn find_one-metodin avulla onko annettu käyttäjänimi jo käytössä, 
        nostaa virheilmoituksen mikäli käyttäjä löytyy. 

        Tarkistaa käyttäjänimen ja salasanan pituuden ja nostaa virheilmoituksen niiden ollessa 
        alle 4 merkkiä lyhyitä. 

        Luo argumenttien kenttien ja uuid-kirjaston id'n avulla User-olion. 
        Kutsuu user_repositoryn create-metodia luodakseen käyttäjän. 
        Asettaa create-metodin palauttaman käyttäjän kirjautuneeksi käyttäjäksi.

        Args:
            username: käyttäjän käyttäjänimi 
            password: käyttäjän salasana

        Returns:
            Palauttaa luodun User-olion

        """
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
        """Tyhjentää kirjautuneen käyttäjän tiedot ja kirjaa tämän ulos.
        """
        self._user = None

    def login(self, username, password):
        """Tarkistaa user_repositoryn find_one-metodin avulla onko annettu käyttäjätunnus olemassa, 
        nostaa virheilmoituksen mikäli käyttäjää ei löydy. 

        Kutsuu user_repositoryn login-metodia kirjatakseen käyttäjän sisään. 
        Asettaa login-metodin palauttaman käyttäjän kirjautuneeksi käyttäjäksi.

        Args:
            username: käyttäjän käyttäjänimi 
            password: käyttäjän salasana

        Returns:
            Palauttaa luodun User-olion

        """
        user = self._user_repository.find_one(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user
        return user


user_service = UserService()
