# lista= []
# # for item in "Ana are mere":
# #     lista.append(item)
# #
# # rezultatul este o lista
# #
# # sau mai putem face
#
# lista = [item for item in "Ana are mere" ] #primul item zice ca adauga, executa for-ul
# print (lista)

#
# my_numbers=[1,2,3,4,5]
# lista_numere = [item **2 for item in my_numbers if item % 2 == 0] #item e valoare
# print(lista_numere) #verifica in lista care numere se impart fix la 2 si cele care se impart le ridica la putere si le printeaza


# lista_produse= [ "ciocolata", "suc", "mere", "miere", "apa"]
# lista_noua = [x for x in lista_produse if "a" in x] #primul x inseamna ca o sa adauge, for x in lista inseamna ca verifica fiecare element din lista daca are in componenta litera a si daca are returneaza in lista
# print(lista_noua)



# lista = [x for x in range(10) if x< 5]
# print (lista) #returneaza de la 0 la 4 inclusiv


#
# a,b = 10, 20
# min = a if a<b else b #daca a e mai mic ca b, min =a altfel min = b, ce e in stanga if-ului se executa daca e adevarat, altfel se returneaza ce e in dreapta
# print(min) #operator ternar


# lista_produse= [ "ciocolata", "suc", "mere", "miere", "apa"]
# lista_noua=[x if x!="suc" else "apa minearala" for x in lista_produse] #for-ul se executa prima data!!!
# print(lista_noua)
#for x in lista produse inseamna ca parcurge lista
#primul x inseamna ca va adauga elementul din lista in cazul in care conditia este indeplinita


#functia filter
# lista_numere = [1,2,3,4,5,6,7,8,9,10] #vrem sa extragem elementele care se impart la 2
# def functie_nr_pare(number):
#     if number %2 ==0:
#         return True
#     return False
#
# iterator_numere_pare = filter(functie_nr_pare, lista_numere)
# print(list(iterator_numere_pare))



litere = ["a","b","c","d","e","i","j"]
def filter_vocale(letter):
    vocale = ["a","e","i","o","u"]
    return True if letter in vocale else False

filtrare_vocale = filter(filter_vocale,litere)
print(list(filtrare_vocale))


