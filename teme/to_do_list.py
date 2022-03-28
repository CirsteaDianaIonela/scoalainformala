import pandas as pd
import csv
import datetime

actiune = ""

lista_categorii = [item for item in input("Introduceți categoriile de taskuri: ").split()]
print(f'Lista categoriilor este: {lista_categorii}')


linie_task = {
    "id": [],
    "task": [],
    "deadline": [],
    "persoana_responsabila": [],
    "categoria_task": [],
    "status": []
}

tabel_tasks = pd.DataFrame(linie_task)
print(tabel_tasks)
fisier = tabel_tasks.to_csv("tasks.csv")


while actiune != 'i':  #daca nu merge pune o alta modalitate de iesire in loc de i

    actiune = str(input("Actiuni asupra datelor din tabel : \n'l' inseamna listare date (afisare date),"
                        "\n's' inseamna sortare date, \n'f' inseamna filtrare date, \n'ad' inseamna adaugare task-uri, "
                        "\n'e' inseamna editare date,\n'd' inseamna stergere date, "
                        "\n'i' inseamna ca nu mai facem nicio actiune "))
    if actiune == 'l':
        tabel_tasks = tabel_tasks.sort_values("task") #ok
        tabel_tasks.to_csv("tasks.csv")
        print(tabel_tasks)

    elif actiune == "s": #ok
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

    elif actiune == 'ad': #merge
        numar_task = input("Spune-mi id-ul: ")
        linie_task["id"].append(numar_task)
        task = input("Spune-mi task-ul: ")
        linie_task["task"].append(task)

        data_limita = input("Spune-mi data limita: ") #imi creeaza erorare daca las verificarea datei ValueError: All arrays must be of the same length
        # verificare_data = data_limita
        # try:
        #     datetime.datetime.strptime(verificare_data, "%d.%m.%Y %H:%M")
        #     linie_task["deadline"].append(data_limita)
        # except ValueError:
        #     print("Data nu este valida") # de pus sa reintroduca

        linie_task["deadline"].append(data_limita)

        responsabilul = input("Spune-mi persoana responsabila de task: ")
        linie_task["persoana_responsabila"].append(responsabilul)

        categorie_task = input("Spune-mi categoria din care face parte task-ul: ")
        while categorie_task not in lista_categorii:  # functioneaza partial, de facut in asa fel incat sa nu mai treaca la introducerea statusul daca categoria nu este valida si nu vrea sa reintroduca task-ul
            reintroducere = input(
                "Categoria introdusa nu face parte din lista de categorii. Doriti sa reintroduceti categoria? y/n")
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
    elif actiune == "d": #ok
        task_de_sters = int(input("Alege index-ul de la task-ul ce vrei sa fie sters "))
        tabel_tasks.drop([task_de_sters], inplace=True)
        print(tabel_tasks)
        tabel_tasks.to_csv("tasks.csv")

    elif actiune == "f": #nu functioneaza, imi da erorare
        # tabel_tasks_filtrat = tabel_tasks
        filtrare_date = int(input("Scrie cifra câmpulului după care se realizeaza filtrarea: \n'1' filtrare dupa task,"
                                  "\n'2' filtrare dupa data, \n'3' filtrare dupa responsabil,\n'4' filtrare dupa categorie "))
        if filtrare_date == 1:
            tabel_tasks = tabel_tasks.query("task", inplace=True)
            print(tabel_tasks)
        elif filtrare_date == 2:
            tabel_tasks = tabel_tasks.query("deadline", inplace=True)
            print(tabel_tasks)
        elif filtrare_date == 3:
            tabel_tasks = tabel_tasks.query("persoana_responsabila", inplace=True)
            print(tabel_tasks)
        elif filtrare_date == 4:
            tabel_tasks= tabel_tasks.query("categoria_task", inplace=True)
            print(tabel_tasks)
        else:
            pass


