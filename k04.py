#16.10.24
#ülesanne 04
import turtle

#5 ringi pindala ja turtle 
try:
    r = int(input("lisa ringi raadius: "))
    pi = 3.14
    s = pi * r ** 2
    p = 2 * pi * r
    print(f"Ringi pindala on {s:.2f} ja ümbermõõt on {p:.2f}")
    turtle.circle(r, 360)
except:
    print("tegid sisestamisel vea!")    





#4 kingituste pakkimine
try:
    kingitused = int(input("Lisa kinkide arv: "))
    maht = 5
    pakid = kingitused // maht 
    yle = kingitused % maht
    prtint(f"Saad teha {pakid} täis kinkekastid. Üle jääb {yle} kingitust")	
except:
    print("tegid sisestamisel vea!")



#3 faili harjutus
try:
    failinimi = int(input("Sisesta faili nimi: "))
    downkiirus = int(input("Sisesta allalaadimise kiirus (MB/s): "))
    aeg = failisuurus / downkiirus
    print(f"Allalaadimiseks kulub {aeg:0.2f} sekundit")
except:
    print("tegid sisestamisel vea!")



#2. raamatute allahindlus 
ale = 0.3
kogus = 3
hind = 12.53
summa = hind - (hind * ale) * kogus 
print(f"{kogus} raamatu hind soodustusega on {summa:0.2f}€")


#1.aia pikkus
a = int(input("sisesta külg 1: "))
b = int(input("sisesta külg 2: "))
p = 2 * (a + b)
print(f"Aia kogupikkus on {p} meetrit")

turtle.done()