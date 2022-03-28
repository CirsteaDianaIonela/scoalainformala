# Problema 1
# class Catalog:
#
#     def __init__(self, nume, prenume):
#         self.nume = nume
#         self.prenume = prenume
#         self.absente = 0
#         self.materii = {}
#
#     def __str__(self):
#         return f'{self.nume, self.prenume, self.materii, self.absente}'
#
#     def incrementeaza_abs(self):
#         self.absente += 1
#
#     def delete_absente(self, numar_absente):
#         if self.absente > numar_absente:
#             self.absente -= numar_absente
#
#
# class Extensie1(Catalog):
#     def __init__(self, nume, prenume):
#         super().__init__(nume, prenume)
#         print(self.materii)
#
#     def add_subject(self, materie, note):
#         self.materie = self.materii.update({materie: note})
#
#     def print_all(self):
#         return f"{self.materii.keys()}"
#
#     def final_grade(self):
#         note_finale = {}
#         for i,j in self.materii.items():
#             if all(isinstance(x, int) for x in j):
#                 medie = sum(j) / len(j)
#                 note_finale.update({i: medie})
#         return note_finale
#
#
#
# student = Catalog("Roata", "Ion")
# print(student)
# student.incrementeaza_abs()
# student.incrementeaza_abs()
# student.incrementeaza_abs()
# print(student)
# student.delete_absente(2)
# print(student)
#
# student2 = Catalog("Cerc", "George")
# student2.incrementeaza_abs()
# student2.incrementeaza_abs()
# student2.incrementeaza_abs()
# student2.incrementeaza_abs()
# print(student)
# student2.delete_absente(2)
# print(student2)
#
# obj = Extensie1("Ana", "Maria")
# obj.add_subject("Python", [5,7,9])
# obj.add_subject("Java", [5,5,5])
# print(obj.print_all())
# print(obj.final_grade())

# Problema 2
# from operator import itemgetter
#
#
# class CatalogPrajituri:
#
#     lista_prajituri = []
#
#     def __init__(self, nume = "Chec", pret = 100, gramaj = 500):
#         self.nume = nume
#         self.pret = pret
#         self.gramaj = gramaj
#         catacteristici_obiect = [self.nume, self.pret, self.gramaj]
#         self.lista_prajituri.append(catacteristici_obiect)
#
#     @staticmethod
#     def sortare_gramaj():
#         sortare_gramaj = sorted(CatalogPrajituri.lista_prajituri, key = itemgetter(2))
#         return f"Prajiturile sortate in functie de gramaj sunt {sortare_gramaj}"
#
#     @staticmethod
#     def sortare_pret():
#         sortare_pret = sorted(CatalogPrajituri.lista_prajituri, key = itemgetter(1))
#         return f"Prajiturile sortate in functie de pret sunt {sortare_pret}"
#
#
# class Tort(CatalogPrajituri):
#     def __init__(self, nume, gramaj, pret, etajat = False, glazura = "ciocolata"):
#         super().__init__(nume, gramaj, pret)
#         self.etajat = etajat
#         self.glazura = glazura
#
#     def __str__(self):
#         return f"Etajarea este {self.etajat} si glazura este {self.etajat}"
#
#
# class Fursec(CatalogPrajituri):
#     pass
#     # def __init__(self):
#     #     super().__init__()
#
#
# prajutura2 = CatalogPrajituri("Ecler mare", 10, 15)
# prajutura1 = CatalogPrajituri("Ecler mic", 5, 10)
# prajutura3 = CatalogPrajituri("Carpati", 15, 20)
#
# tort1 = Tort(nume = "A", pret = 150, gramaj = 112, etajat=True, glazura = "cacao")
# tort2 = Tort(nume = "D", pret = 55, gramaj = 45, etajat=True, glazura = "cacao")
# tort3 = Tort(nume = "B", pret = 1150, gramaj = 350, etajat=True, glazura = "cacao")
# # fursec1 = Fursec()
# # print(fursec1.nume)
#
# print(CatalogPrajituri.lista_prajituri)
# print(CatalogPrajituri.sortare_pret())
# print(CatalogPrajituri.sortare_gramaj())

# print(tort1.glazura)
# print(tort1.gramaj)
# print(tort1.nume)

# print(tort1)
# print(tort2)
# print(tort3)

# Ex 3
#
# class CatalogAuto:
#     def __init__(self, marca, tip):
#         self.marca = marca
#         self.tip = tip
#
#     def schimbare_culoare(self, culoare):
#         self.culoare = culoare  #am folosit self ca sa il facem atribut de clasa ca sa il folosim si in alte metode
#
#     def __str__(self):
#         return f"Culoarea este: {self.culoare}"
#
#
# class ScauneIncalzite(CatalogAuto):
#     def __init__(self, scaune_incalzite, marca, tip):
#         super().__init__(marca, tip)
#         self.scaune_incalzite = scaune_incalzite
#
#     def __str__(self):
#         return f"Marca este: {self.marca}, tip-ul este {self.tip}, scaune incalzite: {self.scaune_incalzite}"
#
#
# class BlocuriOptice(CatalogAuto):
#     def __init__(self, blocuri_optice, marca, tip):
#         super().__init__(marca, tip)
#         self.blocuri_optice = blocuri_optice
#
#     def __str__(self):
#         return f"Marca este: {self.marca}, tip-ul este {self.tip}, blocuri oprice {self.blocuri_optice} "
#
#
# obiect_clasa2 = ScauneIncalzite(marca="ARO", tip=461, scaune_incalzite="Nu")
# print(obiect_clasa2)
# obiect_clasa2.schimbare_culoare("rosu")
# print(obiect_clasa2.culoare)
# object_2 = BlocuriOptice(marca="Dacia", tip=1310, blocuri_optice="Nu")
# print(object_2)
# object_2.schimbare_culoare("negru")
# print(object_2.culoare)
# print(object_2.culoare, object_2.blocuri_optice, object_2.marca, object_2.tip)
# print(obiect_clasa2.culoare, obiect_clasa2.scaune_incalzite, obiect_clasa2.marca, obiect_clasa2.tip)



# 1. Creati o clasa care sa calculeze si sa returneze operatia matematica de mai jos pentru
# 4 numere: [a(b+3)/c]*d.
# Clasa trebuie sa aiba 2 metode: prima metoda este metoda speciala init.
# Iar cea dea doua metoda este metoda speciala str.
# Va rog sa aplicati cel putin doua exemple (doua obiecte).
# Metoda init trebuie sa foloseasca parametrii default a=1,b=2,c=3,d=4 si trebuie sa suprime
# orice eroare.
# La aparitia unei erori trebuie sa afiseze textul: <>
# Folositi clasa in trei exemple:
# • cu patru parametrii numerici diferiti de cei default
# • cu 3 parametrii non-numerici
# • cu 2 parametrii numerici


class Calcul:
    def __init__(self, a=1, b=2, c=3, d=4 ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def verificare(self):
        self.e = f"Informatiile introduse nu sunt cifre"
        if str(self.a).isnumeric() and str(self.b).isnumeric()and str(self.c).isnumeric() and str(self.d).isnumeric():
            self.e = (self.a * (self.b + 3) / self.c) * self.d
        return self.e

    def __str__(self):
        return f"Rezultatul este: {self.verificare()}"

obiect = Calcul()
print(obiect)
obiect2=Calcul(5,6,7,8)
print(obiect2)
obiect3 = Calcul("x","y","z",2)
print(obiect3)
obiect4 = Calcul(9,2)
print(obiect4)


