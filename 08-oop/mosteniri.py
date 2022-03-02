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


