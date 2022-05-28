# print("Hello world")
# a = 1
# b = 1.5
# c = "Diana"
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# a = float(a)
# # b = int(b)
# # print(a,b)
# #  # + adunar, - scadere, * inmultire, ** ridicare la putere, / impartire, // impartire exacta, % modulo returneaza restul
# #  == egalitate != inegalitate, is, is not, in, not in , >=, <=< >, <
# a=5
# b=6
# print(7 is not 6)

# print('Dumnezeu a zis: "Sa se faca lumina"')

# print("Diana \nGeorge")

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista.append(10000)
# print(lista)
# lista.insert(0,999)
# print(lista)
# lista[0]=888888888
# print(lista)
# print(lista.index(0))

# tuplu = (1,2,3)
# print(tuplu, type(tuplu))
# set_1={1,1,1,2}
# print(set_1)
# lista=[1,1,2,3,4,4]
# print(set(lista))
# print(tuplu[0])
# dictionar= {"a":1, "b":2}
# print(dictionar, type(dictionar))
# print(dictionar.keys())
# print(dictionar.values())
# print(dictionar.items())
# adaugare = {"c":3}
# dictionar.update(adaugare)
# print(dictionar)
# print(dictionar.get('a'))
# # print(dictionar.popitem())
# lista = [1,2,3,4]
# lista.insert(1000,5)
# print(lista)

# a = 'ana are mere'
# b = a.split( )
# print(b)
#
# for i,j in enumerate(b):
#     print(i,j)

# a = 1
# for i in range (1,10):
#     a = a+1
# print(a)
# while a<10:
#     a = a+1
# print(a)
#

# dictionar = {'a':1, "b": 2}
# for item in dictionar:
# print(dictionar.keys())

# a = int(input("Sune-mi valoarea lui a "))
# b = int(input("Sune-mi valoarea lui b "))

# def suma():
#     a = int(input("Sune-mi valoarea lui a "))
#     b = int(input("Sune-mi valoarea lui b "))
#     return a +b
#
# print(suma())
# def suma(a,b):
#     return a +b
#
# var1=1
# var2=2
# print(suma(var1,var2))

# a = "aa"
# if a.isdigit() is True:
#     print(a)
# else:
#     print("no")
# msg=" "
# def verificare():
#     a = input("Spune-mi valoarea lui a ")
#     if a.isdigit() is True:
#         msg = a
#     else:
#         msg = "No"
#     return msg
#
# print(verificare())

# a = [1,2, 3, [4, 5, [6,7]]]
# #vreau sa il scot pe 6
# print(a[3][2][0])

# def a(*args, **kwargs):
#     return args, kwargs
# print(a(1,2,3, nume= "Diana", prenume = "Manta"))
# print("Diana Ionela Manta")

# def incercare():
#     lista = [1,2,3,4,5]
#     # lista.append(4)
#     # lista[1:100:1]
#     return lista[1:100:1]
# print(incercare())

# def functie(param1, param2, *args, **kwargs):
#     print(param1)
#     print(param2)
#     print(args)
#     print(kwargs)
#
# functie(1, 2, 3, 4, 5,"abc", nume="Manta", prenume = "Diana")

# try:
#     a = int(input("Spune-mi valoarea lui a "))
#     # print(a)
# except ValueError:
#     print("Nu este nr intreg")
#
# else:
#     print(f'Nu avem erori, valoarea lui a este {a}')
# finally:
#     print("Returneaza oricum")

# def functie(a,b,c=0):
#     print(a,b,c)
#
# functie(1,2, c=3)
# print(functie)


# def functie(a=1,b=2,c=4):
#     return a, b, c
#
# print(functie(4,5,6))
#
# def functie():
#     initial = 0
#     nr_introdus = int(input("Spune-mi un nr "))
#     for item in range(nr_introdus+1):
#         initial = initial + item
#
#
#     initial_2 = 0
#     for item in range(0, nr_introdus+1):
#         if item % 2 == 0:
#             initial_2 = initial_2 + item
#
#
#     initial_3 = 0
#     for item in range(0, nr_introdus+1):
#         if item % 2 != 0:
#             initial_3 = initial_3 + item
#     return initial, initial_2, initial_3
#
# print(functie())

