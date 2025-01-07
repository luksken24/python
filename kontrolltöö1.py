"""
#Ül 1 

#sisemine_haal.py

#kasutaja sisend 
sisend = input("Palun sisestage oma tekst: ")

#Sisend väikeste tähtedega 
Väiksed_tähed = sisend.lower()

#Väljend
print = ("teie tekst väikeste tähtedega: ", Väiksed_tähed)
"""
#Ül 6
# Küsi kasutajalt faili nime
failinimi = input("Palun sisestage faili nimi: ")

# Muudame faili nime väikesteks tähtedeks
failinimi_lower = failinimi.lower()

#  muutuja
meediatüüp = "application/octet-stream"

# Kontrollime
if failinimi_lower.endswith('.gif'):
    meediatüüp = 'image/gif'
elif failinimi_lower.endswith('.jpg'):
    meediatüüp = 'image/jpeg'
elif failinimi_lower.endswith('.jpeg'):
    meediatüüp = 'image/jpeg'
elif failinimi_lower.endswith('.png'):
    meediatüüp = 'image/png'
elif failinimi_lower.endswith('.pdf'):
    meediatüüp = 'application/pdf'
elif failinimi_lower.endswith('.txt'):
    meediatüüp = 'text/plain'
elif failinimi_lower.endswith('.zip'):
    meediatüüp = 'application/zip'

# Väljasta meediatüüp kasutajale
print(f"Faili '{failinimi}' meediatüüp on: {meediatüüp}")

"""
#Ül 10

# Palume kasutajal sisestada tekst
user_input = input("Palun sisestage tekst: ")
    
# Eemaldame täishäälikud
ilma_taishaalikuteta = user_input.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
ilma_taishaalikuteta = ilma_taishaalikuteta.replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")
    
# Väljastame tulemuse
print("Tekst ilma täishäälikuteta:", ilma_taishaalikuteta)
"""