## vk 5

* Korjattu edellisen viikon kehityskohdat
* Pakollinen sekvenssikaavio lisätty dokumentaatioon
* Ns. service käyttöliittymän ja repon väliin
* Elokuvakokoelman peruspalikat kohdillaan; lisääminen, poistaminen, tarkastelu
* Testejä
* Skeemaa taas parenneltu

### mahdollisesti kehitettävää

* `.vscode`-hakemisto on tarkoituksella lisätty gitiin, mutta mikäli ohjaajan mielestä tämä on pisteenvähennyksiin johtava teko, niin sen voin jättää pois

## vk 4

* Lint pystyyn
* Refaktorointia; nimimuutoksia ja muuttujakaaoksen selvittelyä
* Viankäsittelyä käyttäjän käsitellessä tietokantaa ohjelman kautta
* Käyttäjä kirjataan automaattisesti sisään, kun tili on luotu
* Skeemaa päivitetty hieman
* Järjestelmään voi nyt lisätä elokuvan (jota toistaiseksi ei voi lisätä käyttäjän omaan kokoelmaan; tulee seuraavaksi)
* `MovieRepository` testikattavuus 100 %, ohjelman testikattavuus pysyy toistaiseksi 100 %:ssa

### bugit/kehitettävää

* Elokuvan nimi voi olla tyhjä. Koskee todennäköisesti myös käyttäjänimiä. Tämä ei vaikuta ohjelman toimintaan, mutta tulevissa versioissa tähän tulee mahdollisesti muutosta.
* Lint valittaa virheenkäsittelyosioista. Muutetaan tätä pikimmiten, jotta lintin valitusta ei tarvitse katsoa.

## vk 3

* Käyttäjä näkee sovelluksen käynnistyttyä käyttäjälistan
* Käyttäjä voi kirjautua
* Käyttäjä voi luoda tunnuksen
* Luotu primitiivinen käyttöliittymä ja siihen liittyvät luokat
* Tietokantayhteys muodostettu ohjelman kautta
* Tietokannan skeema ja tyhjentämismahdollisuus
* `UserRepository`n tesitkattavuus 100 % (saa nähdä miten kauan...)
