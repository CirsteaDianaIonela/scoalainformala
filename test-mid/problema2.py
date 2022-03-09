# 2. Scrie un program care sa elimine si sa printeze numerele din 3 in 3 pana cand lista devine goala. (1 punct)
#
# Lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
dimensiune_lista = len(lista)

while dimensiune_lista>2:
    del lista[0:13:3]
    dimensiune_lista = len(lista)
    print(lista)

if dimensiune_lista<3:
    lista.clear()
    print(lista)


