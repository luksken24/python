# Ken Luks 8.11.24
# Harjutus 11


def pikim_sona(*sonad):
    pikkim = 0
    for i in sonad:
        if len(i)>pikim:
            pikim=len(i)
        print(f"pikim sõna on {pikim} märki!")
        


pikim_sona("ükas", "kaks", "kolmkümmend")