# def functie():
#     msg = " "
#     a = input("Spune-mi un numar: ")
#     nr_introdus = a
#     if nr_introdus.isdigit() is True:
#         msg = nr_introdus
#     else:
#         msg = "0"
#     return msg
# msg=functie()
# print(msg)
#
# lista = [{"nume": "Manta", "prenume": "George"},
#          {"nume": "Cirstea", "prenume": "Diana"},
#          {"nume": "Cretu", "prenume": "Teodora"}]
#
# nume_sortat = sorted(lista, key = lambda name: name["nume"])
# print(nume_sortat)

# def adunare(n):
#     return n+n
#
# lista = [1,2,3]
# lista_noua = map(adunare, lista)
# print(list(lista_noua))

# lista1 = [1,2,3]
# lista2 = [4,5,6]
# adunare = map(lambda x,y:x-y, lista1,lista2)
# print(list(adunare))

# lista1 = [5,6,7]
# lista2 = [10,11,12]
# adunare = zip(lista1,lista2)
# print(list(adunare))


# lista = [1,2,3,4]
# lista_noua = [item*2 for item in lista if item % 2 == 0]
# print(lista_noua)

# lista = ["ciocolata", "mere", "suc"]
# #vreau sa returnez cuvintele care contin litera c
# lista_noua = [item for item in lista if "c" in item]
# print(lista_noua)
#

# class Caine: #creez clasa
#     picioare = 4 #atribut de clasa, este general pentru toate obiectele ce vor fi create
#
#     def __init__(self, name, vaccin): #constructorul, atributele clasei/obiectelor
#         self.nume = name
#         self.v = vaccin
#         Caine.picioare = 6
#
#     def schimbare(self, name):
#         self.nume = name
#         return self.nume
#
#     def __str__(self): #folosim pentru a afisa
#         return f'Informatiile despre caine sunt: nume {self.nume}, numar vaccinuri {self.v}, picioare {self.picioare}'
#
# caine1 = Caine("Rex", "2") #instantierea clasei
# print(caine1)
# print(caine1.picioare) #accesare atribut de clasa
# print(caine1.nume) #accesare atribut
# print(caine1.v) #accesare atribut
# print(caine1.schimbare("Ben"))
# print(caine1)
# # Caine.picioare = 6
# print(Caine.picioare)


# class Persoana:
#     def __init__(self, first, second):
#         self.__nume = first
#         self.__prenume = second
#
#
#     def __str__(self):
#         return f"Nume: {self.__nume}, prenume: {self.__prenume}"
#
#
#     def change(self, first, second):
#         self.__nume = first
#         self.__prenume = second
#         return self.__nume, self.__prenume
#
#
# om1 = Persoana("Diana", "Cirstea")
# print(om1)
# print(om1.change('Diana', 'Manta'))
#
# print(om1._Persoana__nume)
# print(om1._Persoana__prenume)


# class Persoana:
#     maini = 2
#
#     def __init__(self, first, second):
#         self.__nume = first
#         self.prenume = second
#
#     def schimbare(self,first):
#         self.nume = first
#         return self.nume
#
#     def __str__(self):
#         return f'Numele este: {self.__nume} si prenumele este: {self.prenume}'
#
# om1 = Persoana("George", "Manta")
# om2 = Persoana("Diana", "Cirstea")
# print(om1)
# # print(om2)
# # print(om1.nume) #accesare de atribut de instanta
# # print(om1.maini) #accesare atribut de clasa
# # print(om1.schimbare("Daniel")) #metoda
# # print(om1) #s-a modificat obiectul dupa aplicarea metodei
# print(om1._Persoana__nume)

# class Animal:
#     def __init__(self, name):
#         self.nume = name
#
#
# class Caine(Animal):
#     def __init__(self, name, picioare):
#         super().__init__(name)
#         self.__picioare = picioare
#
#
#     def __str__(self):
#         return f"Numele este: {self.nume}, iar nr picioare este {self.picioare}"
#
# caine1 = Caine("Rezx", "2")
# print(caine1)
# print(hasattr(caine1,'nume'))
# print(caine1.__dict__)

# class Persoana:
#     def __init__(self, name):
#         self.nume = name

