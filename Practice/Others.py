# scopul este sa afisez "Buna! Numele meu este Diana si am 26 de ani"
# name = "Diana"
# age = "26"
#
# # print("Numele meu este "+ name + " si am " +age + " de ani")
# print(f'Numele meu este {name} si am {age} de ani')

# lista1=[1,2,3,4,5]
# print(lista1)
# lista2=lista1.copy()
# lista2[1]=7
# print(lista2)
# print(lista1)
# lista1.append(999)
# print(lista1)
# lista3=lista1+lista2
# print(lista3)
# print(lista1.index(4))


# lista_noua=[1,3,2]
# # print(sorted(lista_noua))
# lista_noua2=sorted(lista_noua)
# # print(lista_noua2)
# lista_noua3=lista_noua2
# lista_noua3.sort(reverse=True)
# print(lista_noua3)
# print(len(lista_noua3))
#
# print(list(range(1,100)))
# # print(list(range(1,100,2)))
# lista1=[1,2,3,6]
# print(len(lista1))

# exercitiu=list(range(1,10,4))
# print(exercitiu)
#
# #dictionare
# def test():
#     dictionar1={ "cheie1": "a", "cheie2": list(range(1,30))}
# # # print(dictionar1.values())
# # print(dictionar1["cheie1"][0])
# #     print(dictionar1)
#     n=3
#     if n not in dictionar1["cheie2"]:
#         print(False)
#         break
#     else:
#         print(True)
# print(test())
#
# is_magician =False
# is_expert = True
# if is_magician and is_expert:
#     print("you are a master magician")
# elif is_magician and not is_expert:
#     print("at least")
# else:
#     print("you need magic power")


# for z in [1,2,3,4]:
#     print(z)
#
# my_list = [1,2,3,4,5,6,7,8,9,10]
# counter = 0
# for item in my_list:
#     counter = counter + item
# print(counter)
#
# i=5
# while i<20:
#     i=i+5
#     print(i)
# some_list = ["a","b","c","b","d","m","n","n"]
# print((some_list).count("b"))
#

#scop: de printat numerele mai mari de 10
# lista_numere=[1,10,34,65,3,4,99,22]
# lista_noua=[]
# for item in lista_numere:
#     if item>50:
#         lista_noua.append(item)
# print(lista_noua)

# ● Să se scrie o funcție care citește de la tastatură și returnează valoarea
# dacă aceasta este un număr întreg, altfel returnează valoarea 0.

# def functie():
#     nr_introdus=input("Spune-mi o valoare: ")
#     value=nr_introdus
#     if value.isnumeric():
#         print(value)
#     else:
#         print("0")
# print(functie())

#a3a incercare
    # def functie():
    #     lista_introdusa = []
    #     variabila = input("Spune-mi o valoare: ")
    #     for item in variabila:
    #         if int(variabila) is True:
    #             lista_introdusa.append(variabila)
    #         else:
    #             print("0")
    # print(functie())
#
# import datetime
# CNP = input("Introdu CNP-ul: ")
# CNP_introdus = list(CNP)
# data = slice(1, 7, 1)
# judet = slice(7, 9, 1)
# data_nasterii = CNP[data]
# msg = " "
#
# def lungime():
#     if len(CNP_introdus) == 13:
#         msg  = "CNP valid"
#     else:
#         msg = "CNP invalid"
# #
# #     return msg
# # print(lungime())
# #
# #
# # def S():
# #      if CNP_introdus[0] == 0:
# #          msg = "CNP invalid"
# #      else:
# #          msg = "CNP valid"
# #      return msg
# # print(S())
# #
# # def AA_LL_ZZ():
# #     msg = " "
# #     data = slice(1, 7, 1)
# #     data = data_nasterii
# #     try:
# #         datetime.datetime.strptime(data, "%y%m%d")
# #         return True
# #     except ValueError:
# #         return False
#
#
# # if lungime()==True and S()==True:
# #     msg = "CNP valid"
# #     print(msg)
# # else:
# #     msg = "CNP invalid"
# #     print(msg)
#
#
#
# import datetime
# CNP = input("Introdu CNP-ul: ")
# CNP_introdus = list(CNP)
# data = slice(1, 7, 1)
# judet = slice(7, 9, 1)
# data_nasterii = CNP[data]
# msg = " "
#
# def lungime():
#     if len(CNP_introdus) == 13:
#         return True
#
# def S():
#      if CNP_introdus[0] != "0":
#          return True
#
# def AA_LL_ZZ():
#     data = slice(1, 7, 1)
#     data = data_nasterii
#     try:
#         datetime.datetime.strptime(data, "%y%m%d")
#         return True
#     except ValueError:
#         return False
#
# def JJ():
#     jud = ['01', 'Alba', '02', 'Arad', '03', 'Arges', '04', 'Bacau', '05', 'Bihor', '06', 'Bistrita-Nasaud', '07',
#            'Botosani', '08', 'Brasov', '09', 'Braila', '10', 'Buzau', '11', 'Caras-Severin', '12', 'Cluj', '13',
#            'Constanta', '14', 'Covasna', '15', 'Dambovita', '16', 'Dolj', '17', 'Galati', '18', 'Gorj', '19',
#            'Harghita', '20', 'Hunedoara', '21', 'Ialomita', '22', 'Iasi', '23', 'Ilfov', '24', 'Maramures', '25',
#            'Mehedinti', '26', 'Mures', '27', 'Neamt', '28', 'Olt', '29', 'Prahova', '30', 'Satu-Mare', '31', 'Salaj',
#            '32', 'Sibiu', '33', 'Suceava', '34', 'Teleorman', '35', 'Timis', '36', 'Tulcea', '37', 'Vaslui', '38',
#            'Valcea', '39', 'Vrancea', '40', 'Bucuresti', '41', 'Bucuresti-S1', '42', 'Bucuresti-S2', '43',
#            'Bucuresti-S3', '44', 'Bucuresti-S4', '45', 'Bucuresti-S5', '46', 'Bucuresti-S6', '51', 'Calarasi', '52',
#            'Giurgiu']
#
#     judet = slice(7, 9, 1)
#     judet_n=CNP[judet]
#     while judet_n in jud:
#         return True
#
# def cifra_de_control():
#         nr_control = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
#         val = sum(a * int(b) for a, b in zip(nr_control, CNP_introdus)) % 11
#         return '1' if val == 10 else str(val)
#
# def caractere_cnp():
#     if CNP.isdigit():
#         return True
#
# if lungime()==S()==AA_LL_ZZ()==JJ()==caractere_cnp()==True and cifra_de_control() == CNP_introdus[12]:
#     msg = "CNP valid"
#     print(msg)
# else:
#     msg = "CNP invalid"
#     print(msg)

