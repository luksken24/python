
#10. Kaugushüpe

def main():
    print("Tere, sisestage kaugushüppe tulemused ")










#1. Korrutamise kontrollimine

#kümmne ül esitamine
# import random

# for i in range (10):
#     arv1 = random.randint (1, 10)
#     arv2 = random.randint (1, 10)
#     õige_vastus = arv1 + arv2

#kasutaja vastus
# Kasutaja_vastus = int(input(f"{arv1} * {arv2} = "))


# if Kasutaja_vastus == õige_vastus:
#     print ("Õige!")
# else:
#     print (f"Vale. Õige vastus on {õige_vastus}")



"""

#11. Salakeel
import base64
try:
    soov = input ("kas sa soovid sala keelt luua või tõlkida")

"""

"""
#16. Täringud
import random

def viska_taringut():
    return random.randint(1, 6) + random.randint(1, 6)

def main():
    # Küsi kasutajalt nime
    kasutaja_nimi = str(input("Sisesta oma nimi: "))


#mängu raha 
kasutaja_raha = 100
arvut_raha = 100

print("{kasutaja_nimi}, sul on {kasutaja_raha} eurot") 
print(f"arvutil on {arvut_raha} eurot")

#mängu tsükkel
while kasutaja_raha > 0 and arvut_raha > 0 :
    pakkumine = int(input("Sisesta oma pakkumine (0- raha, mis sul on): "))
    if pakkumine < 0 or pakkumine > kasutaja_raha:
        print("vale pakkumine! Palun proovi uuesti.")

#viskas täringu
kasutaja_tulemus = viska_taringut()
arvut_tulemus = viska_taringut()

print("{kasutaja_nimi} viskas {kasutaja_tulemus} punkti.")
print(f"Arvuti viskas {arvut_tulemus} punkti.")

#määrake võitja
if kasutaja_tulemus > arvut_tulemus:
    print(f"{kasutaja_tulemus} võitis! Sa saad {pakkumine} eurot.")
    kasutaja_raha += pakkumine
    arvut_raha -+ pakkumine
elif arvut_tulemus > kasutaja_tulemus:
    print(f"Arvuti võitis! Sa kaotasid {pakkumine} eurot.")
    kasutaja_raha -= pakkumine
    arvut_raha += pakkumine
else:
    print("Viik! Raha jääb lauale") 

#mängu lõpp
if kasutaja_raha <= 0:
    print("Sa kaotasid kõik oma raha! Mängu lõpp")
else:
    print("Arvuti kaotas kõik raha! Sa võiysid")


if __name__ == "__name__":
    main()
"""







# # #14. Palkade võrdlus

töötad = {"Hubert Hunt m 2340"
	"Siim Siil m 2570"
	"Märt Mäger m 1960"
	"Vilma Vihmauss n 2060"
	"Merike Metskits n 2250"
	"Kati Karu n 2370"
	"Elmar Elevant m 2900"
	"Timoteus Tigu m 2850"
	"Reet Rebane n 2340"
	"Kalev Kaamel m 2570"
	"Karmen Kass n 2120"
	"Kornelius Koer m 2250"}

#eralda meeste ja naiste palgad
meeste_palk  = 
naiste_palk = 






