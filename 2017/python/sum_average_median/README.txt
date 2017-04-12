koodauskoe.py <tiedoston nimi> <sum|avg|median> [<gt|lt|eq> <n>]

Developed using Python 3.5.1

Testing done with PyTest

===
 
Toteuta Python-ohjelma joka laskee tiedostoon talletetuista luvuista summan, keskiarvon tai mediaanin, vertailee tulosta annettuun lukuun ja tulostaa vertailun tuloksen.
 
Ohjelman komentorivi:
koodauskoe.py <tiedoston nimi> <sum|avg|median> [<gt|lt|eq> <n>]
 
Tiedoston nimi - se on tiedosto, jossa oletetaan olevan allekkain lukuja. Esimerkiksi test.txt:
123
521
325
 
Seuraava argumentti kertoo, mikä tulos näistä tehdään. sum = summa. Eli lasketaan kaikki yhteen. avg = keskiarvo. median = suuruusjärjestyksessä keskimmäinen luku. Jos tässä tapauksessa lukuja on parillinen määrä, tulostetaan molemmat. Esimerkiksi sarjasta 2,3,6,8 tulostettaisiin luvut 3 ja 6.
 
Sitten pääsemme vapaaehtoisiin argumentteihin. Ne tekevät vertailun tuloksen ja <n> -luvun välillä. gt on tulos > n, lt tulos < n, ja eq tulos = n
 
Jos mediaanissa on useampi kuin yksi luku, vertailu on tehtävä niille kaikille.
 
Jos lauseke on tosi, silloin kirjoitetaan "<tulos> on <operaatio> <n>". Muuten kirjoitetaan "<tulos> ei ole <operaatio> <n>".
 
Esimerkiksi:
koodauskoe.py test.txt sum lt 1000
Summa on: 969
969 on pienempi kuin 1000
 
koodauskoe.py test.txt median
Mediaani on: 325
 
koodauskoe.py test.txt sum gt 1000
Summa on: 969
969 ei ole suurempi kuin 1000
 
===