# # LAMBDA
#
# my_lambda = lambda x,y : x+y
#
# suma = my_lambda(2,3)
# # print(suma)
#
# def my_lambda(x,y):
#     return x + y
# print(my_lambda(2,3))


# my_lambda_diff = lambda x,y: x-y
# diferenta = my_lambda_diff(5,3)
# print(diferenta)
#
# players = [
#     {
#         "first_name": "Ion",
#         "last_name": "Gheorghe",
#         "varsta": 43
#
# },
#     {
#         "first_name": "Andreea",
#         "last_name": "Popa",
#         "varsta": 99
#     },
#
#     {
#         "first_name": "Cucu",
#         "last_name": "Enache",
#         "varsta": 25
#     }
# ]

# # jucatori_sortati = sorted(players, key = lambda jucator: jucator["varsta"])
# # print(jucatori_sortati)
# jucatori_sortati = sorted(players, key=lambda juc: juc["first_name"])
#
# print(jucatori_sortati)
#
# my_lamda = lambda x,y: x+y
# suma = my_lamda(100,99)
# # print(suma)
#
# def adunare(n):
#     return n+n
#
# lista_numere = [1,2,3,4]
# rezultat = map(adunare, lista_numere)
# print(list(rezultat))
#
# adunare = lambda x,y,z,t:
#

# def functie_recursiva (*lista):
#     try:
#         nr_introdus = int(input("Spune-mi valoarea lui n: "))
#         valoare_introdusa = nr_introdus
#         suma_totala = sum([item for item in lista])
#         print(valoare_introdusa,suma_totala)
#     except ValueError:
#         print("Trebuie sa introduci un numar intreg!")
#
#     #
#     #
# #     #
# #     # return valoare_introdusa, suma_totala
# functie_recursiva()
# print(functie_recursiva())






    # print()
    # suma_totala = 0
    # for item in lista:
    #     suma_totala = suma_totala+item
    # return suma_totala
    # try:
    #     nr_introdus = int(input("Spune-mi valoarea lui n: "))
    #     valoare_introdusa = nr_introdus
    #     suma_totala = 0
    #     for item in lista:
    #         suma_totala = suma_totala + item
    #     print(suma_totala)
    # except ValueError:
    #     print("Trebuie sa introduci un numar intreg!")

    #
    #
#     #
# #     # return valoare_introdusa, suma_totala
#     return suma_totala
#
# print(functie_recursiva())


# def numbers_sum(*var):
#     suma = 0
#     for item in var:
#         suma = suma + item
#     return suma
# print
# (numbers_sum(1,2,3,4,5))


# def functie_recursiva():
#
#     nr_introdus = int(input("Spune-mi valoarea lui n: "))
#     valoare = nr_introdus
#     suma_totala = 0
#     for item in range(valoare + 1):
#         suma_totala = suma_totala + item
#
#
#     suma_pare = 0
#     for item in range(valoare + 1):
#         if item % 2 == 0:
#             suma_pare = suma_pare + item
#
#     suma_impare = 0
#     for item in range(valoare + 1):
#         if item % 2 != 0:
#             suma_impare = suma_impare + item
#
#
#     return suma_totala, suma_pare, suma_impare
#
# print(functie_recursiva())
import csv
import json
# x = '{"1":"2"}'
# y = json.loads(x)
# print(y, type(y))
#
#
# a = "hello"
# print(a, type(a))









