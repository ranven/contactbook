import uuid
from repositories.contact_repository import contact_repository
from entities.contact import Contact


class NoUserError(Exception):
    pass


class ContactService:
    """Luokka joka vastaa kontakteihin liittyvästä sovelluslogiikasta.
    """

    def __init__(
            self,
            contact_repo=contact_repository):
        """Luokan konstruktori.

        Args: 
            contact_repo: luokka josta kutsua kontakteihin liittyvien 
            tietokantaoperaatioiden metodeja
        """
        self._contact_repository = contact_repo
        self.contacts = None

    def get_contacts(self, user_id):
        """Tarkistaa käyttäjän id'n ja kutsuu contact_repositoryn find_all-metodia hakeakseen 
        käyttäjän kontaktit. 

        Nostaa virheilmoituksen mikäli käyttäjän id'tä ei ole.

        Args:
            user_id käyttäjän id

        Returns:
            Palauttaa listan Contact-olioita

        """

        if user_id is None:
            raise NoUserError("No user is logged in.")
        return self._contact_repository.find_all(user_id)

    def create_contact(self, first_name, last_name, email, phone, role, user_id):
        """Tarkistaa käyttäjän id'n ja luo argumenttien kentistä Contact-olion sekä 
        id'n kontaktille. 
        Kutsuu contact_repositoryn create-metodia luodakseen kontaktin. 
        Nostaa virheilmoituksen mikäli käyttäjän id'tä ei ole.

        Args:
            first_name: kontaktin etunimi
            last_name: kontaktin sukunimi
            email: kontaktin sähköposti 
            phone: kontaktin puhelinnumero
            role: kontaktin rooli
            user_id: kontaktin luoneen käyttäjän id

        Returns:
            Palauttaa luodun Contact-olion

        """

        if user_id is None:
            raise NoUserError("No user is logged in.")

        new_contact = Contact(
            contact_id=uuid.uuid4().hex,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            role=role,
            created_at=None,
            user=user_id)

        return self._contact_repository.create(new_contact)

    def delete_all(self, user_id):
        """Tarkistaa käyttäjän id'n ja kutsuu contact_repositoryn delete_all-metodia 
        poistaakseen käyttäjän kontaktit. 

        Nostaa virheilmoituksen mikäli käyttäjän id'tä ei ole.

        Args:
            user_id käyttäjän id

        Returns:
            Palauttaa listan Contact-olioita

        """
        if user_id is None:
            raise NoUserError("No user is logged in.")

        self._contact_repository.delete_all(user_id)


contact_service = ContactService()
