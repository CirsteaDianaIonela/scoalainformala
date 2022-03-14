# 1. Scrie un program care sa calculeze suma dintre trei numere. Daca valorile sunt egale, returnati de trei ori suma acestora.(1 punct)

def suma_numere(a, b , c):
    suma = 0
    if a == b and a == c:
        suma = (a+b+c)*3
    else:
        suma = a+b+c
    return suma


print(suma_numere(2, 2, 2))