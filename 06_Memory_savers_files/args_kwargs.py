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
