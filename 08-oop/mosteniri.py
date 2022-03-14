#1. vehicul este super clasa
#1.1 vehicul de apa
#1.2 vehicul de aer
#1.3 vehicul de spatiu
#1.4 vehicul terestru
#de la 1.1 la 1.4 sunt subclase a clasei mare
# 1.4.1 vehicul de teren
#1.4.2 vehicul de curse -> subclase ale lui 1.4


# 2. Animale
# 2.1 mamifere
# 2.1.1 animale salbatice
# 2.1.2 anibale domestice
# 2.2 reptile
# etc
#  2 este pt 2.1 si 2.2 este superclasa
# 2.1 si 2.2 pentru 2 sunt subclase
# 2.1.1 si 2.1.2 pentru 2.1 sunt subclase
# 2.2.1 si 2.1.2 pentru 2 sunt subclase


# Max este un caine mare care doarme toata ziua
# doresc sa scot obiectul -> este un substantiv: Max
# doresc sa scot clasa -> caine (substantiv)
# doresc sa scot proprietatea -> mare (adjectiv) : mic,mare,mediu -> poate fi modificabila
# doresc sa scot activitatea -> verbul/actiunea/activitatea prin care definim o metoda in cadrul clasei: doarme, din verb scoatem metode


# Un Logan verde merge incet
# obiect: logan
# clasa: masina -> chiar daca nu e scris
# proprietate: verde
# activitate: merge incet


# Lenovo-ul gri se poate cumpara la un pret mai mic de pe magazinul online
# obiect: Lenovo -> se poate schimba
# clasa: calculator
# proprietate: gri -> se poate schimba
# activitate: se poate cumpara -> se poate schimba


#Sa se realizeze jocul x si 0 intre 2 jumcatori in care:
# primul jucator este mereu calculatorul
# exista reguli de joc pentru mutari
# obiect: calculatorul/omul
# clasa: jocul
# proprietate: regulile
# activitate: mutarile / calculul de scor al jocului


# class MyFirstClass:
# pass
#
# object = MyFirstClass()

# problema stivei -> farfurii puse in chiuveta la spalat, ultima pusa e prima spalata

# stack = []
#
# def push(val):
#     stack.append(val)
#     return stack #asa adaugam valori in stiva
#
# def pop():
#     val = stack[-1] #stergem una cate una de la coada la cap
#     del stack[-1] #del sterge
#     return val
#
# print(push(3))
# print(push(2))
# print(push(1))
#
# print(pop())
# print(pop())
# print(pop())


# adaugam tot ce mai sus intr-o clasa
# class Stack:
#     def __init__(self): #initializare -> constructor
#         self.__stack_list = [] #daca pun__ inainte de stack list, fac proprietatea privata -> INCAPSULARE, nu poate fi accesibila, initizam o lista goala ce urmeaza a fi umpluta
#
#     def push(self, val): #activitate, metoda pentru a adauga
#         self.__stack_list.append(val) #folsim self pt ca ne refeim la lista din constructor (stack_list)
#
#     def pop (self): #activitate, metoda pt a sterge
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#     def __str__(self):#metoda pt a vedea elementele, NEAPARAT, este un fel de print
#         return f'{self.__stack_list}'
#
# obiect_stiva = Stack()
# obiect_stiva.push(3)
# print(obiect_stiva)
# obiect_stiva.push(2)
# print(obiect_stiva)
# obiect_stiva.push(1)
# print(obiect_stiva)
# obiect_stiva.pop()
# print(obiect_stiva)
# obiect_stiva.pop()
# print(obiect_stiva)
# obiect_stiva.pop()
# print(obiect_stiva)   #stack_list este proprietatea
#

# class ClasaExemplu:
#     def __init__(self, val=1):
#         self.first = val #first este PROPRIETATE
#         self.second = 0 #second este PROPRIETATE
#
#     def set_second(self, val=2):
#         self.second = val
#
#     def __str__(self):
#         return f"{self.first, self.second}"
#
#
# obiect_1 = ClasaExemplu() #nu atribuim o valoare default, deci ramane cu val =1
# obiect_2 = ClasaExemplu(2)  # merge in constructor si pune 2 pe val
# obiect_3 = ClasaExemplu(3)
# print(obiect_1)
# print(obiect_2)
# print(obiect_3)
# print(obiect_3.second)


#apelarea clasei se numeste instatiere - INSTANCE

#!!!!! PENTRU VEDEA PROPRIETATILE FOLOSIM __dict__
# print(obiect_1.__dict__)

