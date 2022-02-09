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

def functie():
    nr_introdus=input("Spune-mi o valoare: ")
    value=nr_introdus
    if value.isnumeric():
        print(value)
    else:
        print("0")
print(functie())

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