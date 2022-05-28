import matplotlib.pyplot as plt
import pandas as pd
# print(pd.__version__)
# a = {'x': 1, "y": 7, "z":2}
# variabila = pd.Series(a, index = a.keys()) #returneaza datele dictionarului unui tabel
# variabila = pd.Series(a, index = ["x", "y"]) #returneaza datele dictionarului unui tabel pentru cheile pe care le mentionam
# print(variabila)
#
# data = {
#     "key1": [0,1,2],
#     "key2": [3,4,5],
#
# }

#data frame pt ca sunt mai multe randuri, cheile sunt header, iar valorile sunt coloanele, returneaza un tabel

# variabila = pd.DataFrame(data, index = ['linie1', 'linie2', 'linie3']) #aceste linii inlocuiesc indecsii
# # print(variabila["key2"]) #valorile de pe o cheie, key2, o coloana
# print(variabila.loc['linie2'])

# df = pd.read_csv('EXEMPLU.csv')
# print(df)
# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }
# cum citesc aceste date sa le pun in dataframe
# df = pd.DataFrame(data)
# print(df)



# df1 = None
#
# for x in df.index:
#     print(df.loc[x,'AL']) #numara cate inregistrari sunt
#     if df.loc[x, 'AL'] == ':':
#         print('dff')
#         df.drop(x, inplace= True)
#
# print(df)

#cum sa obtinem datele dupa stergere:

# df1 =  df.to_csv("test1,csv") trimitem datele in csv
# print(df.corr()) #matricea de corelatii intre elemente
# print(df.describe())statistici descriptive despre datele preluate din csv
# print(df.mean()) #media coloanelor
# import matplotlib.plot as plt #importam ca sa facem grafic, este o librarie
# df.plot(kind = 'scatter', x = 'AT', y = 'BE') #pt a face grafic
# plt.show()

#histograma:

# df['AT'].plot(kind = 'hist')
# plt.show() #ca sa afisez histograma


#daca avem 100 de linii si vrem sa le vedem pe primele 5
# print(df.head(5))

#daca avem 100 de linii si vrem sa le vedem pe primele 3
# print(df.tail(3))

#daca vrem sa pastram doar randurile fara NaN
# new_df = df.dropna(inplace = True)
# print(new_df)

#daca vrem sa inlocuim NaN sa treaca 0:
# print(df.fillna(0, inplace = True)) #punem in place ca sa ramana datele modificate

#vrem sa inlocuim acel 84 CU 45
# df.loc[7, 'AL'] = 45 #index 7 si AL
# print(df)

#curatam punctele :
# df.replace(':', 0, inplace = True) #trebuie realocat
# df.replace(':', 0, inplace = True)
# print(df.transpose()) #intoarce datele invers
# df.to_csv('test1.csv')

