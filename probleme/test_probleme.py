# 1. Realizati o functie care sa inlocuiasca textul din variabila string aflat
# intre valorile “start” si “end” cu textul din “text”.

# string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be
# introduced."
# # [start, end, text]

# patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]
# Textual rezultat este: The Conquistator must meet King on top of Palace battlements to be introduced.

# Numaratoarea de start si end incepe cu indexul 1. Se pot introduce de la
# tastatura alte valori pentru index si text, cat si un numar mai mare de liste.
#

# def string_inital(*args):
#
#     text = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
#     a = text.split(" ")
#     a[1] = "Conquistador"
#     a[4] = "King"
#     a[8] = "Palace"
#     return ' '.join(a)
#
# print(string_inital())


# def string_v2 ():
# text = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
# text_reversed = text[::-1]
# a = input("Spune-mi indexul de inceput ")
# b = input("Spune-mi indexul de final ")
# # print((str[::-1].replace("Skyhold's", "Palace", 1))[::-1])
#
# print(text_reversed)
    # inlocuitor = str(input())

# txt = [a, b, inlocuitor]
    # return text.replace(txt, inlocuitor)

#     return (text_initial)
#
# print(string_v2())



lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']

lista_nume.sort() #1. Sortati lista dupa nume
dictionar_nume = {}

for i in lista_nume: # 2. Determinati numarul de aparitii al fiecarui nume
    dictionar_nume[i] = lista_nume.count(i)
print(dictionar_nume)

# dict_sortat = max(dictionar_nume.values())
# print(dict_sortat.keys())

# dictionar_nume = {}
# for i in lista_nume:
#     dictionar_nume[i] = lista_nume.count(i)
#     all_values = dictionar_nume.values()
#     max_value = max(all_values)
# print(max_value)




# 3. Listati numele care apare de cele mai multe ori in lista initiala.
# 4. Listati numele care apare de cele mai putine ori in lista initiala.









