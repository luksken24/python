# 22.10.24 Ken Luks
# ülesanne 07 loendid


"""
nimed = ["madis", "kristjan", "kristi","Kati"]


muusika = ['ALIKA – "Bridges”' ,'Anett x Fredi – "Read Between The Lines”','villemdrillem – "leekiv armastus”','Clicherik & Mäx – "PAKSUD”','nublu – "ära ärata”','NOËP – "Move Your Feet”','Trad.Attack! – "Bring It On”','Bedwetters – "It Is What It Is”','Reket – "Panama paberid”','Grete Paia – "Võluväel”',]
print(muusika)           
for i in range (len(muusika)):
    print(str(i+1) + ". " + muusika[i])

try:
    valik = int(input("Vali laul: "))
    print(f"Mänig lugu {muusika[valik-1]}")
except:
    print("Midagi läkas katki. teavita adminit")
"""
# tanane kuu nr
import datetime
x = datetime.datetime.now()
tana = int(x.strftime("%m")) - 1 # -1 et loendiga ühildada


# 12 kuud
kuud = [["jaanuar",21,-8,0,24,18,7,0,-19,13,5,23,-2,18,7,12,11,18,17,-11,9,5,6,-19,-9,-11,22,30,25,18,-19,-5],
["veebruar",-17,-10,-17,30,15,27,-3,-7,-1,-2,-14,20,29,7,-4,-13,26,28,2,-2,-20,29,-6,-17,20,24,11,9],
["märts",-4,4,4,12,12,16,19,-19,29,-17,-12,7,-3,11,21,6,10,1,-17,-4,-16,-14,-20,21,9,-14,-10,9,23,-11,20],
["aprill",15,22,-19,-13,8,-5,11,0,-14,27,-17,13,8,1,6,-1,25,22,22,-15,25,16,24,-4,12,-5,13,-19,26,-5],
["mai",12,28,17,-18,-15,6,9,4,-12,19,-9,-19,3,16,-8,-2,3,28,15,9,-19,-15,-13,15,13,6,23,-18,-4,28,15],
["juuni",29,30,29,0,27,-9,12,-2,-12,6,13,-18,11,9,25,5,0,27,26,-9,3,6,-3,26,-17,18,-20,1,-11,10],
["juuli",2,26,-5,-9,14,-19,21,22,15,-10,20,0,11,13,10,-4,9,15,23,-17,-16,19,18,23,20,28,3,-18,-5,-20,-20],
["august",1,30,-15,9,-17,25,8,-18,7,27,-16,18,-18,17,3,19,11,-1,-13,5,-3,11,-16,17,10,-2,22,-5,-13,1,11],
["september",-18,21,-13,9,9,-10,28,0,-14,-4,-1,-5,-8,-8,29,3,-8,-15,6,15,6,-5,-11,23,-3,-9,-13,23,1,-17],
["oktoober",-8,15,-19,-9,16,8,6,23,4,6,30,24,-18,-11,27,-19,-15,10,-8,14,-16,-3,10,0,1,8,-11,20,8,19,14],
["november",13,-6,21,-4,20,15,-1,22,-5,10,20,14,12,-15,-8,18,26,18,-7,-17,12,5,9,19,-20,16,-7,-11,19,13],
["detsember",9,16,-17,4,19,30,15,-8,-16,-16,14,-19,20,6,30,16,-16,27,-12,19,22,22,-12,14,20,7,-6,8,-14,-13,17]]


# ülesanded

print(kuud[tana][0])
print (f"viimane mõõtmine sellel kuul: {kuud[tana][len(kuud[tana])-1]}")
ajutine = []
for i in range (len(kuud[tana])-1):
    ajutine.append(kuud[tana][i+1])
    print(kuud[tana][i+1], end=", ")
print(f"Max temp: {max(ajutine)}")
print(f"min temp: {min(ajutine)}")
print(f"keskmine temp: {round(sum(ajutine)/len(ajutine),2)}")

print(ajutine)
print(f"-20 esineb {ajutine.count(ajutine,-20)} korda")

ajutine.pop(5)
print(ajutine)





