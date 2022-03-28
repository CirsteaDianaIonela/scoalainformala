# def my_function(*param_1):
#     print(type(param_1))
#     return param_1
#
#
# print(my_function('string','string','string'))

# def numbers_sum(param_1, *var):
#     suma=0
#     for item in var:
#         suma = suma + item
#     return suma
#
# print(numbers_sum(1,2,3,4,5))
#
#
# def diff_vars(*params): #o lista cu un numar nedefinit de paramentrii si *ia tot
#     diferenta = 0 #de aici pleaca
#     for item in params:
#         diferenta = diferenta - item
#     return diferenta
# print(diff_vars(1, 2, 3, 4)) #calculeaza 0-1-2-3-4=-15, cifrele din print noi le dam pentru ca pentru acelea vrem noi sa calculeze

# def catalog(**kwargs):
#     return  kwargs.keys() #afiseaza doar cheile, s-a creat un dictionar
#
# print(catalog(nume="Popa", prenume = "Ionut", varsta = "12"))
#
#
# # *tuplu
# # **dictionar, argumente bazate pe chei
#
# def catalog(*args,**kwargs):
#     return  args, kwargs.keys()
#
# print(catalog(1, 2, nume="Popa", prenume = "Ionut", varsta = "12"))

# def numbers_sum(*var):
#     suma = 0
#     for item in var:
#         suma = suma + item
#     return suma
# print(numbers_sum(1,2,3,4,5))

# def diferenta(*var):
#     dif = 0
#     for item in var:
#         dif= item - dif
#     return dif
# print(diferenta(5,4))



# def functie_impartire(*args):
#     impartire = 1
#     for item in args:
#         impartire=item/impartire
#     return impartire
# print(functie_impartire(2,4))


#
# def functie_inmultire(*arg):
#     inmultire  = 1
#     for item in arg:
#         inmultire= inmultire * item
#         return inmultire
# print(functie_inmultire(3,4))
#

# def catalog(*args, **kwargs):
#     return args, kwargs.values()
#
# print(catalog(1,2, nume= "Cirstea", prenume = "Diana", varsta = "27"))
#))
#
#

# nr_introdus = input("Spune-mi un numar ")
# def tema2():
#         if nr_introdus.isdigit():
#             return nr_introdus
#         else:
#             return "0"
# print(tema2())


