# def introducere_tasks(*lista_taskuri):
# lista_tasks = []
# task_introdus = input("Introdu un task de la tastatura")
# lista_tasks.append(task_introdus)
# print(lista_tasks)
# # return True
#
# # def introducere_responsabil(*lista_responsabili):
# lista_responsabili =[]
# responsabil_introdus = input("Introdu responsabilul de task")
# lista_responsabili.append(responsabil_introdus)
# print(lista_responsabili)
#     # return True
#
#
# # def reintroducere_elemente (*lista):
# alt_task = input("Mai aveti task-uri de introdus? y/n")
# if alt_task == "n":
#     print(lista_tasks)
# else:
#     task_nou_introdus = input("Introdu urmatorul task de la tastatura")
#

# variabila = "Ana"
# variabila_2= "are"
# variabila_3 ="mere"
# convertire = list(variabila, variabila_2, variabila_3)
# # print(convertire)
# var = 1
# while var < 5:
#     var += 1
#     print("a mers", var)
#


# 1.
# In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
#done
#
# 2.
# Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
# string, int, float, bool
# Valorile le alegeti voi dupa preferinte
#
#
# 3.
# Utilizat functia type pentru a verifica daca au tipul de date asteptat
# var1 = "a"
# print(type(var1))
#
# 4.
# Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
# Verificati tipul acesteia

# a = 1.1
# a=round(a)
# print(type(a), a)

#
# 5.
# folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
# (rezolvati nepotrivirile de tip prin ce modalitate doriti)


#
# 6.
# citeste de la tastatura numele,
# citeste de la tastatura prenumele
# afiseaza 'Numele complet are x caractere'
#
# nume = "Diana"
# prenume = "Cirstea"
# nr_caractere = len(nume) + len(prenume)
# print( f'Numele complet are {nr_caractere}')
# #
# 7.
# citeste de la tastatura lungimea
# citeste de la tastatura latimea
# afiseaza 'Aria dreptunghiului este x'
# lungime = 6
# latimea = 7
# aria = lungime*latimea
# print(f'Aria dreptunghiului este {aria}')


# 8.
# Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# cititi de la tastatura un int x
# afiseaza stringul fara ultimele x caractere
# ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

# stringul_nostru = "Coral is either the stupidest animal or the smartest rock"
# print(int(len(stringul_nostru)))
#
# modificat = stringul_nostru[:50:]
#
# print(modificat)

# 9.
# acelasi string
# declara un string nou care sa fie format din primele 5 caractere + ultimele 5

# stringul_nostru = "Coral is either the stupidest animal or the smartest rock"
# primele = stringul_nostru[:5:]
# ultimele = stringul_nostru[52:58:]
# string = primele + ultimele
# print(string)

#
# 10.
# acelasi string
# afisati de cate ori apare cuvantul 'the'

# stringul_nostru = "Coral is either the stupidest animal or the smartest rock"
# numaratoare =stringul_nostru.count(" the ")
# print(numaratoare)


# 11.
# acelasi string
# inlocuieste the cu THE peste tot
# printeaza rezultatul
#
# stringul_nostru = "Coral is either the stupidest animal or the smartest rock"
# nou = stringul_nostru.split()
# print(type(nou))
#
# inlocuit = stringul_nostru.replace(" the ", " THE ")
# print(inlocuit)


# 12.
# acelasi string
# salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
# (hint: este o functie care te ajuta sa faci asta)
# folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
# output: 'Coral is either the stupidest animal or the smartest '

# stringul_nostru = "Coral is either the stupidest animal or the smartest rock"
# index = stringul_nostru.find("rock")
# print(index)
# afisare = stringul_nostru[0:53:1]
# print(afisare)


#
# 13.
# Folosind variabilele definite la exercitiul numarl 2 (cele 4 variabile declarate de tip str, int, float, bool), declarati
# o alta variabila de tip string in care sa le adaugati folosind tehnica de formatare a unui string.
# Printeaza rezultatul

# a = 1
# b = 1.1
# c = "mere"
# d = True
# e = f'{a} {b} {c} {d}'
# print(e)



#
# 14.
# avand stringul '0123456789'
# afisati doar numerele pare
# acum afisati doar numerele impare
# (hint: folositi slicing, controlati din pas)


# ex_14 = "0123456789"
# lista=ex_14.split()
# print(lista)
# pare = ex_14[0:10:2]
# print(pare)
# impare = ex_14[1:10:2]
# print(impare)



# 15.
# Aveti un dreptunghi, declarati 2 variabile pe nume “lungime” si “latime”, ele trebuie sa primeasca ca si input de la tastatura dimensiunile.
# Printati aria calculata a dreptunghilui
#
# lungime = int(input("Spune-mi lungimea dreptunghiului"))
# latime = int(input("Spune-mi latimea dreptunghiului"))
# arie = lungime*latime
# print(arie)



# c. Optionale (may need google)
# 16.
# citeste de la tastatura un string de dimensiune impara
# # afiseaza caracterul din mijloc
#
# test = "paste"
# nr_caractere = len(test)
# x = nr_caractere//2
# print(x)
# # print(nr_caractere)
# # mijloc = test[3::]
# # print(mijloc)
# print(test[x])