# !!!!!!!!VEZI IN INREGISTRARE CUM POTI ACCESA O PROPRIETATE PRIVATA
# !!!!!!!!VEZI IN INREGISTRARE CUM POTI modifica atributeele de dinainte de initializare
# !!!!!!!!VEZI IN INREGISTRARE atribute la nivel de clasa si cele la nivel de obiect
# !!!!!!!!VEZI IN INREGISTRARE daca exita atribute la nivel obiect
# !!!!!!!!VEZI IN INREGISTRARE hasattr -> verifica daca exista atributul respectiv
# numele unei case se verifica cu prin(type(obiect1).__name__)

# MOSTENIRI:

# Ex1:
# class Star:
#     def __init__(self, nume, galaxie):
#         self.name = nume
#         self.galaxy = galaxie
#
#     def __str__(self): #ce vrem sa afisam pe ecran
#         return f'{self.name} este in {self.galaxy}'
#
# soare = Star("Soarele", "Calea Lacteei")#definire obiect soare
# print(soare)


# Ex2:

#vehicul #clasa principala
#vehicul de teren  #subclasa
#vehicul de tractare #subclasa de subclasa
#citirea se face de la stanga la dreapta

#
# class Vehicul:
#     pass
#
# class VehiculTeren(Vehicul): #subclasa VehiculTeren, clasa principala Vehicul -> pun in paranteza clasa mama
#     pass
#
# class VehiculTractare(VehiculTeren):
#     pass

#parinti sunt: Vehicul pentru VehiculTeren (direct) si VehiculTranctare (indirect)
#parinti sunt Vehicul Teren pentru VehiculTractare
#parintii sunt superclasa pentru copii (superclass)
#copii sunt VehiculTeren (direct) si VehiculTractare (indirect) pentru Vehicul
#copilul este VehiculTractare pentru VehiculTeren
#copiii se numesc subclase

# print("Vehicul VehiculTeren VehiculTractare")
# for cls1 in [Vehicul, VehiculTeren, VehiculTractare]:
#     for cls2 in [Vehicul, VehiculTeren, VehiculTractare]:
#         print(issubclass(cls1, cls2), end = '\t') #afiseaza o lista cu valorile superclaselor

# vehicul1 = Vehicul() #instante
# vehicul_teren = VehiculTeren()
# vehicul_tractare = VehiculTractare()
# # print(isinstance(vehicul1, VehiculTractare)) #vedem daca o clasa are mostenire din alta clasa
#
# for obj in [vehicul1, vehicul_teren, vehicul_tractare]:
#     for cls in [Vehicul, VehiculTeren, VehiculTractare]:
#         print(isinstance(obj, cls), end = '\t')
#     print()
#

#
# # EX 3
# class Exemplu:
#
#     def __init__(self, val):
#         self.value = val
#
# obiect_1 = Exemplu(0) #returneaza
# # print(obiect_1.value, '223')
# obiect_2 = Exemplu(2)
# # print(obiect_2.value, '225')
# obiect_3 = obiect_1
# # print(obiect_3, obiect_1, "227")
# obiect_3.value += 1
#
# # print(obiect_1 is obiect_2 ) #false
# # print(obiect_2 is obiect_3)
# # print(obiect_3 is obiect_1) #true)
# # print(obiect_1.value, obiect_2.value, obiect_3.value)
#
# string1 = "Maria are mere"
# string2 = string1
# string2 = 'www'
#
# # string2 = "Maria are mere mari"
# # string1 += "mari"
#
# print(string1 == string2, string1 is string2)


# Ex:4

class SuperClass:
    supVar = 1
    variabila_clasa = 6

    def __init__(self, nume):
        self.name = nume
        self.var_1 = 101

    def __str__(self):
        return f'Numele meu este {self.name}'


class Clasa3:
    variabila_clasa = 5
    def __int__(self,nume):
        self.name = nume
        self.var_2 = 201


class SubClass(Clasa3, SuperClass):
    subVar = 2
    supVar = 3
    def __init__(self, nume):
        self.var_1 = 202
        print(self.var_1)
        super().__init__(nume) #ne ajuta daca avem mai multe mosteniri, invoca constructorul super clasei, ne da acces la toate resursele super clasei
        self.var_3 = 301
        # self.name = nume
        # Super.__init__(self,nume)

    # def __str__(self):
    #     return f'Nume'

obiect = SubClass("Alexandra")
# print(obiect.subVar)
# print(obiect.supVar)
# print(obiect.variabila_clasa)
print(obiect.var_3)
# print(obiect.var_2)
# print(obiect.var_1)





