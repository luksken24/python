#Ken Luks 08.10.24
#harjutus2.3

import turtle

"""
Ülesanne 3.1: Tervitus
Loo muutuja nimi, mis sisaldab kasutaja nime (string)
Loo muutuja vanus, mis sisaldab kasutaja vanust (integer)
Loo muutuja keskmine_hinne, mis sisaldab kasutaja keskmist hinnet (float)
Trüki välja lause, mis ühendab kõik kolm muutujat, nt: “Karin, 18 aastat vana ja keskmine hinne on 4.7”
"""
nimi="üllar"
vanus=18
keskmine_hinne=4.7
print(nimi+", "+str(vanus)+" aastat vana ja keskmine hinne on"+str(keskmine_hinne))

"""
Ülesanne 3.2: Ostunimekiri
Loo muutuja toode, mis sisaldab toote nime (string)
Loo muutuja kogus, mis näitab, mitu toodet soovitakse osta (integer)
Loo muutuja hind, mis näitab ühe toote hinda (float)
Trüki välja lause, mis ühendab need andmed, nt: “Soovin porgandeid 3, mille tüki hind on 5 eurot.”
"""
toode="porgand"
kogus=3
tüki_hind=5
print(toode+", "+str(kogus)+" tükki mille tüki hind on"+str(tüki_hind))

"""
Ülesanne 3.6: Python Turtle
Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
Loo muutuja kujundi_varv, mis määrab kujundi täitevärvi (string)
Kasutades Turtle’i, joonista kõrvuti värvilised kujundid ruut ja kolmnurk, mis kasutab loodud muutujai
"""

k = 100
varv = "green"

#ruut
turtle.color(varv)
turtle.fd(k)
turtle.left(90)
turtle.fd(k)
turtle.left(90)
turtle.fd(k)
turtle.left(90)
turtle.fd(k)
turtle.left(90)


#liigu
turtle.penup()
turtle.goto(k*1.5,0)
turtle.pendown()

#kolmnurk
turtle.fd(k)
turtle.left(120)
turtle.fd(k)
turtle.left(120)
turtle.fd(k)
turtle.left(120)


turtle.done()


