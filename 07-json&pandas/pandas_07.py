import pandas as pd


# dictionar_date = {
#     "masini": ["Dacia", "Volvo", "Renault"],
#     "culoare": ["rosu", "alb", "verde"]
# }
#
# variabila = pd.DataFrame(dictionar_date)
# print(variabila)

#
# masini =["Dacia", "Volvo", "Renault"]
# variabila=pd.Series(masini)
# # # print(variabila) #afiseaza tot
# # print(variabila[0]) #afiseaza elementul de pe pozitia 0


# masini =["Dacia", "Volvo", "Renault"]
# variabila=pd.Series(masini, index=["x", "y", "z"])
# print(variabila)


# masini =["Dacia", "Volvo", "Renault"]
# variabila=pd.Series(masini, index=["x", "y", "z"])
# print(variabila["z"]) # z preia valoare de pe index-ul 2
# print(variabila[0]) #afiseaza primul element

# masini = {"x": "Dacia", "y": "Volvo", "z": "Renault"}
# variabila = pd.Series(masini)
# print(variabila)



# masini = {"x": "Dacia", "y": "Volvo", "z": "Renault"} #vrem sa afiseze doar y si z
# variabila = pd.Series(masini, index=["y", "z"])
# print(variabila)




# dictionar_date = {
#     "masini": ["Dacia", "Volvo", "Renault"],
#     "culoare": ["rosu", "alb", "verde"]
# }


# variabila = pd.DataFrame(dictionar_date)
# print(variabila.loc[[0,1]]) #afiseaza randurile cu index-ul 0 si 1



# variabila = pd.DataFrame(dictionar_date, index = ["producator1", "producator 2", "producator3"]) #daca vrem sa dam indecsi
#  print(variabila)



# print(variabila.loc["producator1"])  #accesez anumite date de pe un anumit rand/coloana returneaza dacia si rosu



data = {
    "producator1": {
        "masini": "Dacia",
        "culoare": "rosu"
    },
    "producator2": {
        "masini": "Volvo",
        "culoare": "alb"
    },
    "producator3": {
        "masini":"Renault",
        "culoare": "verde"
    }
}

# variabila1 = pd.DataFrame(data)
# print(variabila1)



# #printare informatii dintr-un site
# url = "https://api.exchangerate-api.com/v4/latest/USD"
# variabila1 = pd.read_json(url)
# print(variabila1)



#salvare date dintr-un dataframe in excel
variabila1 =pd.DataFrame(data)
fisier =variabila1.to_csv("data.csv")

