# class A:
#     counter = 0
#     zi_nastere = 12
#     def __init__(self, nume):
#         self.name = nume
#         A.counter +=1
#
#     def __str__(self):
#         return f"Numele este {self.name}"
#
#
# class B(A):
#     def __init__(self, nume,adresa):
#         super().__init__(nume)
#         self.__adress = adresa
#
#     def schimbare_nume(self, nume):
#         self.name = nume
#         return nume
#
#     def __str__(self):
#         return f"Numele este {self.name} si adresa este {self.__adress}"
#
# class C(B)
#     pass


# om1 = B("Diana","Zori de zi")
# print(om1)
# om1.schimbare_nume("Anca") #accesare metoda
# print(om1)
# print(A.zi_nastere) #accesare atribut de clasa
# om2 = A("George")
# print(om2)
# om3 = B("Cosmin", "Ciprian Porumbescu")
# print(om3)
# print(A.counter)
# print(om1.adress)
# print(om1.__dict__)
# print(om1._B__adress) #accesare atribut privat
# print(hasattr(om1, 'name'))
# print(hasattr(om1, 'nr_ochi'))
# print(hasattr(om1, 'adress'))
# om4 = A("Ionela")
# om4.varsta = 27
# print(om4.__dict__)


# # ex1
# # Creati o clasa ce va reprezenta un catalog:
# # • La initializare trebuie sa oferim doi parametrii de intrare nume si prenume
# #  Metoda de initializare creaza un atribut numit materii de tip dictionar nepopulat, dar si un atribut numit absente initializat la 0.
# # • Avem o metoda care afiseaza absente implementat cu __str__
# # • Avem o metoda care incrementeaza cu 1 nr. de absente
# # • Avem o metoda care sterge un nr. (exclusiv un numar - verifica) de absente dat (pentru
# # cazurile in care avem o scutire medical) fara a deveni negativ
#
# class Catalog:  #creez clasa
#
#     def __init__(self, nume, prenume):
#         self.nume = nume
#         self.prenume = prenume
#         self.absente = 0
#         self.materii = {}
#
#     def __str__(self):
#         return f'{self.nume}, {self.prenume}, {self.absente}, {self.materii}'
#
#     def incrementare(self):
#         self.absente += 1
#
#     def stergere(self, numar_absente):
#         if self.absente > numar_absente:
#             self.absente -= numar_absente
#
# # Creati a doua clasa numita Extensie1 care sa mosteneasca prima clasa. Clasa materii sa aiba 3 metode:
# # - Prima metoda permite adaugarea prin doi parametrii de intrare a unui sir de
# # caractere reprezentand materia si o lista reprezentand notele. Acesti parametrii de
# # intrare sunt utilizati pentru a adauga o intrare in dictionarul atribut materii al obiectului
# # current. Cheia este materia (sirul de caractere) si lista reprezinta value.
# # - A doua metoda permite afisarea tuturor materilor unui student.
# # - A treia metoda permite afisarea materiilor si media aritmetica a fiecarei liste asociate
# # pentru fiecare materie in parte. Verificati daca in lista sunt elemente de tip numar si
# # ignorati alte valori.
#
#
# class Extensie(Catalog):
#     def __init__(self, nume, prenume):
#         super().__init__(nume, prenume)
#         # print(self.materii)
#
#     def adaugare(self, materie, nota):
#         self.materie = self.materii.update({materie: nota})
#
#     def afisare(self):
#         return f"{self.materii}"
#
#     def final_grade(self):
#         note_finale = {} #defineste un disctionar gol
#         for i,j in self.materii.items():
#             if all(isinstance(x, int) for x in j): #verifica daca toate valorile dictionarului sunt int-uri in acest dictionar
#                 medie = sum(j) / len(j) #daca este indeplinita conditia de mai sus, calculeaza media aritmetica a valorilor
#                 note_finale.update({i: medie}) #returneaza i care este cheia adica materia si media calculata mai sus
#             return note_finale
#
# # • Creati 1 student numit Ion Roata
#
# obiect1 = Catalog("Roata","Ion")
# print(obiect1)
# # • Modificati argumentul absente sa fie incrementat de 3 ori prin metoda creata
# obiect1.incrementare()
# obiect1.incrementare()
# obiect1.incrementare()
# print(obiect1)
#
# # • Stergeti doua absente prin metoda specificata
# obiect1.stergere(2)
# print(obiect1)
#
# # • Creati al doilea student numit George Cerc
# obiect2 = Catalog("Cerc", "George")
# print(obiect2)
# # • Modificati argumentul absente sa fie incrementat de 4 ori prin metoda creata
# obiect2.incrementare()
# obiect2.incrementare()
# obiect2.incrementare()
# obiect2.incrementare()
# print(obiect2)
# # • Stergeti doua absente prin metoda specificata
# obiect2.stergere(2)
# print(obiect2)
# # • Afisati absentele fiecarui student
# print(obiect1.absente)
# print(obiect2.absente)
# # • Adaugati materia ”Python” impreuna cu o lista formata din 3 numere intre 1-10 pentru
# # fiecare student
# obiect1 = Extensie("Roata", "Ion")
# obiect1.adaugare("Python", [5,5,5])
# print(obiect1)
# obiect2 = Extensie("Cerc", "George")
# obiect2.adaugare("Python", [7,7,7])
# print(obiect2)
# # • Adaugati materia ”Matematica” la al doilea student numit George Cerc si “Romana” pentru
# # studentul numit Ion Roata impreuna cu o lista formata din 3 numere intre 1-10 pentru fiecare
# # student
# obiect1.adaugare("Matematica",[5,6,7])
# print(obiect1)
# obiect2.adaugare("Romana", [5,6,7])
# print(obiect2)
#
#
# # • Verificati ce materii are fiecare student prin metoda ce permite afisarea tuturor materilor
# # unui student.
# print(obiect1.afisare())
# print(obiect2.afisare())
# # • Verificati ce materii si ce note mediate au studentii.
# print(obiect1.final_grade())
# print(obiect2.final_grade())

