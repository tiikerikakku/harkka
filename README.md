# ohjelmistotekniikka, harjoitustyö

Ohjelma, jolla voi hallinnoida omaa elokuvakokoelmaansa.

*Linkkejä:* [vaatimusmäärittely](https://github.com/tiikerikakku/harkka/blob/main/dokumentaatio/vaatimusmaarittely.md), [tuntikirjanpito](https://github.com/tiikerikakku/harkka/blob/main/dokumentaatio/tuntikirjanpito.md), [muutokset](https://github.com/tiikerikakku/harkka/blob/main/dokumentaatio/changelog.md)

## käyttö

```sh
poetry shell
invoke db               # tietokanta kuntoon (huom!!!!!!!!!!!!!!!!! tyhjentää kannan)
invoke start

invoke test             # testaa
invoke coverage-report  # luo kattavuusrapsa
```
