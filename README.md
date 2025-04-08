# ohjelmistotekniikka, harjoitustyö

Ohjelma, jolla voi hallinnoida omaa elokuvakokoelmaansa.

*Linkkejä:* [vaatimusmäärittely](https://github.com/tiikerikakku/harkka/blob/main/dokumentaatio/vaatimusmaarittely.md), [tuntikirjanpito](https://github.com/tiikerikakku/harkka/blob/main/dokumentaatio/tuntikirjanpito.md), [muutokset](https://github.com/tiikerikakku/harkka/blob/main/dokumentaatio/changelog.md), [arkkitehtuuri](https://github.com/tiikerikakku/harkka/blob/main/dokumentaatio/arkkitehtuuri.md)

## käyttö

Asenna ensin poetrylla. Tämän jälkeen seuraavat komennot ovat käytettävissäsi:

```sh
poetry shell
invoke db               # tietokanta kuntoon (huom!!!!!!!!!!!!!!!!! tyhjentää kannan)
invoke start

invoke test             # testaa
invoke coverage-report  # luo kattavuusrapsa
invoke lint             # koodityylin tarkastus
```
