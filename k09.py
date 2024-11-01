# 24.20.24 Luks
# ülesanne 09
"""
# Genereeri ja kuva arvud 1-20
for i in range(1,21):
    print(i, end=" ")
print()
import random
# Genereeri ja kuva 20 suvalist arvu vahemikus 1-99
# import random
# random.randint(min, max)
for i in range(1,21):
    print(random.randint(14, 99), end=" ")

print()

# Kasuta loendit 60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75
# Leia paaris ja paaritud arvud ning lisa oma loendisse
# Kuva paaris ja paritute arvude summad
loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
paaris = []
paaritud = []

for i in loend:
    if i % 2 == 0:
        paaris.append(i)
    else:
        paaritud.append(i)
   
print(f"paarisarvude summa on: {sum(paaris)}")
print(f"paaritutearvude summa on: {sum(paaritud)}")

print()


# Kuva arvud 1-42
# Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
# Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
# Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)

for i in range(1,43):
    if i%3 == 0 and i%5 == 0:
        print(i,"TIKTAK", end= "")
    elif i%3 == 0:
        print(i,"TIK", end= "")
    if i % 3 ==0 :
        print(i,"TIK", end= "")
    elif i % 5 == 0:
        print(i,"TAK", end= "")
    else:
        print(i, end=" ")

print()
"""





# Leia kõik arvud vahemikus 200 kuni 320, mis jaguvad 7-ga, kuid ei jagu 5-ga. Prindi need arvud komadega eraldatult ühele reale.

# kuva nimekirja unikalsed alusd 
nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
unimed = []

for nimi in nimed:
    if nimi not in unimed:
        unimed.append(nimi)

print(unimed)


#Sulle on saadetud õpilaste keskmised hinded, mille lisasid loendisse. Eralda hinded ning leia kogu rühma parim ja kehvem tulemus ning keskmine hinne.
ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
meeles = []



for opilane in ryhma_hinded:
    meeles.append(float(opilane.split()[1]))

print(f"parim tulemus {max(meeles)}")
print(f"halvim tulemus {min(meeles)}")
print(f"halvim tulemus {round(sum(meeles)/len(meeles),2)}")






#Koosta programm, mis genereerib ja kuvab korrutustabeli, kus iga number korrutatakse iseendaga:
#Näiteks:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
# for i in range(11):
    # print(f"{i} x {i} = {i*i}")



#Loo programm, mis loob suvalised tehted 1-100 arvudega.
#Kasuta tsükli puhul alakriipsu
#kasuta suvalise tehte märgi jaoks loendit ja sealt suvalise märgi leidmiseks random.choice()
#Näiteks:
#7 – 2=
#45 * 69=
#71 – 45=
tehted = ["+", "-", "*", "/"]
import random   
for i in range(6):
    j = random.randint(1,10)
    k = random.randint(1,10)
    tehe = random.choice(tehted)
    if tehe == "+":
        print(f"{j} {tehe} {k} = {j*k}")