# decoratorii sunt o functie

# Ex 1:
# def decorator_simplu(parametru):
#     print(f"Apelam functia {parametru.__name__}")
#     return parametru
#
# @decorator_simplu
# def fuctie_simpla():
#     return "Buna seara"
#
# print(fuctie_simpla())

# scrii un decaorator si il aplici pe mai multe functii -> rolul decoratorului


# Ex 2
#definire decorator care are mai multe roluri:

# def decorator_depozit(material):
#     def ambalaj(fuctia_noastra):
#         def ambalaj_intern(*args):
#             print(f"Ambalam produse din {fuctia_noastra.__name__} cu {material}")
#             fuctia_noastra(*args)
#             return args
#         return ambalaj_intern
#     return ambalaj
#
#
# @decorator_depozit("hartie")
# def impachetare_carti(*args):
#     return f"Impachetam carti: {args}"
#
# # print(impachetare_carti("Amintiri din copilarie", "Baltagul"))
#
# @decorator_depozit("folie alimentara")
# def impachetare_fructe(*args):
#     return args
# print(impachetare_fructe("mere", "pere"))


# Exercitiu:

# def decorator(functie):
#     def decoreaza (var):
#         return functie(var)
#     return decoreaza
#
# def p(functie):
#     def decoreaza(var):
#         return f'<p>{functie(var)}</p'
#     return decoreaza
#
# def strong(functie):
#     def decoreaza(var):
#         return f'<p>{functie(var)}</p'
#     return decoreaza
#
# @strong
#
# def text(sir):    #text egal functie, parametru sir = parmametru var
#     return sir.upper()
#
# text_p = decorator(text)
# print(text("Salut")) #am apelat decorator cu functia parametru



# EXEMPLU:
#
# class Dog:
#     def __init__(self, nume):
#         self.__nume = nume     #name = atribut
#
#     @property  #citesti proprietatea, valoarea din atribut - ajuta la nivel de obiect sa putem sa accesam/definim/modifcam proprietati exsitente, trasnfomam metotda in atribut
#
#
#     def name(self):  #metoda
#         return self.__nume
#
#     @name.setter #schimb proprietatea din Rex in Ben -  sa am drepturi de setare, petnru o reatribuire setare
#     def name(self, nume):  #metoda prin care setez o alta valoare
#         self.__nume = nume
#
#     @name.deleter #sterge
#     def name(self):
#         del self.__nume
#
# my_dog = Dog(nume="Rex")    #obiectul
# print(my_dog.name) #pt ca am scris property nu mai pun aici dupa name doua paranteze()
#
# my_dog.name = "Ben"
# print(my_dog.name)
#
# del my_dog.name
# print(my_dog.name) #da erorare pentru ca l-am sters mai sus

# class Cat:
#     legs_no = 4
#
#     def __init__(self, nume):
#         self.__nume = nume
#
#     @property
#     def name (self):
#         return self.__nume
#     @name.setter
#     def name (self, nume):
#         self.__nume = nume
#
#     @name.deleter
#     def name(self):
#         del self.__nume
#
#     def change_name(self, nume):
#         self.__nume = nume
#
#     def __str__(self):
#         return f'{self.__nume}'
#
# cat_object = Cat("Fluffy")
# cat_object.change_name("Milly")
# print(cat_object)
# print(cat_object.legs_no)
#


# STATIC METOD

# from datetime import date
# class Persoana:
#
#     def __init__(self, nume, varsta):
#         self.nume = nume
#         self.varsta = varsta
#
#     @classmethod #transfera in metoda de clasa, dependent de constructor
#     def varsta_ani(cls, nume, varsta):
#         return cls (nume, date.today().year - varsta)
#
#     @staticmethod #independent de constructor
#     def stare(ani):  #ajuta sa apelam o metoda fara sa folosim self, nu tine cont de nume si varsta
#         return ani > 18
#
# persoana_1 = Persoana("Ion", 21)
# # print(persoana_1.varsta)
# persoana_2 = Persoana.varsta_ani("Maria",20)
# print(persoana_2.varsta)
# print(Persoana.stare(25))

