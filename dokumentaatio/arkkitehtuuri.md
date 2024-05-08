# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa kerrosarkkitehtuuria, jonka pakkausrakenne on seuraava:

![Arkkitehtuuri](./image/arkkitehtuuri.png)

Pakkaus `UI` sisältää sovelluksen käyttöliittymäkoodin.
Pakkaus `services` vastaa sovelluslogiikasta ja koostuu seuraavista osista:

- **ContactService** joka vastaa kontaktien hallinnoinnin sovelluslogiikasta
- **UserService** joka vastaa käyttäjien hallinnoinnin sovelluslogiikasta

## Käyttöliittymä

Sovelluksen käyttöliittymä koostuu seuraavista näkymistä ja luokista:

- Kirjautumisnäkymä `login_view`
- Rekisteröitymisnäkymä `register_view`
- Kontaktien listausnäkymä `contacts_view`
- Kontaktien luomisnäkymä `contacts_form_view`

Käyttöliittymän luokat kutsuvat sovelluslogiikasta vastaavien _UserServicen_ sekä _ContactsServicen_ metodeja, mutta eivät itsessään toteuta sovelluslogiikkaa.

## Sovelluslogiikka

Sovelluksen tietomallin muodostavat luokat `User` ja `Contact`, jotka kuvaavat käyttäjiä ja käyttäjien tallentamia yhteystietoja. Näitä tietomalleja hallinnoivat sovelluksen sovelluslogiikasta vastaavat luokat `ContactService` ja `UserService`.

![Entities](./image/entities.png)

### ContactService

Luokka **ContactService** vastaa käyttöliittymän kontaktilistauksen ja kontaktilomakkeen toimintojen metodeista, joita ovat:

- `get_all_contacts(user_id)`
- `create_contact(self, first_name, last_name, email, phone, role, user_id)`
- `delete_all_contacts(user_id)`
- `delete_one_contact(self, user_id, contact_id)`

**ContactService** pääsee käsiksi kontaktien tallennuksesta/hakemisesta/poistamisesta vastaavan pakkauksessa repositories sijaitsevan luokan **ContactRepository** kautta.

### UserService

Luokka **UserService** vastaa käyttöliittymän kirjautumisen ja rekisteröitymisen toimintojen metodeista sekä tämänhetkisen käyttäjän id'n tarkistamisesta:

- `get_all_users()`
- `get_current_user()`
- `create_user(username, password)`
- `logout()`
- `login(username, password)`

**UserService** pääsee käsiksi käyttäjän luomisesta ja hakemisesta vastaavan pakkauksessa repositories sijaitsevan luokan **UserRepository** kautta.

## Repositories

Pakkaus _repositories_ vastaa tietojen pysyväistallennuksesta tietokantaan, ja koostuu seuraavista osista:

- **ContactRepository** joka vastaa kontaktien tietojen pysyväistallennuksesta
- **UserRepository** joka vastaa käyttäjien tietojen pysyväistallennuksesta

Pakkaus _entities_ sisältää luokkia, jotka kuvaavat sovelluksen käyttämiä tietueita `User` ja `Contact`

## Tietojen pysyväistallennus

Pakkauksen repositories luokat **UserRepository** ja **ContactRepository** vastaavat tietojen pysyväistallennuksesta SQLite-tietokantaan. Molemmat luokat noudattavat repository-suunnittelumallia.