#
# 17.
# folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
# si salveaza fiecare cuvant intr-o variabila
# acum printeaza ambele variabile pentru verificare



# 18.
# citeste un string de la tastatura (eg: alabala portocala)
# salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)
# capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
# => alAbAlA portocAla
#
#
# 19.
# citeste un user de la tastatura
# citeste o parola
# afiseaza: 'Parola pt user x este *** si are x caractere'
# *** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
# eg: parola abc => *
# parola abcd => **


# Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
# Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if
# X poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte.
# X este un int
#
#
# 1.
# Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else
#
#
# 2.
# Verifica si afiseaza daca x este numar pozitiv sau nu
# x = -2
# if x>=0:
#     print("Nr pozitiv")
# else:
#     print("Nr negativ")

#
# 3.
# Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

# x = int(input("Spune numar"))
# if x>0:
#     print("Nr pozitiv")
# elif x<0:
#     print("Nr negativ")
# else:
#     print("Nr neutru")



#
# 4.
# Verifica si afiseaza daca x este intre -2 si 13

# lista = range(-2,14)
# x = int(input("Spune-mi un numar "))
# if x in lista:
#     print("Nr este in interval ")
# else:
#     print("Nr nu se afla in interval ")


# 5.
# Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5

# x = int(input("Spune-mi val lui X "))
# y = int(input("Spune-mi valoarea lui Y"))
# diferenta = x - y
# if diferenta <5:
#     print("Da")
# else:
#     print("Nu")



# 6.
# Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
#
# x = int(input("Spune-mi valoarea lui x"))
# lista = range(5,28)
# if x not in lista:
#     print("Nu se afla")
# else:
#     print("Se afla")

#
# 7.
# x si y (int)
# Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare

# x = int(input("Spune-mi valoarea lui x "))
# y = int(input("Spune-mi valoarea lui y "))
# if x == y:
#     print("Sunt egale")
# elif x>y:
#     print(x)
# else:
#     print(y)


#
# 8.
# X, y, z - laturile unui triunghi
# Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
#

#isoscel catete egale
#echilaterlale sunt toate egale
#oarecare toate diferite

#x,y catetele, z ipotenuza
#
# x = int(input("Spune-mi valoarea lui x "))
# y = int(input("Spune-mi valoarea lui y "))
# z = int(input("Spune-mi valoarea lui z "))
# if x==y and not x==z:
#     print("isoscel")
# elif x==y and y==z:
#     print("echilateral")
# else:
#     print("oarecare")
#
#


#
#
# 9.
# Citeste o litera de la tastatura
# Verifica si afiseaza daca este vocala sau nu
#
# vocale = ["a","e","i","o","u"]
# litera = input("Spune-mi litera")
# if litera in vocale:
#     print("Este vocala")
# else:
#     print("Este consoana")





# 10.
# Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

# nota_romaneasca = float(input("Spune-mi nota romaneasca "))
# while nota_romaneasca < 0:
#     print("Reintrodu nota")
#     print(nota_romaneasca)
#     break
# if nota_romaneasca>9:
#     print("A")
# elif nota_romaneasca>=8:
#     print("B")
# elif nota_romaneasca>=7:
#     print("C")
# elif nota_romaneasca>=6:
#     print("D")
# elif nota_romaneasca>=4:
#      print("E")
# else:
#      print("F")

#
# c. Optionale (may need google)
#
#
# 11.Verifica daca x are minim 4 cifre
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

# x = "789500"
# nr = len(x)
# print(nr)



# 12.Verifica daca x are exact 6 cifre
#
#
# 13.
# Verifica daca x este numar par sau impar

