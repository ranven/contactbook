# Vaatimusmäärittely

## Sovelluksen idea

Sovellus on osoitekirja, johon voidaan tallentaa yhteystietoja listaan. Sovellusta voi käyttää useampi rekisteröitynyt käyttäjä joilla kaikilla on oma yhteystietolistansa.

## Käyttäjäroolit

Sovelluksella on yksi käyttäjärooli (normaali käyttäjä).

## Perustoiminnallisuudet

Sovelluksen tiedot tallennetaan SQLite-tietokantaan ja 4. Yhteystietojen vienti csv-tiedostona
sen graafinen käyttöliittymä toteutetaan PyQt-kirjaston avulla. Sovelluksen perustoiminnallisuudet jakautuvat autentikaatioon sekä kontaktien hallinnointiin.

#### Autentikaatio

- Käyttäjä voi luoda tunnukset sovellukseen

  - Käyttäjätunnuksen tulee olla uniikki ja vähintään 4 merkkiä pitkä

- Käyttäjä voi kirjautua sovellukseen

  - Sovellus autentikoi käyttäjän mikäli tämä syöttää olemassaolevan käyttäjätunnuksen ja salasanan, tai ilmoittaa virheestä mikäli näin ei tapahdu

- Ollessaan sisäänkirjautunut käyttäjä voi kirjautua ulos järjestelmästä

#### Kontaktit

- Käyttäjä voi nähdä tallentamansa kontaktit kirjauduttuaan sovellukseen
- Käyttäjä voi lisätä uuden kontaktin
  - Kontaktiin voi tallentaa nimen, sähköpostiosoitteen, puhelinnumeron sekä roolin.
- Käyttäjä voi poistaa kontaktin
- Käyttäjä voi poistaa kaikki luomansa kontaktit

## Jatkokehitysideat

- Yhteystietojen hakutoiminnallisuus
- Käyttäjätunnuksen ja sen luomien yhteystietojen poisto
- Yhteystietojen tallentaminen erillisiin yhteystietolistoihin sekä listojen hallinnointi
- Admin-käyttäjäroolin luonti jonka avulla voi hallinnoida kaikkia sovellukseen luotuja yhteystietoja
- Kontaktien editointitoiminnallisuus
- Yhteystietojen lisäkentät (esim. tunnisteet tai tägit) joiden avulla filtteröidä kontaktilistaa
