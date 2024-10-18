# ülesanne5 
# 18.10.24 Ken Luks
import random

#4. Mündiviskamise äraarvamine koos juhuslikkusega (and ja or)
# 1 kull
# 0 kiri
suv = random.randint(0,1)
kasutaja_valik = input("kiri või kull")
if (suv ==1 and kasutaja_valik =="kull") or (suv == 0 and kasutaja_valik == "kiri"):
    color = "green"
else:
    color = "red"

print(suv)
turtle.color(color)
turtle.circle(50, 360)
turtle.done()




#3. Matemaatika test (randint)
a, b = random.randint(1, 10) , random.randint(1, 10)
vastus = int(input(f"Lisa vastus {a} * {b} = "))
if vastus == a * b:
    print("Õige vastus!")
else: 
    print("Vale vastus!")    
    



#2. Ilmaennustuse rakendus (and)
c = 15
if c < 0:
    print("talveriided!")
elif c >= 0 and c <=10:
    print("kevad-sügis ")
else:
    print("suvi!")        





#1. Vanusepiiranguga üritus
vanus = 18
if vanus >= 18:
    print("saad sisse!")
else:
    print("Liiga noor!") 