# a = 9
# if a%2==0:
#     print("par")
# else:
#     print("impar")
#
# #
# 14. x, y, z (int)
# Afiseaza care este cel mai mare dintre ele?
# x=4
# y=3
# z=9
# if x>y and x>z:
#     print("x cel mai mare")
# elif x>y and x<z:
#     print("z cel mai mare")
# else:
#     print("y cel mai mare")
#
# 15. X, y, z - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu
#
#
#
#
# 16. Pentru exercitiile cu biletele de avion incercati sa aplicati tehnicile de equivalence partitioning si boundary value analysis astfel incat sa eficientizati testarea.
#
#
# Sa tineti cont de urmatoarea chestie: tehnicile de testare vor fi aplicate nu pe faptul ca o persoana are pasaport sau nu ci pe varsta persoanei
#
#
# pasaport = input('Are pasaportul valid : DA/NU ')
# ambii_parinti = input('Are ambii parinti? DA/NU ')
# permisiune = input('Are permisiune? DA/NU/NA ' )
#
#
# if pasaport == 'DA' and (ambii_parinti == 'DA' or permisiune == 'DA') :
#     print('Permite calatoria')
# else :
#     print('Nu permite calatoria')
#
#
#
# Codul de mai sus va fi actualizat astfel incat sa țină cont și de varsta
#
#
#
#
# Age = input(introduceti varsta)
# pasaport = input('Are pasaportul valid : DA/NU ')
# ambii_parinti = input('Are ambii parinti? DA/NU ')
# permisiune = input('Are permisiune? DA/NU/NA ')
#
#
# If age >=18 and pasaport == “DA”:
#         print(permite calatoria)
# elif pasaport == 'DA' and (ambii părinți == 'DA' or permisiune == 'DA') :
#     print('Permite calatoria')
# else :
#     print('Nu permite calatoria')
#
#
#
#
# Tehnicile de testare discutate vor fi aplicate pe condiția age>=18 și vor consta în crearea unor clase de echivalență din care vom alege cate o singura valoare și respectiv valorile de graniță pentru a le folosi în testare
# def functie(a,b,c):
#     return a+b+c
# var1=1
# var2=2
# total = functie(var1, var2)
# print(total)
#
# def suma(a,b):
#     return a+b
#
#
# def diferenta(a,b):
#     return a-b
#
#
# def inmultire(a,b):
#     return a*b
#
#
# def impartire(a,b):
#     if b ==0:
#         while b == 0:
#             b = int(input("Nu se poate imparti la 0, realoca o valoare pt B "))
#     return a/b
#
#
# def operator():
#     op = input("Alege operatorul: ")
#     if op not in ["*", "/", "+", "-"]:
#         while op not in ["*", "/", "+", "-"]:
#             op = input("Alege operatorul")
#     return op
#
#
# def introducere():
#     nr1 = int(input("Spune-mi valoare pentru nr1"))
#     nr2 = int(input("Spune-mi valoare pentru nr2"))
#     return nr1, nr2
#

#
# lista_categorii = [item for item in input("Introduceți categoriile de taskuri: ").split()]
# print(f'Lista categoriilor este: {lista_categorii}')
#
# categorie_task = input("Spune-mi categoria din care face parte task-ul: ")
#
# while categorie_task not in lista_categorii:
#     reintroducere = input("Categoria introdusa nu face parte din lista de categorii. Doriti sa reintroduceti categoria? y/n")
#     if reintroducere == "y":
#         categorie_task = input("Spune-mi categoria din care face parte task-ul: ")
#     else:
#         break
#
#
# status = input("Spune-mi statusul task-ului: activ sau inactiv: ")
#
#
#
#
#
# lista = [1,2,3,[4,5,[6,7]]]
# print(lista[3][2][1])
#


# try:
#     nr = int(input("Spune-mi nr "))
#     print(f'Numarul este {nr}')
# except ValueError:
#     print("Nu este nr intreg ")
# else:
#     print("else")
# finally:
#     print("Ana are mere")
#

#vreau sa inlocuiesc are cu mananca
# text = "Ana are mere"
# lista=text.split()
# print(lista)
# lista[1]="mananca"
# print(lista)
# print(str(lista))
#
# def functie(a,*args):
#     diff = a
#     for item in args:
#         diff = item - diff
#     return diff
#
# print(functie(1,2,3,4))

# def functie(n):
#     return n+n
#
# lista = [1,2,3,4]
# # rezultat = map(functie,lista)
# # print(list(rezultat))
#
# rezultat = map(lambda n: 2*n,lista)
#
# print(list(rezultat))

# import csv
# lista = [
#     [1,2,3,4,5,6],
#     ["ana", "are", "mere"],
#     [1000,2000,3000]
#      ]
# with open("csv_test.csv", "a") as csv_incercare:
#     csv_unu = csv.writer(csv_incercare, delimiter = ",")
#     for item in lista:
#         csv_unu.writerow(item)
#
# import json
# # a = '{"name":"Ion", "prenume":"Cirstea" }'
# # b = json.loads(a)
# # print(b, type(b))
# # x = "Ana are mere"
# # y=json.dumps(x)
# # print(y)
#
# a = None
#
# print(json.dumps(a), type(a))


# num_calls = 0

# def exercitiu(x):
#     global num_calls
#     num_calls = 3
#     num_calls +=1
#     return x * x
#
# print(exercitiu(4))

# x = 1
# def f():
#     return x
#
# print(x)
# print(f())

# x = [1,2, "hellooooo", "world", ["another", "list"]]
# print(len(x))


# x = (1,2,3)
# x[1]=4

# a = [1, 2, 3]
# b = [4,5]
#
# print(a + (b*3))


# x = [1,2,3,4]
# print(x[-3:-1])

# x = [0, 1, [2]]
# x[2][0] = 3
# x[2].append(4)
# x[2] = 2
# print(x)
#
# def exercitiu(i):
#     for i in range(i):
#         return i
# x = exercitiu(3)
# print(x)



# a = range(10)
# y = [x*x for x in a if x%2 == 0]
# print(y)
# [0,2,4,6,8] -> [0,4,16, 36, 64]
#
# def make_account():
#     return {'balance': 0}
#
#
# def deposit(account, amount):
#     account ['balance'] += amount
#     return account['balance']


# a = make_account()
# print(deposit(a, 10))
#
# "foo" + 2
# try:
#     print("a")
# except:
#     print("b")
# else:
#     print("c")
# finally:
#     print("d")

#
# for k in {"x":1, "y":2}:
#     print(k)

# print(list("python"))

