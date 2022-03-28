#click dr inspect pe o pagina web si vad codul in elements
# https://www.bnr.ro/Cursul-de-schimb--7372.aspx
#BeautifulSoup este o clasa
from bs4 import BeautifulSoup
import requests
import pandas as pd

r = requests.get("https://www.bnr.ro/Cursul-de-schimb--7372.aspx")    #o sa preluam pe baza unui URL informatiile de pe pagina

print(r)  #rezultat -> Response [200], tot ce incepe cu 2 este de bine, 200 este un status inseamna ca e incarcat cu succes, daca aveam 404 page not found, 500 eroare de server, 201 succes cu redirect
print(r.text) #retureaza sursa HTML a paginii, tot ce contine pagina respectiva
link = BeautifulSoup(r.text, "html.parser") #mutam aceasta pagina in beautifulsoup ca sa putem sa lucram pe acele date
#link este un obiect al clasei BeautifulSoup, in paranteza punem r.text care este link ul site ului
print(link)
#trebuie sa accesam tabelul de pe pagina noastra de la bnr, mergem in pagina noastra, click pe tabel, inspect, cautam din div ul de deasupra tabelului elementul de care ne putem folosi: class"contentDiv"
title = link.find_all('div', attrs = {'class': "contentDiv"}) #acceseaza div-ul de deasupra tebelului
header = []
dataset = []
# print(title) #returneaza o lista de elemente
for i in title: #iteram prin aceasta lista
    # print(i)
    for tr_index in i.find_all_next('table'): #din acest div vrem sa luam tabelul, doar un div
        # print(tr_index) #afiseaza doar tabelul
        for td_index in tr_index.find_all ('tr'):##intra pe coloana si itereaza pe rand element cu element, vrem sa luam pe baza tabelului tr, sa ne preia randurile din tabel
            # print(tr_index)
            td_list = [] #lista temporata pentru intrarea pe fiecare rand
            if td_index.find_all('th'): # trebuie sa preluam th = tabel header, mergem mai sus si facem o lista cu headere
                header = [th_index.get_text() for th_index in td_index.find_all('th')] #preluam informatia din th
            for index, td_value in enumerate(td_index.find_all('td')):
                print(index, td_value) # in stanga indexul, in dreapta td-ul
                if index == 0: #preluam data in mod particular
                    td_list.append(td_value.get_text())
                else:
                    td_list.append(float(td_value.get_text().replace(',','.'))) #retueneaza toate liniile
            dataset.append(td_list) #returneaza o lista cu prima coloana ce are data
# print(header) #vedem lista doar cu headere, capul de tabel
print(dataset)
df = pd.DataFrame(dataset, columns=header) #punem dataset in excel
print(df)
df.to_csv("CursBNR.xls", header = header)