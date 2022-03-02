import pandas as pd
import csv
import datetime
actiune = ""
id = 0

lista_categorii = list(["curs", "cumparaturi", "munca", "cadouri"])

task = input("Spune-mi task-ul: ")

data_limita = input("Spune-mi data limita: ")


def verificare_data():

    data_verificata = data_limita
    try:
        datetime.datetime.strptime(data_verificata, "%d.%m.%Y %H:%M")
        return True
    except ValueError:
        return "Data introdusa nu este corecta sau nu este introdusa corect. "


responsabilul = input("Spune-mi persoana responsabila de task: ")

categorie_task = input("Spune-mi categoria din care face parte task-ul: ")

if categorie_task in lista_categorii:
    pass
else:
    print("Categoria introdusa nu face parte din lista de categorii")

status = input("Spune-mi statusul task-ului: activ sau inactiv: ")

linie_task = {
    "id": 1,
    "task": task,
    "deadline": data_limita,
    "persoana_responsabila": responsabilul,
    "categoria_task": categorie_task,
    "status": status

}

coloane_tabel = [task, data_limita, responsabilul, categorie_task, status]
tabel_tasks = pd.DataFrame(coloane_tabel)

while actiune != 'i':
    actiune = str(input("Actiuni asupra datelor din tabel : 'l' inseamna listare date (afisare date),"
                        "'s' inseamna sortare date, 'f' inseamna filtrare date, 'ad' inseamna adaugare task-uri, "
                        "'e' inseamna editare date,'d' inseamna stergere date, "
                        "'i' inseamna ca nu mai adaugam date noi "))
    if actiune == 'l':
        tabel_tasks.sort_values(categorie_task)
        print(tabel_tasks)

    elif actiune == 'ad':
        tabel_tasks_adaugat = tabel_tasks
        task = input("Spune-mi task-ul: ")
        data_limita = input("Spune-mi data limita: ")
        responsabilul = input("Spune-mi persoana responsabila de task: ")
        categorie_task = input("Spune-mi categoria din care face parte task-ul: ")
        status = input("Spune-mi statusul task-ului: activ sau inactiv: ")
        tabel_tasks_adaugat = tabel_tasks_adaugat.append({
            "id": 1,
            "task": task,
            "deadline": data_limita,
            "persoana_responsabila": responsabilul,
            "categoria_task": categorie_task,
            "status": status
        }, ignore_index=True)
        print(tabel_tasks)

    elif actiune == "d":
        task_de_sters = int(input("Alege id-ul de la task-ul ce vrei sa fie sters"))
        tabel_tasks_actualizat = tabel_tasks
        tabel_tasks_actualizat.drop([task_de_sters], inplace=True)
        print(tabel_tasks_actualizat)

    elif actiune == "s":
        sortare_date = int(input("Scrie doar cifra aferenta sortarii fiecarei optiuni de mai jos:"
                                 " '1' pentru sortare ascendentă task,"
                                 " '2' pentru sortare descendentă task,"
                                 " '3' pentru sortare ascendentă data,"
                                 " '4' pentru sortare descendentă data, "
                                 " '5' pentru sortare ascendentă persoana responsabilă"
                                 " '6' pentru sortare descendentă persoană responsabilă,"
                                 " '7' pentru sortare ascendentă categorie,"
                                 " '8' pentru sortare descendentă categorie "))
        tabel_tasks_sortat = tabel_tasks
        if sortare_date == 1:
            tabel_tasks_sortat.sort_values(categorie_task)
            print(tabel_tasks_sortat)
        elif sortare_date == 2:
            tabel_tasks_sortat.sort_values(categorie_task, ascending=False)
            print(tabel_tasks_sortat)
        elif sortare_date == 3:
            tabel_tasks_sortat.sort_values(data_limita)
            print(tabel_tasks_sortat)
        elif sortare_date == 4:
            tabel_tasks_sortat.sort_values(data_limita, ascending=False)
            print(tabel_tasks_sortat)
        elif sortare_date == 5:
            tabel_tasks_sortat.sort_values(responsabilul)
            print(tabel_tasks_sortat)
        elif sortare_date == 6:
            tabel_tasks_sortat.sort_values(responsabilul, ascending=False)
            print(tabel_tasks_sortat)
        elif sortare_date == 7:
            tabel_tasks_sortat.sort_values(categorie_task)
            print(tabel_tasks_sortat)
        elif sortare_date == 8:
            tabel_tasks_sortat.sort_values(categorie_task, ascending=False)
            print(tabel_tasks_sortat)
        else:
            pass

    elif actiune == "f":
        tabel_tasks_filtrat = tabel_tasks
        filtrare_date = int(input("Scrie cifra câmpulului după care se realizeaza filtrarea: '1' filtrare dupa task,"
                                  "'2' filtrare dupa data, '3' filtrare dupa responsabil,'4' filtrare dupa categorie"))
        if filtrare_date == 1:
            tabel_tasks_filtrat.query(categorie_task, inplace=True)
            print(tabel_tasks_filtrat)
        elif filtrare_date == 2:
            tabel_tasks_filtrat.query(data_limita, inplace=True)
            print(tabel_tasks_filtrat)
        elif filtrare_date == 3:
            tabel_tasks_filtrat.query(responsabilul, inplace=True)
            print(tabel_tasks_filtrat)
        elif filtrare_date == 4:
            tabel_tasks_filtrat.query(categorie_task, inplace=True)
            print(tabel_tasks_filtrat)
        else:
            pass


#  Editarea detaliilor referitoare la task dată, persoană sau categorie dintr-un anumit task ales de utilizator de la
#  tastatură (când se cere această opțiune, se va lista lista de taskuri cu un identificator unic pe rand, astfel încât
#  să se știe ce informație urmează să editeze utilizatorul)
