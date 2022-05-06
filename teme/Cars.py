import pandas as pd
from os import path, mkdir
import shutil
import json

output_folder = "output_data"


def cars():

    masini = {"id": [1, 2, 3], "brand": ["Mazda", "Skoda", "Mazda"], "model": ["A", "B", "C"],
              "hp": [90, 170, 200], "price": [900, 1700, 20000]}

    tabel_masini = pd.DataFrame(masini)
    fisier = tabel_masini.to_csv("input.csv")  #il trimit in csv
    print(tabel_masini)


def create_folder():  #creez folderul
    if path.exists(f'./{output_folder}/'):
        shutil.rmtree(f'./{output_folder}/')

    mkdir(f'./{output_folder}')


def about_cars():
    cars()
    dataframe = pd.read_csv('input.csv')
    dataframe = pd.DataFrame(dataframe.values, index=dataframe.index, columns=dataframe.dropna(axis=1, how='all').columns)
    dataframe.hp = pd.to_numeric(dataframe.hp)
    create_folder()
    slow_car = dataframe[dataframe.hp < 120]
    slow_car.to_json(f'{output_folder}/slow_cars.json')
    fast_car = dataframe[(dataframe.hp >= 120) & (dataframe.hp < 180)]
    fast_car.to_json(f'{output_folder}/fast_cars.json')
    sport_car = dataframe[dataframe.hp >= 120]
    sport_car.to_json(f'{output_folder}/sport_cars.json')
    cheap_car = dataframe[dataframe.price < 1000]
    cheap_car.to_json(f'{output_folder}/cheap_cars.json')
    medium_car = dataframe[(dataframe.price >= 1000) & (dataframe.hp < 5000)]
    medium_car.to_json(f'{output_folder}/medium_cars.json')
    expensive_car = dataframe[(dataframe.price >= 5000)]
    expensive_car.to_json(f'{output_folder}/expensive_cars.json')


def cars_by_brand():
    cars()
    dataframe = pd.read_csv('input.csv')
    dataframe = pd.DataFrame(dataframe.values, index=dataframe.index, columns=dataframe.dropna(axis=1, how='all').columns)
    mazda = dataframe.sort_values(by='brand')
    filters = mazda['brand'].str.contains('Mazda')
    mazda = mazda.loc[filters]
    mazda.to_json(f'{output_folder}/Mazda.json')
    skoda = dataframe.sort_values(by='brand')
    filters = skoda['brand'].str.contains('Skoda')
    skoda = skoda.loc[filters]
    skoda.to_json(f'{output_folder}/Skoda.json')


cars()
create_folder()
about_cars()
cars_by_brand()
