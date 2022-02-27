import csv
import pandas as pd
import datetime

def introducere_lista_todo():

    lista_categorii = list(["curs", "cumparaturi", "munca", "cadouri"])

    task = input("Spune-mi task-ul: ")
    print(task)

    data_limita = input("Spune-mi data limita: ")
    print(data_limita)


    def verificare_data():

        data_verificata = data_limita
        try:
            datetime.datetime.strptime(data_verificata, "%d.%m.%Y %H:%M")
            return True
        except ValueError:
            return False
#TODO sa oprim codul daca functia de data in final sa dea erorare


    print(verificare_data())


    responsabilul = input("Spune-mi persoana responsabila de task: ")
    print(responsabilul)

    categorie_task = input("Spune-mi categoria din care face parte task-ul: ")
    print(categorie_task)


    if categorie_task in lista_categorii:
        pass
    else:
        print("Categoria introdusa nu face parte din lista de categorii")
#TODO de revenit sa oprim codul daca da erorare la if - categorie

    status = input("Spune-mi statusul task-ului: activ sau inactiv ")
    print(status)

# with open("categorii.csv","w") as csv_file_categorii:
#     csv_writer = csv.writer(csv_file_categorii)
#     for categ in lista_categorii:
#         csv_writer.writerow(categ)
#


# file = open("categorii.csv", "w")
# file.write(task)
# file.close()
#TODO de actualizat dupa ce introducem toate datele


    global linie_task
    linie_task= [{
    "id" : 1,
    "task" : task,
    "deadline" : data_limita,
    "persoana_responsabila" : responsabilul,
    "categoria_task" : categorie_task,
    "status": status

}
]
    print(linie_task)
    lista_linie_task = list(linie_task)
    alegere_operatii = input("Doriti listare? y/n")
    if alegere_operatii == "n":
        print(lista_linie_task)

    else:
        listare = sorted(lista_linie_task, key = lambda sort: sort ["categoria_task"])
        print(listare)
#TODO am erorare
introducere_lista_todo()



