#Kontrolltöö
#06.11.24
#Neljas
import turtle 

d = 100

for i in range (1):
    turtle.lt(360/5)
    for i in range (5):
        turtle.lt(360/5)
        turtle.fd(50)
        for i in range(1):
            turtle.left(90)
            turtle.fd(d)
            turtle.left(90)
            turtle.fd(d)
            turtle.left(90)
            turtle.fd(d)
            turtle.left(90)
            turtle.fd(50)



turtle.done()