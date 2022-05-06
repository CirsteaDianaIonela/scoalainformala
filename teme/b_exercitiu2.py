from a_exercitiu2 import dataset
import pandas as pd
import csv


def get_year_data(set_date, an):
    result = {an: []}
    for key, value in set_date.items():
        for item in set_date[key]:
            if item['year'] == str(an):
                res = {key: item['coverage'] for key, value in set_date.items()}
                result[an].append(res)
    return result


df = pd.DataFrame(get_year_data(dataset, '2019'))
df.to_csv('c_exercitiu2.csv', index=False, mode='a', )


def get_country_data(set_date, tara):
    result = {tara: []}
    a = [d.get('year') for country, sublists in set_date.items() if country == tara for d in sublists]
    b = [e.get('coverage') for country, sublists in set_date.items() if country == tara for e in sublists]
    c = list(zip(a, b))
    result[tara].append(c)
    return result


df1 = pd.DataFrame(get_country_data(dataset, 'Romania'))
df1.to_csv('c_exercitiu2.csv', index=False, mode='a', )


def perform_average(country_data):
    country_data = [e.get('coverage') for country, sublists in dataset.items() if country == country_data for e in
                    sublists]
    return str(round(sum(country_data) / len(country_data), 2))


print(type(perform_average(country_data='Bulgaria')))
