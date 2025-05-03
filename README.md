# Reseptipankki

## Sovelluksen toiminnot

 - Sovelluksessa käyttäjät pystyvät jakamaan ruokareseptejään. Reseptissä lukee tarvittavat ainekset ja valmistusohje.
 - Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
 - Käyttäjä pystyy lisäämään reseptejä ja muokkaamaan ja poistamaan niitä.
 - Käyttäjä pystyy lisäämään resepteihin kuvia ja poistamaan niitä.
 - Käyttäjä näkee sovellukseen lisätyt reseptit.
 - Käyttäjä pystyy etsimään reseptejä hakusanalla.
 - Käyttäjäsivu näyttää, montako reseptiä käyttäjä on lisännyt ja listan käyttäjän lisäämistä resepteistä.
 - Käyttäjä pystyy valitsemaan reseptille luokittelun.
 - Käyttäjä pystyy antamaan reseptille kommentin ja arvosanan. Reseptistä näytetään kommentit ja keskimääräinen arvosana.
   
## Sovelluksen asennus

Asenna Flask- kirjasto:
```
$ pip install flask
```
Luo tietokannan taulut ja lisää alkutieto:
```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```
Voit käynnistää sovelluksen näin:
```
$ flask run
```
## Suuri tietomäärä
 - Sovellusta testattu suurella tietomäärällä ja silloin se toimii erittäin huonosti.
