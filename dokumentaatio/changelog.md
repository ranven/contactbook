# Changelog

## Viikko 3

- Luotu runko sovellukselle ja alustettu tietokanta
- Luotu UserRepository-luokka, joka vastaa käyttäjän hallinnasta tietokannassa
- Luotu UserService-luokka, joka vastaa sovelluslogiikan koodista autentikoinnin suhteen
- Käyttäjä voi luoda käyttäjätunnuksen, kirjautua sisään sekä kirjautua ulos graafisen käyttöliittymän kautta
- Testattu että UserRepository-luokka palauttaa ja luo käyttäjätunnuksia oikein

## Viikko 4

- Lisätty PyLint ja Autopep-työkalut sekä korjattu Pylint-virheet
- Lisätty kontaktit sekä käyttäjän ID tietokantamalliin
- Luotu ContactService-luokka, joka vastaa sovelluslogiikan koodista kontaktien hakemisen ja luomisen suhteen
- Luotu ContactRepository-luokka, joka vastaa kontaktien hallinnasta tietokannassa
- Käyttäjä voi kirjautuneena ollessaan luoda uusia kontakteja graafisen käyttöliittymän kautta
- Toteutettu alustava käyttöliittymä kontaktien listaamiseksi kirjautuneelle käyttäjälle (listaus ei kuitenkaan vielä toimi)
- ContactRepository-luokan testit aloitettu

## Viikko 5

- Luotu toiminnallisuudet kontaktien listaamiseksi ja poistamiseksi
- Parannuksia virheiden käsittelyyn ja virheilmoituksiin
- Lisätty puuttuvat kentät (role, email) kontaktien luomiseen ja listaamiseen
- Käyttäjä voi kirjautuneena ollessaan tarkastella tallentamiansa kontakteja graafisen käyttöliittymän kautta
- Käyttäjä voi kirjautuneena ollessaan poistaa kaikki luomansa kontaktit graafisen käyttöliittymän kautta
- Testattu että ContactRepository-luokka palauttaa, luo ja poistaa kontakteja oikein

## Viikko 6

- Testattu että käyttäjän rekisteröityminen ja kirjautuminen toimii oikeilla tunnuksilla ja epäonnistuu liian lyhyillä, käytössä olevilla tai väärillä tunnuksilla
- Testattu että kontaktien luominen, hakeminen ja poistaminen toimii odotetulla tavalla kirjautuneelle käyttäjälle
