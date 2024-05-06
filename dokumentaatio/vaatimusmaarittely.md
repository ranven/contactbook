# Vaatimusmäärittely

## Sovelluksen idea

Sovellus on osoitekirja, johon voidaan tallentaa yhteystietoja listaan. Sovellusta voi käyttää useampi rekisteröitynyt käyttäjä joilla kaikilla on oma yhteystietolistansa.

## Käyttäjäroolit

Sovelluksella on yksi käyttäjärooli (normaali käyttäjä).

## Perustoiminnallisuudet

Sovelluksen tiedot tallennetaan SQLite-tietokantaan ja
sen graafinen käyttöliittymä toteutetaan Tkinter-kirjaston avulla. Sovelluksen perustoiminnallisuudet jakautuvat autentikaatioon sekä kontaktien hallinnointiin.

#### Autentikaatio

- Käyttäjä voi luoda tunnukset sovellukseen **TEHTY**

  - Käyttäjätunnuksen tulee olla uniikki ja vähintään 4 merkkiä pitkä **TEHTY**
  - Salasanan tulee olla vähintään 4 merkkiä pitkä **TEHTY**
  - Käyttäjä näkee virheilmoituksen mikäli nämä ehdot eivät täyty **TEHTY**

- Käyttäjä voi kirjautua sovellukseen **TEHTY**

  - Sovellus autentikoi käyttäjän mikäli tämä syöttää olemassaolevan käyttäjätunnuksen ja salasanan, tai ilmoittaa virheestä mikäli näin ei tapahdu **TEHTY**

- Ollessaan sisäänkirjautunut käyttäjä voi kirjautua ulos järjestelmästä **TEHTY**

#### Kontaktit

- Käyttäjä voi nähdä tallentamansa kontaktit kirjauduttuaan sovellukseen **TEHTY**
- Käyttäjä voi lisätä uuden kontaktin **TEHTY**
  - Kontaktiin voi tallentaa nimen, sähköpostiosoitteen, puhelinnumeron sekä roolin. **TEHTY**
  - Käyttäjä näkee virheilmoituksen mikäli annettu puhelinnumero ei ole numeroarvo **TEHTY**
- Käyttäjä voi poistaa yksittäisen kontaktin **TEHTY**
- Käyttäjä voi poistaa kaikki luomansa kontaktit **TEHTY**

## Jatkokehitysideat

- Yhteystietojen hakutoiminnallisuus
- Käyttäjätunnuksen ja sen luomien yhteystietojen poisto
- Yhteystietojen tallentaminen erillisiin yhteystietolistoihin sekä listojen hallinnointi
- Admin-käyttäjäroolin luonti jonka avulla voi hallinnoida kaikkia sovellukseen luotuja yhteystietoja
- Kontaktien editointitoiminnallisuus
- Yhteystietojen lisäkentät (esim. tunnisteet tai tägit) joiden avulla filtteröidä kontaktilistaa
