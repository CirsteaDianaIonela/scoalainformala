# import json
#
# masini = {"ID":"1", "Brand":"Renault","Model":"Clio","CP":"75","Pret":"5000"}
# y = json.dumps(masini)
# print(json.dumps(y), type(y))

# import json
# person_dict = {"name": "Bob", "languages": ("English", "Fench"), "married": True, "age": 32 }
# with open('person.json', 'w') as json_file: json.dump(person_dict, json_file)


import json
masini = {"ID":"1", "Brand":"Renault","Model":"Clio","CP":"75","Pret":"5000"}
with open('fisier1.json', 'w') as json_file: json.dump(masini, json_file)