# def funct(*args):
#     return 3 + len(args)
#
# print(funct(4,4,4))

# count = (3,2,5,4,6,7)
# while len(count)<5:
#     count0 = count[0]+1
#     print(count0)
#     break


# def exercitiu(var):
#     for letter in 'geeksforgeeks':
#         if letter == 'e' or letter == 's':
#             continue
#         print('Current Letter: ', letter)
#         var = 10
#         return var
# print(exercitiu(20))
# # #
# def f(a,list=[]):
#     for i in range (a):
#         list.append(i*i)
#     print(list)
#
# f(3)
# f(2,[1,2,3])
# f(2)


# list = ['1','2','3','4','5']
# print(list[12:])


# Se da urmatoarea lista:
# lista_nume = [‘Maria’, ‘Irina’, ‘Claudiu’, ‘Ionut’, ‘Irina’, ‘Matei’, ‘Irina’, ‘Maria’,‘Claudiu’]
# Se cere:




# 1. Sortati lista dupa nume #done
# lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria','Claudiu']

# lista_sortata=sorted(lista_nume)
#
# print(lista_sortata)

# 2. Determinati numarul de aparitii al fiecarui nume #done
# dictionar = {}
# for i in lista_nume:
#     dictionar[i]= lista_nume.count(i)
# print(dictionar)

# 3. Listati numele care apare de cele mai multe ori in lista initiala.

# lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria','Claudiu']
# def max_aparitii(nums):
#     max_val = 0
#     result = nums[0]
#     for i in nums:
#         occ = nums.count(i)
#         if occ > max_val:
#             max_val = occ
#             result = i
#     return result
# print(max_aparitii(lista_nume))

# 4. Listati numele care apare de cele mai putine ori in lista initiala
# lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria','Claudiu']
# def minim_aparitii(nums):
#     minim_val = 0
#     result = nums[0]
#     for i in nums:
#         occ = nums.count(i)
#         if occ < minim_val:
#             minim_val = occ
#             result = i
#     return result
# print(minim_aparitii(lista_nume))

# 3. Sa se verifice daca doua stringuri sunt anagrame ##not done
# def functie():
#
#     a = input("Spune-mi primul string: ")
#     b = input("Spune-mi al doilea string: ")
#     while i in a and i in b:
#         print("Stringurile sunt anagrame")
#
# print(functie())
#


# # 4. Sa se elimine toate duplicatele dintr-o lista #done
# lista = ["ana","ana","maria"]
# lista_noua=set(lista)
# print(lista_noua)

# 5. Sa se verifice daca un string este palindrom #done

# def verificare():
#     a = str(input("Spune-mi ce cuvant verificam daca este palindrom: "))
#     b = a[::-1]
#     if a.lower() == b.lower():
#         print("Cuvantul este palindrom")
#     else:
#         print("Cuvantul nu este palindrom")
#     return a
# print(verificare())


# 6. Sa se verifice ce numere lipsesc dintr-un interval

# def functie():
#     inceput_interval = int(input("Spune-mi inceputul de interval: "))
#     final_interval = int(input("Spune-mi ultima cifra a intervalului +1: "))
#     interval = range(inceput_interval,final_interval)
#     print(interval)
#     x = int(input("Spune-mi ce cifra vrei sa verificam daca este in interval: "))
#     if x not in interval:
#         print("Cifra nu este in interval")
#     else:
#         print("Cifra este in interval")
#     return x
# print(functie())

# 7. Sa se afiseze inversul unul string

# a = "mere"
# reversat = a[::-1]
# print(a)
# print(reversat)

# 8. Sa se afiseze toate permutarile dintr-un string

# Se da urmatoarea lista:
# lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria','Claudiu']
# # Se cere:
# # 1. Sortati lista dupa nume
#
# lista_sortata = sorted(lista_nume)
# print(lista_sortata)

# 2. Determinati numarul de aparitii al fiecarui nume

# lista_nume_2 = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria','Claudiu']
# # dictionar_nume = {}
# # for i in lista_nume_2:
# #     dictionar_nume[i] = lista_nume_2.count(i)
# # print(dictionar_nume)
#
# c = collections.Counter(lista_nume_2)
# print(c)
# 3. Listati numele care apare de cele mai multe ori in lista initiala.
#
# lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria','Claudiu']
# def max_aparitii(nums):
#     max_val = 0
#     result = nums[0]
#     for i in nums:
#         occ = nums.count(i)
#         if occ > max_val:
#             max_val = occ
#             result = i
#     return result
# print(max_aparitii(lista_nume))


# 4. Listati numele care apare de cele mai putine ori in lista initiala.

# lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria','Claudiu']






# lista_nume_2 = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria','Claudiu']
# dict = {}
# for i in lista_nume_2:
#     dict[i] = lista_nume.count(i)
#
# print(dict)

# lista_numere = [1,2,3,4,5,5,5,6,6]
# dictionar = {}
# for i in lista_numere:
#     dictionar[i] = lista_numere.count(i)
# print(dictionar)



# 3. Sa se verifice daca doua stringuri sunt anagrame
# 4. Sa se elimine toate duplicatele dintr-o lista

