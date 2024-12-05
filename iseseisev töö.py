"""
#1.1
print ("Tere, Maailm!")

#1.2
aasta = 2020
liblikas = ("teelehe-mosaiikliblikas")
lause_keskosa = ("aasta liblikas on")
lause = str(aasta) + (lause_keskosa) + (liblikas)
print(lause)

#1.3

kõrgeim = (6)
keskmine = (2-6)
alumine = (2)

korgus = float(input("pilvede aluse kõrgus: "))
if korgus > 6:
    print ("Need on ülemised pilved")
else:
    print ("Need ei ole ülemised pilved")


#1.4

num_inimesed = int(input("sisedta inimeste arv"))
kohtade_arv = int(input("sisesta bussi kohtade arv"))

busside_arv = num_inimesed / kohtade_arv
Viimase_Bussi_inimesed = num_inimesed % kohtade_arv

if Viimase_Bussi_inimesed >0:
    busside_arv +1
print(f"kohtade_arv" (busside_arv))
else: 
print(f"")



#2.2

ringide_arv = 6
porgandite_arv = 0
ringide_arv = int(input("Sisesta ringide arv"))
while i <=ringide_arv:
    if i%2==0:
        porgandite_arv+=i
        print (i)
    i +=1
print ("porgandite_koguarv on : {porgandite_arv}")


#2.3
import random 
taringute_arv = 5
for i in range (taringute_arv):
    print (random.randint(1,6))

#2.4


taisarv = 10
nisutera = 0
korda = taisarv

if taisarv > 64:
    print("Nii palju ruute ei ole")

if taisarv >=1:
    nisutera+=1
    taisarv-=1
korda
while taisarv >= 1:
    nisutera *=2
    korda -=1

print (taisarv+" "+)


#2.5
import random
oun = 14
poisse = 3
for i in range(poisse):
    oun -= (random.randint(1,2))
    print (oun)


#3.1

fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

c
    vastuvõetud.append(int(rida))
print(vastuvõetud)
fail.close() 

a = input("palun sisestage, millise aasta andmeid vajate?: ")


print(vastuvõetud{int(a[3])-1})
"""


#3.2

fail = open("rebased.txt", encoding="UTF-8")

for rida in fail :
    if int(rida) > 0:
        print(rida,end="")