SQLite-tietokannan taulut `users` ja `contacts` alustetaan [initialize_database.py](https://github.com/ranven/contactbook/blob/main/src/initialize_db.py)-tiedostossa. Sovelluksen testeille on oma eristetty tietokantansa, jolloin testit voidaan suorittaa erillisenä tuotantotietokannasta.

## Päätoiminnallisuudet

### Käyttäjän kirjautuminen

Kirjautumisnäkymässä käyttäjän syötettyä käyttäjänimen, salasanan sekä painettua _login_-painiketta, toimii sovellus seuraavanlaisesti:

![Login](./image/login-sekvenssikaavio.png)

Login-painikkeen tapahtumankäsittelijä kutsuu sovelluslogiikan käyttäjiä hallinnoivan UserServicen metodia login parametreilla käyttäjätunnus ja salasana. Sovelluslogiikka kutsuu **UserRepositoryn** `find_one`-metodia tarkistaakseen onko käyttäjä olemassa. Mikäli käyttäjää ei löydy, **UserService** keskeyttää kirjautumisen ja ilmoittaa käyttäjälle virheestä. Mikäli käyttäjä löytyy, palauttaa metodi käyttäjän **UserServicelle**.

Kun **UserService** saa käyttäjän, tarkistaa se täsmääkö annettu salasana tietokannassa olevan käyttäjän salasanan kanssa. Jos salasana täsmää, kirjautuminen onnistuu ja käyttöliittymän näkymäksi vaihtuu **ContactsView**, johon sovellus renderöi kirjautuneen käyttäjän tallentamat kontaktit.

### Uuden käyttäjän luominen

Rekisteröitymisnäkymässä käyttäjän syötettyä yli 4 merkkiä pitkän uniikin käyttäjänimen, yli 4 merkkiä pitkän salasanan sekä painettua _register_-painiketta, toimii sovellus seuraavanlaisesti:

![Register](./image/reg-sekvenssikaavio.png)

Register-painikkeen tapahtumankäsittelijä kutsuu sovelluslogiikan käyttäjiä hallinnoivan UserServicen metodia `create_user` parametreilla käyttäjätunnus ja salasana. Sovelluslogiikka kutsuu **UserRepositoryn** `find_one`-metodia tarkistaakseen onko käyttäjänimi jo käytössä. Mikäli samanniminen käyttäjä löytyy, **UserService** keskeyttää rekisteröitymisen ja ilmoittaa käyttäjälle virheestä. Mikäli käyttäjää ei löydy, palauttaa metodi None-arvon **UserServicelle**.

Kun **UserService** varmistuu käyttäjänimen saatavuudesta, luo se `User`-olion johon se generoi uuid-kirjaston avulla käyttäjän uniikin id'n uuid-kirjaston avulla. Tämän jälkeen sovelluslogiikka tallettaa käyttäjä-olion tietokantaan kutsumalla **UserRepositoryn** metodia `create` parametrilla User. Onnistuneen tallentamisen seurauksena käyttäjä kirjataan sisään ja käyttöliittymän näkymäksi vaihtuu **ContactsView** johon sovellus renderöi kirjautuneen käyttäjän tallentamat kontaktit.

### Uuden kontaktin luominen

Kontaktin luomislomakkeessa käyttäjän syötettyä etunimen, sukunimen, sähköpostin, puhelinnumeron (numeerisessa muodossa) ja roolin sekä painettua _create_-painiketta, toimii sovellus seuraavanlaisesti:

[!Create](https://github.com/ranven/contactbook/blob/main/dokumentaatio/image/create-contact-sekvenssikaavio.png)

Create-painikkeen tapahtumankäsittelijä kutsuu sovelluslogiikan kontakteja hallinnoivan **ContactServicen** metodia `create_contact` parametreilla etunimi, sukunimi, sähköposti, puhelinnumero, rooli sekä käyttäjän ID. Sovelluslogiikka tarkistaa parametreista puhelinnumeron olevan numeerisessa muodossa, kunkin parametrin olevan alle 100 merkkiä pitkiä ja käyttäjän IDn olemassaolon ja ilmoittaa virheestä mikäli jokin näistä ehdoista ei täyty.

Kun **ContactService** varmistuu kontaktin kenttien oikeellisuudesta, luo se `Contact`-olion edellämainituista kentistä, joiden lisäksi generoi kontaktille uniikin id'n uuid-kirjaston avulla. Lisäksi olioon tallennetaan toistaiseksi `created_at`-arvoksi None, sillä tietokanta luo tyhjälle kentälle arvon kun kontakti tallennetaan pysyväismuistiin.

Tämän jälkeen sovelluslogiikka tallettaa `new_contact`-olion kutsumalla **ContactRepositoryn** metodia `create` parametrilla `new_contact`. Onnistuneen tallentamisen seurauksena palautusarvoksi saadaan luotu **Contact**-olio, ja käyttöliittymän näkymäksi vaihtuu **ContactsView** johon sovellus renderöi kirjautuneen käyttäjän tallentamat kontaktit, mukaanlukien juuri luotu uusi kontakti.

### Yhden kontaktin poistaminen

Kontaktien listausnäkymässä käyttäjän painettua yksittäisen kontaktin X-painiketta, toimii sovellus seuraavanlaisesti:

[!DelOne](https://github.com/ranven/contactbook/blob/main/dokumentaatio/image/del-one-sekvenssikaavio.png)

X-painikkeen tapahtumankäsittelijä kutsuu sovelluslogiikan kontakteja hallinnoivan **ContactServicen** metodia `delete_one_contact` parametreilla käyttäjän ID ja poistettavan kontaktin ID. Sovelluslogiikka tarkistaa käyttäjän IDn olemassaolon ja ilmoittaa virheestä mikäli tätä ei ole.

Tämän jälkeen sovelluslogiikka poistaa kontaktin kutsumalla **ContactRepositoryn** metodia `delete_one` parametreilla käyttäjän ID ja poistettavan kontaktin ID. Onnistuneen poistamisen seurauksena palautusarvoksi saadaan None, ja kontaktilistaus renderöidään uudestaan jolloin poistettu kontakti poistuu listalta.

## Kaikkien kontaktien poistaminen

Kontaktien listausnäkymässä käyttäjän painettua _Delete all_-painiketta, toimii sovellus seuraavanlaisesti:

[!DelAll](https://github.com/ranven/contactbook/blob/main/dokumentaatio/image/del-all-sekvenssikaavio.png)

Delete all-painikkeen tapahtumankäsittelijä kutsuu sovelluslogiikan kontakteja hallinnoivan **ContactServicen** metodia `delete_all_contacts` parametrilla käyttäjän ID. Sovelluslogiikka tarkistaa käyttäjän IDn olemassaolon ja ilmoittaa virheestä mikäli tätä ei ole.

Tämän jälkeen sovelluslogiikka poistaa kaikki käyttäjän luomat kontaktit kutsumalla **ContactRepositoryn** metodia `delete_all` parametrilla käyttäjän ID. Onnistuneen poistamisen seurauksena palautusarvoksi saadaan None, ja kontaktilistaus renderöidään uudestaan jolloin kontaktilistaus tyhjenee.