# lista_duplicate = [1,1,2,3,4,4,4,5]
# lista_unice = set(lista_duplicate)
# print(lista_unice)

# 5. Sa se verifice daca un string este palindrom

# a = str(input("Spune-mi ce cuvant verificam: "))
# b = a[::-1]
# if a == b:
#     print("Cuvantul este palindrom")
# else:
#     print("Cuvantul NU este palindrom")

# 6. Sa se verifice ce numere lipsesc dintr-un interval

# a = int(input("Spune-mi inceptul intervalului:"))
# b = int(input("Spune-mi finalul intervalului:"))
# x = range(a,b)
# c = int(input("Spune-mi ce numar verificam: "))
# if c not in x:
#     print("Numarul nu este in interval")
# else:
#     print("Numarul este in interval")


# 7. Sa se afiseze inversul unul string
# def sir():
#     sir_introdus = input("Spune-mi cuvantul")
#     invers = sir_introdus[::-1]
#     return invers
# print(sir())

# 8. Sa se afiseze toate permutarile dintr-un string

#
# Realizati o functie care sa inlocuiasca textul din variabila string aflat
# intre valorile “start” si “end” cu textul din “text”.
# string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be
# introduced."
# # [start, end, text]
# patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]
# Textual rezultat este: The Conquistator must meet King on top of Palace
# battlements to be introduced.
# Numaratoarea de start si end incepe cu indexul 1. Se pot introduce de la
# tastatura alte valori pentru index si text, cat si un numar mai mare de liste.
# Optimizati codul.

# def x():
#     text = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
#     lista = text.split(" ")
#     lista[1] = "Conquistador"
#     lista[4] = "King"
#     lista[8] = "Place"
#     return " ".join(lista)
#
# print(x())

# def nameChanger(x, y, z):
#     string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
#     # 42 -> 49
#     # string = "The Inquisitor must meet Varric on top of Palace's battlements to be introduced."
#     # 25 -> 31
#     # string = "The Inquisitor must meet King on top of Palace's battlements to be introduced."
#
#     start = string[5:14]
#     end = string[26:31]
#     text = string[43:49]
#     string2 = string.replace(start, x)
#     string3 = string2.replace(end, y)
#     string4 = string3.replace(text, z)
#     #print(string4)
# string_value = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
# lista = [[5, 14, 'Conquistador'],[26,31,'King'],[43,49,'Palace']]
# for i in sorted(lista, reverse=True):
#     #print(i, string_value[i[0]-1:i[1]])
#     string_value = string_value.replace(string_value[i[0]-1:i[1]], i[2])
#     print(string_value, '>>>')
#
# nameChanger("Conquistador", "King", "Palace")



# TO DO LIST INITAL

import pandas as pd
import csv
import datetime
actiune = ""
id = 0

# În prima faza se adaugă categoriile dorite de la tastatură:

lista_categorii = [item for item in input("Introduceți categoriile de taskuri: ").split()]
print(f'Lista categoriilor este: {lista_categorii}')


# Cerinte initiale: introducere de la tastatura

task = input("Spune-mi task-ul: ")

data_limita = input("Spune-mi data limita: ")

# if datetime.datetime.strptime(data_limita, "%d.%m.%Y %H:%M"):
#     pass
# else:
#     print("Data introdusa nu este corecta sau nu este introdusa corect, reincearca", data_limita)


data_verificata = data_limita

# while datetime.datetime.strptime(data_verificata, "%d.%m.%Y %H:%M"):
#     break
# else:
#     print("Data introdusa nu este corecta sau nu este introdusa corect.  ")
#     raspuns1 = input("Doriti sa reintroduceti data? y/n")
#     if raspuns1 == 'y':
#         data_limita = input("Spune-mi data limita: ")
#         print(data_limita)
#     else:  ###de pus aici ce sa returneaze
#         print("Nu se mai continua")


responsabilul = input("Spune-mi persoana responsabila de task: ")

categorie_task = input("Spune-mi categoria din care face parte task-ul: ")

while categorie_task not in lista_categorii: # functioneaza partial, de facut in asa fel incat sa nu mai treaca la introducerea statusul daca categoria nu este valida si nu vrea sa reintroduca task-ul
    reintroducere = input("Categoria introdusa nu face parte din lista de categorii. Doriti sa reintroduceti categoria? y/n")
    if reintroducere == "y":
        categorie_task = input("Spune-mi categoria din care face parte task-ul: ")
    else:
        break


status = input("Spune-mi statusul task-ului: activ sau inactiv: ")

linie_task = {
    "id": id+1,
    "task": task,
    "deadline": data_limita,
    "persoana_responsabila": responsabilul,
    "categoria_task": categorie_task,
    "status": status

}

coloane_tabel = [task, data_limita, responsabilul, categorie_task, status]
tabel_tasks = pd.DataFrame(coloane_tabel) #de scris in csv
print(tabel_tasks)

