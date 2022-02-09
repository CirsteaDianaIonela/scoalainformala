import random

def joc():

    msg = " "

    jucator = input("Your name is: ")

    variante = ["foarfeca", "piatra", "hartie"]

    alegere = input("Alege o varianta: ")

    optiuni_calculator = random.choice(variante)

    if alegere=="foarfeca" and optiuni_calculator=="foarfeca" or alegere=="piatra" and optiuni_calculator=="piatra" or alegere=="hartie" and optiuni_calculator=="hartie":
        msg = "Remiza"

    elif alegere=="foarfeca" and optiuni_calculator=="piatra":
        msg="Piatra bate foarfeca, ai pierdut!"

    elif alegere=="foarfeca" and optiuni_calculator=="hartie":
        msg = f'Foarfeca taie hartia, ai castigat {jucator}!'

    elif alegere=="piatra" and optiuni_calculator=="hartie":
        msg = f'Hartia impacheteaza piatra, ai pierdut {jucator}!'

    elif alegere=="hartie" and optiuni_calculator=="foarfeca":
        msg = f'Foarfeca taie hartia, ai pierdut {jucator}!'

    elif alegere=="hartie" and optiuni_calculator=="piatra":
        msg = f'Hartia impacheteaza piatra, ai castigat {jucator}!'

    elif alegere=="piatra" and optiuni_calculator=="foarfeca":
        msg = f'Piatra bate foarfeca, ai pierdut, {jucator}!'

    return optiuni_calculator,msg

optiuni, mesaj = joc()
print(f'Optiunea calculatorului a fost {optiuni}\n', mesaj)

joc_nou = input("Vrei sa joci din nou? y/n")

while joc_nou == "y":
    optiuni, mesaj = joc()
    print(f'Optiunea calculatorului a fost {optiuni}\n', mesaj)

    joc_nou = input("Vrei sa joci din nou? y/n")








