```mermaid
  classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli

    Ruutu -- Aloitus
    Ruutu -- Vankila
    Ruutu -- Sattuma-yhteismaa
    Ruutu -- Asema-laitos
    Ruutu -- Katu

    Monopolipeli -- "1" Aloitus
    Monopolipeli -- "1" Vankila

    class Katu {
      nimi
    }

    Sattuma-yhteismaa -- Kortti

    class Kortti {
      tapahtuma
    }

    Katu -- "0..4" Talo
    Katu -- "0..1" Hotelli
    Katu "0..1" -- Pelaaja

    Pelaaja -- Raha
```
