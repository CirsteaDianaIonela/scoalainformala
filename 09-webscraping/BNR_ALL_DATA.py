# import requests
# from bs4 import BeautifulSoup
#
# r = requests.get('https://www.bnr.ro/files/xml/nbrfxrates2021.htm') #este o variabila in care incarcam cu ajutorul librariei datele din link
# print(r.text)
# nu merge cu beautiful soup si vom folosi SELENIUM
# DIFERENTE intre beautiful soup si selenium ->: sunt 2 tipuri de incarcare: a paginii si a datelor
# -> beautifoul soup: mai folosit cand pagina web este statica, data trecuta despre link: inspect, datele sunt incarcate direct in pagina, in codul de html, ne dam seama vazand la network, sunt incarcate sincron: se incarca si datele si pagina in acelasi timp,
# -> selenium: mai folosit pentru partea de testare: data asta despre link: inspect, datele sunt incarcate din fiser xls cu ajutorul xml-ului, aici sunt mult mai multe date, datele au un timp mai lung de incarcare, timp mai mare de incarcare a datelor, incarcare asincron, datele sunt incarcate dupa incarcarea paginii si depind de un fisier separat xlm, pagina se incarca mai repede si datele mai greu putin, folosit pentru testari: ce se intampla daca dai un click


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
caps = options.to_capabilities()

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")
table = browser.find_element(by=By.XPATH, value='//*[@id="Data_table"]')
table_text = table.text
lista = table_text.split('\n')
# print(lista)
header_len = browser.find_element(by = By.XPATH, value = '//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n') #capul de tabel
print(header)
dictionar = {i: [] for i in header} #pentru fiecare element din header avem o lista
print(dictionar)
for j in range(0, len(header)):#parcurgem fiecare rand din tabel pana la ultmul element
    for i in range(len(header) + int(j), len(lista), len(header)): #ultimul len este pasul, de la prima celula la ultima din 33 in 33
        print(lista[i])
        dictionar[header[int(j)]].append(lista[i])
print(dictionar)
df = pd.DataFrame(dictionar)
df.to_csv('BRN_ALL_DATA.xls')
# print(table_text) #preia cursurile valutare de la prima coloana pana la ultima inclusiv, si le pune unele sub altele
browser.close()