# ex1
# Creati o clasa ce va reprezenta un catalog:
# • La initializare trebuie sa oferim doi parametrii de intrare nume si prenume
#  Metoda de initializare creaza un atribut numit materii de tip dictionar nepopulat, dar si un atribut numit absente initializat la 0.
# • Avem o metoda care afiseaza absente implementat cu __str__
# • Avem o metoda care incrementeaza cu 1 nr. de absente
# • Avem o metoda care sterge un nr. (exclusiv un numar - verifica) de absente dat (pentru
# cazurile in care avem o scutire medical) fara a deveni negativ


class Catalog:
    def __init__(self, nume, prenume):
        self.first = nume
        self.second = prenume
        self.materii = {}
        self.absente = 0

    def __str__(self):
        return f"{self.first, self.second, self.materii, self.absente}"

    def incrementare(self):
        self.absente += 1

    def stergere(self, numar_absente):
        if self.absente > numar_absente:
            self.absente -= numar_absente

# Creati a doua clasa numita Extensie1 care sa mosteneasca prima clasa. Clasa materii sa aiba 3 metode:
# - Prima metoda permite adaugarea prin doi parametrii de intrare a unui sir de
# caractere reprezentand materia si o lista reprezentand notele. Acesti parametrii de
# intrare sunt utilizati pentru a adauga o intrare in dictionarul atribut materii al obiectului
# current. Cheia este materia (sirul de caractere) si lista reprezinta value.
# - A doua metoda permite afisarea tuturor materilor unui student.
# - A treia metoda permite afisarea materiilor si media aritmetica a fiecarei liste asociate
# pentru fiecare materie in parte. Verificati daca in lista sunt elemente de tip numar si
# ignorati alte valori.


# class Extensie1(Catalog):
#     def __init__(self, nume, prenume):
#         super().__init__(nume, prenume)
#
#     def adaugare(self, materia, nota):
#         self.materia = materia
#         self.nota = []
#         self.materia = self.materii.update({materia:nota})
#
#     def afisare(self):
#         return f"{self.materii}"
#
#     def final_grade(self):
#         note_finale = {}
#         for i,j in self.materii.items():
#             if all(isinstance(x, int) for x in j):
#                 medie = sum(j)/len(j)
#                 note_finale.update({i: medie})
#         return note_finale
#
#
# # • Creati 1 student numit Ion Roata
#
# s1 = Catalog("Roata", "Ion")
# print(s1)
# # • Modificati argumentul absente sa fie incrementat de 3 ori prin metoda creata
# s1.incrementare()
# s1.incrementare()
# s1.incrementare()
# print(s1)
# # • Stergeti doua absente prin metoda specificata
# s1.stergere(2)
# print(s1)
# # • Creati al doilea student numit George Cerc
# s2 = Catalog("cerc", "george")
# # • Modificati argumentul absente sa fie incrementat de 4 ori prin metoda creata
# s2.incrementare()
# s2.incrementare()
# s2.incrementare()
# s2.incrementare()
# print(s2)
# # • Stergeti doua absente prin metoda specificata
# s2.stergere(2)
# print(s2)
# # • Afisati absentele fiecarui student
# print(s1.absente)
# print(s2.absente)
# # • Adaugati materia ”Python” impreuna cu o lista formata din 3 numere intre 1-10 pentru
# # fiecare student
# s1 = Extensie1("Roata", "Ion")
# s2 = Extensie1("cerc", "george")
# print(s1)
# print(s2)
# s1.adaugare("Python", [5,5,5])
# s2.adaugare("Python", [8,8,8])
# print(s1)
# print(s2)
#
# # • Adaugati materia ”Matematica” la al doilea student numit George Cerc si “Romana” pentru
# # studentul numit Ion Roata impreuna cu o lista formata din 3 numere intre 1-10 pentru fiecare
# # student
# # • Verificati ce materii are fiecare student prin metoda ce permite afisarea tuturor materilor
# # unui student.
# s1.afisare()
# print(s1)
# s2.afisare()
# print(s2)
# # • Verificati ce materii si ce note mediate au studentii.
# print(s1.final_grade())
# print(s2.final_grade())





