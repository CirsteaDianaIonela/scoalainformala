#Reguli spanzuratoarea
#daca primul caracter si ultimul se repetau in cuvant, caracterul trebuia afisat
#restul catacterelor erau ascunse
#7 sanse de a ghici cuvantul
#word  o_o___o_ee
word = "onomataopee"
# litera_cuvant = input("Alege o litera")
# print(litera_cuvant)

lista_cuvant = []
for iterator in word:
    lista_cuvant.append("_")
    if iterator == word[0] or iterator == word[-1]:
        lista_cuvant[-1] = iterator
print(" ".join(lista_cuvant))
numar_incercari = 1
lista_litere_incercate = []
while numar_incercari <= 7:
    litera = input("Alege o litera: ").lower()
    if litera.lower() in word.lower():
        for index, valoare in enumerate(word):
            if valoare.lower() == litera.lower():
                lista_cuvant[index] = litera
    else:
        lista_litere_incercate.append(litera.lower())
        numar_incercari += 1
        print(f'Litera nu exista, deja ai incercat urmatoarele litere {",".join(lista_litere_incercate)}')
        print(f'Mai ai {7-numar_incercari} incercari')
        if litera not in lista_litere_incercate:
    if 9 - int(numar_incercari) == 0:
        print(f"Ai pierdut! Cuvantul era {word}")
    elif " ".join(lista_cuvant) == word:
        print("Ai castigat!")
        break
        print("De adaugat in lista cuvant")
        lista_litere_incercate.append(litera)
    print(" ".join(lista_cuvant)