#     @property
#     def name(self):
#         return self.nume
#
#     @name.setter
#     def name(self, name):
#         self.nume = name
#
#     @name.deleter
#     def name(self):
#         del self.nume
#
# om1 = Persoana("Diana")
# print(om1.name)
# om1.name = "Ionela"
# print(om1.name)


#
# class Persoana:
#     def __init__(self, name):
#         self.nume = name
#
#     def __str__(self):
#         return self.nume
#
# om1 = Persoana("Diana")
# print(om1)
# print(hasattr(om1, "nume"))
# print(getattr(om1, "nume"))
# setattr(om1, "nume","Ionela")
# print(om1.nume)
# delattr(om1, "nume")
# print(om1.nume)

# class Catalog:
#     def __init__(self, nume, prenume):
#         self.nume = nume
#         self.prenume = prenume
#         self.absente = 0
#         self.materii = {}
#
#     def __str__(self):
#         return f"{self.nume}, {self.prenume}, {self.absente}, {self.materii}"
#
#     def adaugare(self):
#         self.absente += 1
#
#     def stergere(self, abs_motivate):
#         if self.absente > abs_motivate:
#             self.absente -= abs_motivate
#
# class Extensie1(Catalog):
#     def __init__(self, nume, prenume):
#         super().__init__(nume, prenume)
#
#     def dictionar(self, materia, note):
#         self.materia = self.materii.update({materia: note})
#
#     def medie(self):
#         note_finale = {}
#         for i,j in self.materii.items():
#             medie = sum(j)/len(j)
#             note_finale.update({i: medie})
#         return note_finale
#
#     def __str__(self):
#         return f"Materiile sunt{self.materii}"
#
# elev1 = Catalog("Ion", "Roata")
# print(elev1)
# elev1.adaugare()
# elev1.adaugare()
# elev1.adaugare()
# print(elev1)
# elev1.stergere(2)
# print(elev1)
# elev2 = Catalog("George", "Cerc")
# print(elev2)
# elev2.adaugare()
# elev2.adaugare()
# elev2.adaugare()
# elev2.adaugare()
# print(elev2)
# elev2.stergere(2)
# print(elev2)
# print(elev1.absente)
# print(elev2.absente)
#
# elev3 = Extensie1("Ana", "Maria")
# print(elev3)
# elev3.dictionar("Python", [5,6,7])
# print(elev3)
# print(elev3.medie())

#
# class Clasa1:
#     def __init__(self, marca, tip):
#         self.marca = marca
#         self.tip = tip
#
#     def schimbare(self, culoare):
#         self.culoare = culoare
#
#
#     def __str__(self):
#         return f"Culoarea este {self.culoare}"
#
#
# class Clasa2(Clasa1):
#     def __init__(self,marca, tip, scaune_incalzite):
#         super().__init__(marca, tip)
#         self.scaune_incalzite = scaune_incalzite
#
#     def __str__(self):
#         return f"Marca este: {self.marca}, tipul este {self.tip}, {self.scaune_incalzite} are scaune incalzite"
#
#
# class Clasa3(Clasa1):
#     def __init__(self, marca, tip, led):
#         super().__init__(marca, tip)
#         self.led = led
#
#     def __str__(self):
#         return f"Marca este: {self.marca}, tipul este {self.tip}, {self.led} are led"
#
#
# cls2 = Clasa2("aro", "m461", "Nu")
# print(cls2)
# cls2.schimbare("rosu")
# print(cls2.culoare)
#
# cls3 = Clasa3("Dacia", "1310", "Nu")
# print(cls3)
# cls3.schimbare("negru")
# print(cls3.culoare, cls3.marca, cls3.tip, cls3.led)
# print(cls2.culoare, cls2.marca, cls2.tip, cls2.scaune_incalzite)



# class Calculator:
#     def __init__(self,a=1,b=2,c=3,d=4):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#
#     def calcul(self):
#         self.rezultat = "<>"
#         if str(self.a).isnumeric() and str(self.b).isnumeric() and str(self.c).isnumeric() and str(self.d).isnumeric():
#             self.rezultat = (self.a * (self.b + 3) / self.c) * self.d
#         return self.rezultat
#
#     def __str__(self):
#         return f'Rezultatul este: {self.calcul()}'
#
# calcul1 = Calculator()
# print(calcul1)

# class A():
#     def __init__(self,x):
#         self.x=x
#
# ob = A()
a = 5
print(a)



























































































