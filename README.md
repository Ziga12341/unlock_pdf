## UNLOCK PDF

Program služi odklepanju .pdf datotek računalniško kodiranih gesel z dolžino šest znakov.
Uporabljajte odgovorno.

Opredelitev problema: Več kadrovskih programov uporablja za kodiranje svojih .pdf-je strojno generirano 6 mestno kodo. S tem programom preverjam ali je ta način dandanes še varen.

Cilj/Namen: Vedel sem, da je geslo .pdf katerega odpiram dolgo 6 znakov in kako je kodirano. Želja je odpreti tako močno kodirano geslo z Windows 10 operacijskim sistemom in pythonovo knjižnico pikepdf ter, da vse skupaj teče v ozadju in preveč ne obremenjuje računalnika.
Poleg tega sem želel doseči, da ni potrebno pogledati določeno mapo ali je računalnik našel geslo, pač pa da mi ga enostavno pošlje na e-mail.


#### 1 UVOD


Navodila so za Windows 10

Pri testu sem uporabljal procesor i9-9900K 3,60GHz in 32 giga rama DDR4.
Obremenjenost računalnika je bila približno procesor 50% (4,62 GHz) in 55% (17,5 GB) RAM. Računalnik je kljub obremenitvam omogočal normalno delo.

V primeru da sem zagnal en program je bila obremenitev računalnika manjša ampak je pregledal le 700 gesel na sekundo. Zato sem se odločil, da ustvarim in zaženem 4 datoteke za 4 programe.
V mojem primeru sem zagnal štiri programe hkrati, rezultat v tem primeru je bil 3150 pregledanih gesel/sekundo.

Sam sem odpiral .pdf ki je bil zaklenjen s šest znaki ASCII in števke. Skupaj pride 62 kombinacij za vsako polje vse skupaj predstavlja
56800235584 (približno 56 milijard kombinacij)

Problem sem razdelil na več manjših: tako da sem prva dva znaka določal sam s seznamom (aa,ab,ac,...) potem pa dodal zadnje 4 znake generično
na ta način sem dobil 14776336 kombinacij po 3844 (za prva znaka). Tako sem imel 3844 obravnavanj.

S hitrostjo, ki mi jo omogoča, če zaženem 4 programe hkrati, je pomenilo 0.47 procentov na dan oziroma 18 pregledanih obravnavanj v enem dnevu.
V 213 dneh bo računalnik pogledal vse kombinacije.

##### 1.1 HIPOTEZA

6 mestno geslo ASCII zznaki in štivilke ni varno geslo, saj se ga da relativno hitro odpreti.


##### 1.2 DELOVANJE PROGRAMA

Program omogoča, da teče v ozadju. Sam si zapisuje kje je ostal (da lahko pogleda vseh 3844 kombinacij). Tudi če pride do izpada električne energije ali ponovnega zagona računalnika, program nadaljuje tam kjer je je ostal.
Temu so namenjene datoteke number1.txt, number2.txt,... V teh datotekah je nastavljeno kje (pri katerem indeksu) posamezen program začne. Recimo pri number1.txt začne pri 0 in dela do 999, drugi program prebere v numbre2 številko 1000, tam začne in neha pri 1999 itd.
Bližnjice launch_bat_mg1.vbs, launch_bat_mg2.vbs,... je potrebno prilepiti v "zagon (startup)" C:\Users\[***]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup.
To služi, da se ob ponovnem zagonu v ozadju zažene program. Koliko jih je pogledal program sproti zapisuje v mapo status.txt. Tam napiše tudi geslo ko ga najde. Program omogoča da pošlje geslo tudi na e-mail ko ga le ta odkrije.
Potrebno je ustvariti nov račun na Google in omogočiti [e-mail za razvijalce](https://realpython.com/python-send-email/) poglavje: Sending a Plain-Text Email.


#### 2 NAMESTITEV

Nameščen morate imeti python 3.# novejše verzije
Prenesite vse datoteke v mapo.
Predlagam git Clone

Potrebno je namestiti pikepdf in tqdm
v terminal vnesite:
pip install pikepdf
pip install tqdm



mg#.bat je namenjena temu da pokliče določeno funkcijo (variant#() v mg#.py). V mg# so uvožene funkcije iz main.py. Launch_bat_mg#.vbs je namenjena temu da zažene program v ozadju. Torej da se vidi le pod upravitelj opravil da računalnik dejansko žene ta pythonov file
vse kar morate spremljati je datoteka status.txt kjer vam pove koliko je že pogledal gesel ali je že našel geslo ter kakšno je. Geslo program sam pošlje na mail (ustvariti Google račun - email za razvijalce in spremeniti v main.py svoj naslov


Najprej zaženite .bat file, da vidite če normalno deluje ali javi kakšno napako. Problem bi lahko bil ker Windows ne ve in kje mora zagnati python

Skopiraj vse .vbs – Bližnjica v zagon (startup) win + r shell:startup


#### 3 KAJ MORATE SPREMENITI

Ko naložite vse priložene datoteke v določeno mapo
V mapo morate prilepiti .pdf. Datoteko zaščiteno z geslom preimenujte v unlock.pdf

Ko je vse naloženo in deluje, desni klik na mapo in skrij mapo

#### 4 TEŽAVE

Če se vam pojavlja težava z .bat skripto je to verjetno zato ker sistem ne ve iz kje naj bere python. 
V tem primeru spremenite #.bat tako da sistemu programu poveste kje imate spravljen/naložen python.exe:
"C:\[***]\AppData\Local\Programs\Python\Python37\python.exe"
"C:\[***]\mg#.py"
pause

ter v mape mg#.py na kondu dodajte print(variant#())

V primeru težav z uvozom paythonovih knjižnic.
Odprite cmd. Postavite se v direktory kjer imate shranjene datoteke tega projekta in tam zaženite pip install pikepdf, pip install **,...

#### 5 ZAKLJUČEK

Po 787 obravnavanjih od 3844 sem v mojem primeru odkril geslo. Kar pomeni da je bilo potrebno pogledati 20% vseh možnosti (okrog 11.5 milijard pregledanih možnosti).
Sklep: Hipoteza je potrjena. V Dobrem mesecu dni (34 dni v mojem primeru) se da z zgoraj napisanim programom odpreti .pdf kodiran s 6 mestno kodo ASCII + številke (primer: HTR8ef).
Takšno kodiranje gesel ni priporočljivo.


#### 6 VIRI

- [pypi](https://pypi.org/project/pikepdf/)
- [Pošiljanje pošte s python-om; poglavje: Sending a Plain-Text Email](https://realpython.com/python-send-email/)


ŽP

