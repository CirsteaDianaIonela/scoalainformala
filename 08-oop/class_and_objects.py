# #clasa reprez sablonul (strctura si comportamentul lui obiect)
# class MyFirstClass:
#     pass
#
# my_first_obect = MyFirstClass()

#
# class Caine:
#     nr_picioare = 4 #atribut al clasei caine, 4 este proprietate
#     def __init__(self, name, age): #constructorul!!!! creaza obiecte cu clase diferite, vrem sa ne definim numele cainelui de ex
#         self.nume = name
#         self.varsta = age
#
#     def __str__(self): #exporta mereu un strig, fara a mai scrie noi print
#         return f"{self.nume} - {self.varsta}"
#
#     def change_name(self, name):
#         self.nume = name
#
# #accesare din interiorul clasei atibutul:
# # print(Caine.nr_picioare)
#
#
# cainele_meu = Caine("Rex") #acesta este un obiect
# # print(cainele_meu.change_name("Ben"))
# # print(cainele_meu)
# print(cainele_meu.varsta)



# class Calculator:
#
#     def __init__(self, op1, op2, operation):
#         self.operator1 = op1
#         self.operator2 = op2
#         self.operatie = operation #self ne ajuta sa putem prelua valorile din paramentii din init
#
#     def adunare (self):
#         return self.operator1 + self.operator2
#
#     def __str__(self):
#         if self.operatie == "+":
#             return f"{self.adunare()}"
#
# obiect1 = Calculator(1, 2, "+")
# print(obiect1)







