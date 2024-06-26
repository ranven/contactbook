import uuid
import re
from repositories.contact_repository import contact_repository
from entities.contact import Contact


class NoUserError(Exception):
    """Luokka joka vastaa puuttuvan käyttäjä-idn aiheuttamasta virheestä"""


class ContactCreationError(Exception):
    """Luokka joka vastaa kontaktin luomisessa viallisen syötteen takia tapahtuvasta virheestä"""


class PhoneNumberError(Exception):
    """Luokka joka vastaa kontaktin luomisessa puhelinnumero-kentän 
    viallisuuden takia tapahtuvasta virheestä"""


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

    def get_contacts(self, user_id):
        """Tarkistaa käyttäjän id'n ja kutsuu contact_repositoryn find_all-metodia hakeakseen 
        käyttäjän kontaktit. 

        Nostaa virheilmoituksen mikäli käyttäjän ID'tä ei ole.

        Args:
            user_id käyttäjän id

        Returns:
            Palauttaa listan Contact-olioita

        """

        if user_id is None:
            raise NoUserError("No user is logged in.")

        return self._contact_repository.find_all(user_id)

    def create_contact(self, first_name, last_name, email, phone, role, user_id):
        """Tarkistaa käyttäjän id'n, puhelinnumeron formaatin sekä 
        syötteiden pituuksien olevan alle 100 merkkiä. 
        Nostaa virheilmoituksen mikäli jokin tarkistuksista ei mene läpi.

        Luo argumenttien kentistä Contact-olion sekä id'n kontaktille. 

        Kutsuu contact_repositoryn create-metodia luodakseen uuden kontaktin. 

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

        if not re.search(r'^([\s\d]+)$', phone):
            raise PhoneNumberError("Phone number should be a number.")

        if any(len(field) > 100 for field in [first_name, last_name, phone, email, role]):
            raise ContactCreationError(
                "Each field has a maximum length of 100 characters.")

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

    def delete_all_contacts(self, user_id):
        """Tarkistaa käyttäjän id'n ja kutsuu contact_repositoryn delete_all-metodia 
        poistaakseen kaikki käyttäjän kontaktit. 

        Nostaa virheilmoituksen mikäli käyttäjän ID'tä ei ole.

        Args:
            user_id käyttäjän id
        """

        if user_id is None:
            raise NoUserError("No user is logged in.")

        self._contact_repository.delete_all(user_id)

    def delete_one_contact(self, user_id, contact_id):
        """Tarkistaa käyttäjän id'n ja kutsuu contact_repositoryn delete_one-metodia 
        poistaakseen yhden kontaktin annetun id'n perusteella.

        Nostaa virheilmoituksen mikäli käyttäjän ID'tä ei ole.

        Args: 
            user_id käyttäjän id
            contact_id poistettavan käyttäjän id 
        """

        if user_id is None:
            raise NoUserError("No user is logged in.")

        self._contact_repository.delete_one(user_id, contact_id)


contact_service = ContactService()