def meniu():

    actiune = int(input("Alege actiunea ce urmeaza sa fie executata asupra datelor : "
                        "\n1 Listare date: în afișarea inițială a datelor se realizează o sortare în "
                        "funcție de categorie"
                        "\n2 Sortare date \n3 Filtrare date \n4 Adăugarea unui nou task "
                        "\n5 Editarea detaliilor referitoare la task \n6 Ștergerea unui task "
                        "\n7 Nicio actiune "))
    return actiune


if meniu() == 1:

    while actiune != 'i': #daca nu merge pune o alta modalitate de iesire in loc de i
        actiune = str(input("Actiuni asupra datelor din tabel : \n'l' inseamna listare date (afisare date),"
                        "\n's' inseamna sortare date, \n'f' inseamna filtrare date, \n'ad' inseamna adaugare task-uri, "
                        "\n'e' inseamna editare date,\n'd' inseamna stergere date, "
                        "\n'i' inseamna ca nu mai facem nicio actiune"))
        if actiune == 'l':
            tabel_tasks.sort_values(categorie_task)
            print(tabel_tasks)

        elif actiune == 'ad':
            tabel_tasks_adaugat = tabel_tasks
            task = input("Spune-mi task-ul: ")
            data_limita = input("Spune-mi data limita: ")
            responsabilul = input("Spune-mi persoana responsabila de task: ")
            categorie_task = input("Spune-mi categoria din care face parte task-ul: ")
            status = input("Spune-mi statusul task-ului: activ sau inactiv: ")
            tabel_tasks_adaugat = tabel_tasks_adaugat.append({
                "id": 1,
                "task": task,
                "deadline": data_limita,
                "persoana_responsabila": responsabilul,
                "categoria_task": categorie_task,
                "status": status
            }, ignore_index=True)
            print(tabel_tasks)

        elif actiune == "d":
            task_de_sters = int(input("Alege id-ul de la task-ul ce vrei sa fie sters"))
            tabel_tasks_actualizat = tabel_tasks
            tabel_tasks_actualizat.drop([task_de_sters], inplace=True)
            print(tabel_tasks_actualizat)

        elif actiune == "s":
            sortare_date = int(input("Scrie doar cifra aferenta sortarii fiecarei optiuni de mai jos:"
                                     " \n'1' pentru sortare ascendentă task,"
                                     " \n'2' pentru sortare descendentă task,"
                                     " \n'3' pentru sortare ascendentă data,"
                                     " \n'4' pentru sortare descendentă data, "
                                     " \n'5' pentru sortare ascendentă persoana responsabilă"
                                     " \n'6' pentru sortare descendentă persoană responsabilă,"
                                     " \n'7' pentru sortare ascendentă categorie,"
                                     " \n'8' pentru sortare descendentă categorie "))
            tabel_tasks_sortat = tabel_tasks
            if sortare_date == 1:
                tabel_tasks_sortat.sort_values(categorie_task)
                print(tabel_tasks_sortat)
            elif sortare_date == 2:
                tabel_tasks_sortat.sort_values(categorie_task, ascending=False)
                print(tabel_tasks_sortat)
            elif sortare_date == 3:
                tabel_tasks_sortat.sort_values(data_limita)
                print(tabel_tasks_sortat)
            elif sortare_date == 4:
                tabel_tasks_sortat.sort_values(data_limita, ascending=False)
                print(tabel_tasks_sortat)
            elif sortare_date == 5:
                tabel_tasks_sortat.sort_values(responsabilul)
                print(tabel_tasks_sortat)
            elif sortare_date == 6:
                tabel_tasks_sortat.sort_values(responsabilul, ascending=False)
                print(tabel_tasks_sortat)
            elif sortare_date == 7:
                tabel_tasks_sortat.sort_values(categorie_task)
                print(tabel_tasks_sortat)
            elif sortare_date == 8:
                tabel_tasks_sortat.sort_values(categorie_task, ascending=False)
                print(tabel_tasks_sortat)
            else:
                pass

        elif actiune == "f":
            tabel_tasks_filtrat = tabel_tasks
            filtrare_date = int(input("Scrie cifra câmpulului după care se realizeaza filtrarea: \n'1' filtrare dupa task,"
                                      "\n'2' filtrare dupa data, \n'3' filtrare dupa responsabil,\n'4' filtrare dupa categorie"))
            if filtrare_date == 1:
                tabel_tasks_filtrat.query(categorie_task, inplace=True)
                print(tabel_tasks_filtrat)
            elif filtrare_date == 2:
                tabel_tasks_filtrat.query(data_limita, inplace=True)
                print(tabel_tasks_filtrat)
            elif filtrare_date == 3:
                tabel_tasks_filtrat.query(responsabilul, inplace=True)
                print(tabel_tasks_filtrat)
            elif filtrare_date == 4:
                tabel_tasks_filtrat.query(categorie_task, inplace=True)
                print(tabel_tasks_filtrat)
            else:
                pass


#  Editarea detaliilor referitoare la task dată, persoană sau categorie dintr-un anumit task ales de utilizator de la
#  tastatură (când se cere această opțiune, se va lista lista de taskuri cu un identificator unic pe rand, astfel încât
#  să se știe ce informație urmează să editeze utilizatorul)






























