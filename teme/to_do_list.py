import pandas as pd
import csv
import datetime
actiune = ""
id = 0

# În prima faza se adaugă categoriile dorite de la tastatură:

lista_categorii = [item for item in input("Introduceți categoriile de taskuri: ").split()]
print(f'Lista categoriilor este: {lista_categorii}')


# Cerinte initiale: introducere de la tastatura

task = input("Spune-mi task-ul: ")

data_limita = input("Spune-mi data limita: ")

# if datetime.datetime.strptime(data_limita, "%d.%m.%Y %H:%M"):
#     pass
# else:
#     print("Data introdusa nu este corecta sau nu este introdusa corect, reincearca", data_limita)


data_verificata = data_limita

# while datetime.datetime.strptime(data_verificata, "%d.%m.%Y %H:%M"):
#     break
# else:
#     print("Data introdusa nu este corecta sau nu este introdusa corect.  ")
#     raspuns1 = input("Doriti sa reintroduceti data? y/n")
#     if raspuns1 == 'y':
#         data_limita = input("Spune-mi data limita: ")
#         print(data_limita)
#     else:  ###de pus aici ce sa returneaze
#         print("Nu se mai continua")


responsabilul = input("Spune-mi persoana responsabila de task: ")

categorie_task = input("Spune-mi categoria din care face parte task-ul: ")

while categorie_task not in lista_categorii: # functioneaza partial, de facut in asa fel incat sa nu mai treaca la introducerea statusul daca categoria nu este valida si nu vrea sa reintroduca task-ul
    reintroducere = input("Categoria introdusa nu face parte din lista de categorii. Doriti sa reintroduceti categoria? y/n")
    if reintroducere == "y":
        categorie_task = input("Spune-mi categoria din care face parte task-ul: ")
    else:
        break


status = input("Spune-mi statusul task-ului: activ sau inactiv: ")

linie_task = {
    "id": id+1,
    "task": task,
    "deadline": data_limita,
    "persoana_responsabila": responsabilul,
    "categoria_task": categorie_task,
    "status": status

}

coloane_tabel = [task, data_limita, responsabilul, categorie_task, status]
tabel_tasks = pd.DataFrame(coloane_tabel) #de scris in csv
print(tabel_tasks)

def meniu():

    actiune = int(input("Alege actiunea ce urmeaza sa fie executata asupra datelor : "
                        "\n1 Listare date: în afișarea inițială a datelor se realizează o sortare în "
                        "funcție de categorie"
                        "\n2 Sortare date \n3 Filtrare date \n4 Adăugarea unui nou task "
                        "\n5 Editarea detaliilor referitoare la task \n6 Ștergerea unui task "
                        "\n7 Nicio actiune "))
    return actiune


if meniu() == 1:

    while actiune != 'i': #daca nu merge pune o alta modalitate de iesire in loc de i
        actiune = str(input("Actiuni asupra datelor din tabel : \n'l' inseamna listare date (afisare date),"
                        "\n's' inseamna sortare date, \n'f' inseamna filtrare date, \n'ad' inseamna adaugare task-uri, "
                        "\n'e' inseamna editare date,\n'd' inseamna stergere date, "
                        "\n'i' inseamna ca nu mai facem nicio actiune"))
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
                                     " \n'1' pentru sortare ascendentă task,"
                                     " \n'2' pentru sortare descendentă task,"
                                     " \n'3' pentru sortare ascendentă data,"
                                     " \n'4' pentru sortare descendentă data, "
                                     " \n'5' pentru sortare ascendentă persoana responsabilă"
                                     " \n'6' pentru sortare descendentă persoană responsabilă,"
                                     " \n'7' pentru sortare ascendentă categorie,"
                                     " \n'8' pentru sortare descendentă categorie "))
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
            filtrare_date = int(input("Scrie cifra câmpulului după care se realizeaza filtrarea: \n'1' filtrare dupa task,"
                                      "\n'2' filtrare dupa data, \n'3' filtrare dupa responsabil,\n'4' filtrare dupa categorie"))
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

