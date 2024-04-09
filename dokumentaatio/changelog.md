# Changelog

## Viikko 3

- Luotu runko sovellukselle ja alustettu tietokanta
- Luotu UserRepository-luokka, joka vastaa käyttäjän hallinnasta tietokannassa
- Luotu UserService-luokka, joka vastaa sovelluslogiikan koodista autentikoinnin suhteen
- Käyttäjä voi luoda käyttäjätunnuksen, kirjautua sisään sekä kirjautua ulos graafisen käyttöliittymän kautta
- Testattu että UserRepository-luokka palauttaa ja luo käyttäjätunnuksia oikein

Huomioitavaa: PyQt-käyttöliittymäkirjaston kanssa ilmeni ongelmia, jonka vuoksi käyttöliittymä on toistaiseksi toteutettu TKinterin avulla. Sovelluksen edetessä pyrkimyksenäni on toteuttaa käyttöliittymä PyQt-kirjaston avulla.
