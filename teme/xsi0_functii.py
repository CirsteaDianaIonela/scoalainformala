# Creati un program ce are ca scop crearea jocului X si 0 in care un participant este uman si celalalt este un robot.
# De asemenea, pentru alegerea unei casute libere de catre masina/robot sau de catre om aveti in vedere urmatoarele:
# • intrarile sunt de la 1 la 9 astfel: 1|2|3 4|5|6 7|8|9
# • pozitia 5 este cea mai vanata
# • pozitia 1 sau 3 sau 7 sau 9 reprezinta optiunea a doua in cerintele unei masini.
# Prima valoare disponibila dintre acestea va fi marcata cu “O” de catre masina/robot
# • In cazul in care toate acestea sunt ocupate se incearca prima valoare ramasa libera dintre 2,4,6,8


import random
choice_list = ["jucator", 'robot']
jucator = None
simbol_jucator = '0'
simbol_robot = 'x'
if random.choice(choice_list) == 'jucator':
    jucator = input('Alege valoarea:')
    simbol_robot = "0"
    simbol_jucator = "x"
msg = " "
lista = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def inceput_joc(jucator,robot):
    jucator = '0'
    robot = 'x'
    if random.choice(choice_list) == 'jucator':
        jucator = input('Alege valoarea:')
        robot = "0"
        jucator = "x"
    return msg


def alegeri_jucator(lista):
        valoare_utilizator = int(input("Spune-mi o un numar intre 1 si 9!"))
        if lista[valoare_utilizator - 1] == "-":
            lista[valoare_utilizator - 1] = '[X]'
            return msg


def alegeri_calculator(lista):

    while "-" in lista:

        if lista[4] == "-":
            lista[4] = "[0]"
        elif lista[0] == "-":
            lista[0] = "[0]"
        elif lista[2] == "-":
            lista[2] = "[0]"
        elif lista[6] == "-":
            lista[6] = "[0]"
        elif lista[8] == "-":
            lista[8] = "[0]"
        else:
            ramas = [1, 3, 5, 7]
            computer_choice = random.choice(ramas)
            while computer_choice not in ramas:
                lista[computer_choice] = "[0]"
                break
        return msg

print(inceput_joc(),alegeri_jucator(lista), alegeri_calculator(lista))
print(lista)
#
# def castigator():
#         if lista[0] == lista[1] == lista[2] != "-":
#             if lista[0] == "[X]":
#                 return True
#             else:
#                 return False
#
#         elif lista[3] == lista[4] == lista[5] != "-":
#             if lista[3] == "[X]":
#                 return True
#             else:
#                 return False
#
#         elif lista[6] == lista[7] == lista[8] != "-":
#             if lista[6] == "[X]":
#                 return True
#             else:
#                 return False
#
#         elif lista[0] == lista[4] == lista[8] != "-":
#             if lista[0] == "[X]":
#                 return True
#             else:
#                 return False
#
#         elif lista[2] == lista[4] == lista[6] != "-":
#             if lista[2] == "[X]":
#                 return True
#             else:
#                 return False
#
#         elif lista[0] == lista[3] == lista[6] != "-":
#             if lista[0] == "[X]":
#                 return True
#             else:
#                 return False
#
#         elif lista[1] == lista[4] == lista[7] != "-":
#             if lista[1] == "[X]":
#                 return True
#             else:
#                 return False
#
#         elif lista[2] == lista[5] == lista[8] != ["-"]:
#             if lista[2] == ["X"]:
#                 return True
#             else:
#                 return False
#         return msg
#
# def joc():
#     if inceput_joc():
#         while not castigator(lista):
#             alegeri_jucator(lista)
#             print("{}\t{}\t{} \n{}\t{}\t{}\n{}\t{}\t{}".
#             format(lista[0], lista[1], lista[2], lista[3],
#                     lista[4], lista[5], lista[6], lista[7], lista[8]))
#             alegeri_calculator(lista)
#             print("{}\t{}\t{} \n{}\t{}\t{}\n{}\t{}\t{}".
#             format(lista[0], lista[1], lista[2], lista[3],
#                     lista[4], lista[5], lista[6], lista[7], lista[8]))
#     else:
#         while not castigator(lista):
#             alegeri_calculator(lista)
#             print("{}\t{}\t{} \n{}\t{}\t{}\n{}\t{}\t{}".
#             format(lista[0], lista[1], lista[2], lista[3],
#                     lista[4], lista[5], lista[6], lista[7], lista[8]))
#             alegeri_jucator(lista)
#             print("{}\t{}\t{} \n{}\t{}\t{}\n{}\t{}\t{}".
#             format(lista[0], lista[1], lista[2], lista[3],
#                     lista[4], lista[5], lista[6], lista[7], lista[8]))
#
# msg = joc()
# print(msg)

