import pandas as pd
import csv
import datetime

actiune = ""

linie_task = {
    "id": [1, 2, 3],
    "task": ['citit', 'inot', 'prajitura'],
    "deadline": ['20.08.2022 22:05', '15.07.2022 20:10', '23.11.2022 14:00'],
    "persoana_responsabila": ['Diana', 'George', 'Roza'],
    "categoria_task": ['curs', 'sport', 'gatit'],
    "status": ['activ', 'activ', 'activ']
}
#datele initiale asupra carora se vor putea aplica actiunile din meniu

tabel_tasks = pd.DataFrame(linie_task)
fisier = tabel_tasks.to_csv("tasks.csv")

with open('tasks.csv', 'w') as file:
    writer = csv.writer(file)

categ_tasks = pd.DataFrame(linie_task["categoria_task"])
fisier2 = categ_tasks.to_csv("categorii_tasks.csv")

while actiune != 'i':

    actiune = str(input("Actiuni asupra datelor din tabel : \n'l' inseamna listare date (afisare date),"
                        "\n's' inseamna sortare date, \n'f' inseamna filtrare date, \n'ad' inseamna adaugare task-uri, "
                        "\n'e' inseamna editare date,\n'd' inseamna stergere date, "
                        "\n'i' inseamna ca nu mai facem nicio actiune "))
    if actiune == 'l':
        tabel_tasks = tabel_tasks.sort_values("task")
        tabel_tasks.to_csv("tasks.csv")
        print(tabel_tasks)

    elif actiune == "s":
        sortare_date = int(input("Scrie doar cifra aferenta sortarii fiecarei optiuni de mai jos:"
                                     " \n'1' pentru sortare ascendentă task,"
                                     " \n'2' pentru sortare descendentă task,"
                                     " \n'3' pentru sortare ascendentă data,"
                                     " \n'4' pentru sortare descendentă data, "
                                     " \n'5' pentru sortare ascendentă persoana responsabilă"
                                     " \n'6' pentru sortare descendentă persoană responsabilă,"
                                     " \n'7' pentru sortare ascendentă categorie,"
                                     " \n'8' pentru sortare descendentă categorie "))
        if sortare_date == 1:
            tabel_tasks = tabel_tasks.sort_values("task")
            tabel_tasks.to_csv("tasks.csv")
            print(tabel_tasks)
        elif sortare_date == 2:
            tabel_tasks = tabel_tasks.sort_values("task", ascending=False)
            tabel_tasks.to_csv("tasks.csv")
            print(tabel_tasks)
        elif sortare_date == 3:
            tabel_tasks = tabel_tasks.sort_values("deadline")
            tabel_tasks.to_csv("tasks.csv")
            print(tabel_tasks)
        elif sortare_date == 4:
            tabel_tasks = tabel_tasks.sort_values("deadline", ascending=False)
            tabel_tasks.to_csv("tasks.csv")
            print(tabel_tasks)
        elif sortare_date == 5:
            tabel_tasks = (tabel_tasks.sort_values("persoana_responsabila"))
            tabel_tasks.to_csv("tasks.csv")
            print(tabel_tasks)
        elif sortare_date == 6:
            tabel_tasks = tabel_tasks.sort_values("persoana_responsabila", ascending=False)
            tabel_tasks.to_csv("tasks.csv")
            print(tabel_tasks)
        elif sortare_date == 7:
            tabel_tasks = tabel_tasks.sort_values("categoria_task")
            tabel_tasks.to_csv("tasks.csv")
            print(tabel_tasks)
        elif sortare_date == 8:
            tabel_tasks = tabel_tasks.sort_values("categoria_task", ascending=False)
            tabel_tasks.to_csv("tasks.csv")
            print(tabel_tasks)
        else:
            pass

    elif actiune == 'ad':
        numar_task = int(input("Spune-mi id-ul: "))
        linie_task["id"].append(numar_task)
        task = input("Spune-mi task-ul: ")
        linie_task["task"].append(task)

        data_limita = input("Spune-mi data limita, acesta trebuie sa aiba urmatoarea structura DD.MM.YYYY HH:MM: ")
        verificare_data = data_limita
        linie_task["deadline"].append(data_limita)

        responsabilul = input("Spune-mi persoana responsabila de task: ")
        linie_task["persoana_responsabila"].append(responsabilul)

        categorie_task = input("Spune-mi categoria din care face parte task-ul: ")
        lista_categorii = linie_task['categoria_task']
        while categorie_task not in lista_categorii:
            reintroducere = input(
                "Categoria introdusa nu face parte din lista de categorii. Doriti sa reintroduceti categoria? y/n ")
            if reintroducere == "y":
                categorie_task = input("Spune-mi categoria din care face parte task-ul: ")
            else:
                break
        linie_task["categoria_task"].append(categorie_task)

        status = input("Spune-mi statusul task-ului: activ sau inactiv: ")
        linie_task["status"].append(status)
        tabel_tasks = pd.DataFrame(linie_task)
        tabel_tasks.to_csv("tasks.csv")
        print(tabel_tasks)

    elif actiune == "d":
        task_de_sters = int(input("Alege index-ul de la task-ul ce vrei sa fie sters "))
        tabel_tasks.drop([task_de_sters], inplace=True)
        print(tabel_tasks)
        tabel_tasks.to_csv("tasks.csv")

    elif actiune == "f":
        filtrare_date = int(input("Scrie cifra câmpulului după care se realizeaza filtrarea: \n'1' filtrare dupa task,"
                                  "\n'2' filtrare dupa data, \n'3' filtrare dupa responsabil,"
                                  "\n'4' filtrare dupa categorie "))
        if filtrare_date == 1:
            a = input("Spune-mi task-ul dupa care sa efectuam filtrarea:")
            date_filtrate = tabel_tasks[tabel_tasks.task.str.contains(a)]
            print(date_filtrate)

        elif filtrare_date == 2:
            a = input("Spune-mi data dupa care sa efectuam filtrarea:")
            date_filtrate = tabel_tasks[tabel_tasks.deadline.str.contains(a)]
            print(date_filtrate)

        elif filtrare_date == 3:
            a = input("Spune-mi responsabilul dupa care sa efectuam filtrarea:")
            date_filtrate = tabel_tasks[tabel_tasks.persoana_responsabila.str.contains(a)]
            print(date_filtrate)
        else:
            a = input("Spune-mi categoria dupa care sa efectuam filtrarea:")
            date_filtrate = tabel_tasks[tabel_tasks.categoria_task.str.contains(a)]
            print(date_filtrate)

tabel_tasks = pd.DataFrame(linie_task)
fisier = tabel_tasks.to_csv("tasks.csv")
