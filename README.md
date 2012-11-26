kunnallisvaalit
===============

Kunnallisvaalien numeronmurskausta

* Skripti äänestysdatan ja HS.fi edustajien arvokartan yhteensaattamiseen
* Kevyt WebGL plot-graafi (WIP)

Käyttö
------

* Git Clone tämä repo
* Hesarin datat saatavilla myös täältä, tässä repossa muunnettuna CSV:ksi)
* Lataa seuraava file:
http://192.49.229.37/K2012/data/k-2012_maa.xml.zip
* Unzippaa tiedosto
* Aja skripti
./valuemixer_hel.py  raaka-datat/ehdokasvastaukset-12-10-2012-verkkoon/Suppea data-Table 1.csv <unzipattu xml-file>
* Lopputuloksena vaalitulos xml, jossa values-attribuutteina vaalikonevastauksista johdetut oikeisto-vasemmisto, liberaali-konservatiivi ja vihreä, ei-eivihreä 


Lisenssit
---------
* HTML pohjautuu Apache-lisenssin alaiseen esimerkkiin. Python-skriptit Public Domainissa. Huomaa, että html-hakemiston excanvas.js on kaupallinen js-kirjasto, jonka kaupallisesta käytöstä maksettava lisenssi (mutta sen poistamalla menettää vain internet explorer -tuen)
* Helsingin sanomien datat on alunperin jaettu seuraavalla CC-lisenssillä:
http://creativecommons.org/licenses/by-nc/1.0/fi/
* Oikeusministeriön vaalidata oikeusministeriön ehdoin jaettu
