# Contact Book

Sovellus on osoitekirja johon käyttäjä voi tallentaa ja hallinnoida tallettamiaan yhteystietoja. Sovellusta voi käyttää useampi rekisteröitynyt käyttäjä joilla kaikilla on oma yhteystietolistansa.

## Releases

[Viikon 5 release](https://github.com/ranven/contactbook/releases/tag/viikko5)
[Viikon 6 release](https://github.com/ranven/contactbook/releases/tag/viikko6)

## Dokumentaatio

[Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](/dokumentaatio/tuntikirjanpito.md)

[Changelog](/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](/dokumentaatio/kayttoohje.md)

## Sovelluksen asennus ja käyttäminen

Riippuvuuksien asennus:

`poetry install`

Alusta sovellus:

`poetry run invoke build`

Käynnistä sovellus:

`poetry run invoke start`

## Komentorivitoiminnot

Testien ajaminen:

`poetry run invoke test`

Testikattavuus:

`poetry run invoke coverage-report`

Pylint:

`poetry run invoke lint`
