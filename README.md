Program služi odklepanju .pdf datotek računalniško kodiranih gesel z dolžino šest znakov.
Uporabljajte odgovorno.

Cilj/Namen: Vedel, da je geslo .pdf katerega odpiram dolgo 6 znakov in kako je kodirano. Želja je odpreti tako močno kodirano geslo z windows računalnikom in pythonovo knjižnico pikepdf ter da vse skupaj teče v ozadju in ne obremenjuje računalnika.
Poleg tega sem želel doseči, da ne rabim hoditi gledat v določeno mapo ali je računalnik našel geslo, pač pa da mi ga enostavno pošlje na email.


1. UVOD

Navodila so za Windows 10

Pri testu sem uporabljal procesor i9-9900K 3,60GHz in 32 giga rama DDR4.
Obremenjenost računalnika je bila približno procesor 50% (4,62 GHz) in 55% (17,5 GB) RAM. Računalnik je kljub obremenitvam omogočal normalno delo.

V primeru da sem zagnal en program je bila obremenitev računalnika manjša ampak je pregledal le 700 gesel na sekundo. Zato sem naložil datoteke za 4 programe.
Pri runanju 4. programov hkrati, kar pomeni rezultat 3150 pogledanih gesel/sekundo.

Sam sem odpiral .pdf ki je bil zaklenjen s šest znaki ASCII in števke. Skupaj pride 62 kombinacij za vsako polje vse skupaj predstavlja
56800235584 (pribljižno 56 milijard kombinacij)

Problem sem razdelil na več manjših: tako da sem prva dva znaka določal sam s seznamom (aa,ab,ac,...) potem pa dodal zadnje 4 znake generično
na ta način sem dobil 14776336 kombinacij po 3844 (za prva znaka). Tako sem imel 3844 obravnavanj.

S hitrostjo, ki mi jo omogoča, če zaženem 4 programe hkrati, je pomenilo 0.47 procentov na dan oziromo 18 pogledanih obravnavanj v enem dnevu.
V 213 dneh bo računalnik pogledal vse kombinacije.

1.1

Porgram omogoča, da teče v ozadju. Sam si zapisuje kje je ostal (da lahko pogleda vseh 3844 kombinacij). Tudi če pride do izpada elektrike restarta računalnika ve kje je ostal
za to služijo datiteke stevilka1.txt, stevilka2.txt,... bljižnice launch_bat_mg1.vbs, launch_bat_mg2.vbs,... je potrebno prilepiti v "zagon (startup)" C:\Users\[***]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
to služi da se ob ponovnem zagonu v ozadju zažene program. Koliko jih je pogledal program sproti zapisuje v mapo status.txt. Tam napiše tudi geslo ko ga najde. Program omogoča da pošlje geslo tudi na email ko ga le ta odkrije.
Potrebno je ustvariti nov račun na google in omogočiti email za razvijalce (vir: https://realpython.com/python-send-email/; poglavje: Sending a Plain-Text Email).

2. NAMESTITEV

Nameščen morate imeti python 3.# novejše verzije
Prenesite vse datoteke v mapo.
Predlagam git Clone

Potrebno je namestiti pikepdf in tqdm
v terminal vnesite:
pip install pikepdf
pip install tqdm




mg#.bat je namenjena temu da pokliče določeno funkcijo (variant#() v mg#.py). launch_bat_mg#.vbs je namenjena temu da zažene program v ozadju. Torej da se vidi le pod upravitelj opravil da računalnik dejansko žene ta pythonov file
vse kar morate spremljati je datoteka status.txt kjer vam pove koliko je že pogledal gesel ali je že našel geslo ter kakšno je. Geslo program sam pošlje na mail (ustvariti google za razvijalce in spremeniti v mg#.py svoj naslov


Najprej zaženite .bat file da vidite če normalno deluje ali javi kakšno napako. Problem bi lahko bil ker windows ne ve in kje mora runati python

Skupiraj ".vbs - Bljižnica v zagon (startup) win + r shell:startup


3 KAJ MORATE SPREMENITI

Ko naložite vse priložene datoteke v določeno mapo
V mapo morate prilepiti .pdf. Datoteko zaščiteno z geslom preimenujte v unlock.pdf







Ko je vse naloženo in deluje, desni klik na mapo in skrij mapo



