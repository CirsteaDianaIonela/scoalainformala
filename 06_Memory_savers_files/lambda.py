# my_lambda = lambda x, y: x+y
# #definire functie = lambda param 1, param 2: corp functie
# my_sum=my_lambda(2,3)
# print(my_sum)
#
# def my_lambda(x,y):
#     return  x+y
#
# diferenta = lambda x,y: x-y
# diferenta_mea=diferenta(4,3)
# print(diferenta_mea)
#
# players=[
#     {"first name":"Ion","last_name":"Gheorghe","varsta":12
# },
#     {
#     "first name":"Andreea","last_name":"Popa","varsta":35
# },{
#     "first name":"Isabela","last_name":"Enache","varsta":25
# }
# ]
#
# jucatori_sortati = sorted(players, key=lambda jucator: jucator["varsta"])
# print(jucatori_sortati) #sorteaza dupa varsta


players=[
    {"first_name":"Ion","last_name":"Gheorghe","varsta":12
},
    {
    "first_name":"Andreea","last_name":"Popa","varsta":35
},{
    "first_name":"Isabela","last_name":"Enache","varsta":25
}
]

jucatori_sortati = sorted(players, key=lambda jucator: jucator["first_name"])
print(jucatori_sortati) #sortare dupa first name
