import random

vygenerovana_cisla = []
postupka = [1,2,3,4,5,6]



body = 0
pocitadlo_dvojic = 0


print("Vítej, tento program má simulovat hru kostky.")
input("Pokud chceš začít házet zmáčkni ENTER ")

for i in range(1,7):
    cislo = random.randint(1,6)
    vygenerovana_cisla.append(cislo)

print(f"hodil jsi kostkou a tvá čísla jsou: {vygenerovana_cisla}")


if sorted(vygenerovana_cisla) == postupka:
    print("gratuluji k postupce, získáváš 1500 bodů")
    body += 1500
else:

    if vygenerovana_cisla.count(1) == 1:
        body += 100
        print("Dostal jsi 100 bodů za 1x jedničku")
    
    elif vygenerovana_cisla.count(1) == 6:
        body += 8000
        print("dostal jsi: 8000 bodů za 6x jedničku")
    elif vygenerovana_cisla.count(1) == 5:
            body += 4000
            print("dostal jsi: 4000 bodů za 5x jedničku")
    elif vygenerovana_cisla.count(1) == 4:
            body += 2000
            print("dostal jsi: 2000 bodů za 4x jedničku")
    elif vygenerovana_cisla.count(1) == 3:
            body += 1000
            print("dostal jsi: 1000 bodů za 3x jedničku")

    if vygenerovana_cisla.count(5) == 1:
        body += 50
        print("Dostal jsi 50 bodů za 1x pětku")
    
    for i in range(1,7):
        if pocitadlo_dvojic == 3:
            print("3 dvojice vyhráváš 1000 bodů")
            body += 1000
            break

        elif vygenerovana_cisla.count(i) == 2:
            pocitadlo_dvojic += 1

        if i != 1:    
            if vygenerovana_cisla.count(i) == 6:
                body += (i*800)
                print(f"dostal jsi: {i} * 800 bodů tedy: ",i*800)
            elif vygenerovana_cisla.count(i) == 5:
                body += (i*400)
                print(f"dostal jsi: {i} * 400 bodů tedy:",i*400)
            elif vygenerovana_cisla.count(i) == 4:
                body += (i*200)
                print(f"dostal jsi: {i} * 200 bodů tedy:",i*200)
            elif vygenerovana_cisla.count(i) == 3:
                body += (i*100)
                print(f"dostal jsi: {i} * 100 bodů tedy:",i*100)

print(f"celkem si získal: {body} bodů ")
input("Pro ukončení programu zmáčkni ENTER ")
        