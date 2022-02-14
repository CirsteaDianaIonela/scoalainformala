#map = modifica fiecare element al unei liste
# def adunare(n):
#     return n+n
#

# lista_numere = [1,2,3,4]
# rezultat = map(adunare, lista_numere)
# print(list(rezultat)) #a inlocuit fiecare element din lista cu ce i-am zis noi la return
#


# lista_numere = [1,2,3,4]
# rezultat = map(lambda n: 2*n, lista_numere)
# print(list(rezultat))




# lista_numere = [1,2,3,4]
# lista_numere2 = [5,6,7,8]
# rezultat = map(lambda n,m: n+m, lista_numere,lista_numere2)
# print(list(rezultat))



#cea cu 2 liste de mai sus prin functie, unde listele au acelasi nr de parametrii:
#
# lista_numere = [1,2,3,4]
# lista_numere2 = [5,6,7,8]
# def adunare(lista_numere, lista_numere2):
#     suma=0
#     lista_adunare = []
#     for i, v in enumerate(lista_numere): #i este indexul, v este valoarea
#         for j, w in enumerate(lista_numere2):
#             suma = v + w
#             if i == j: #indecsii din ambele liste sa fie egali
#                 lista_adunare.append(suma)
#     return lista_adunare
#
# print((adunare(lista_numere,lista_numere2)))
#



#cea cu 2 liste de mai sus prin functie, unde listele nu au acelasi nr de parametrii:
#
lista_numere = [1,2,3,4,9]
lista_numere2 = [5,6,7,8]
rezultat = map(lambda n,m:n+m, lista_numere, lista_numere2)
def adunare(lista_numere, lista_numere2):
    suma=0
    lista_adunare = []
    for i, v in enumerate(lista_numere): #i este indexul, v este valoarea
        for j, w in enumerate(lista_numere2):
            suma = lista_adunare[i] + lista_numere2[j]
            suma = v + w
            if i == j:
                lista_adunare.append(suma)
    return lista_adunare

print((adunare(lista_numere,lista_numere2)))



