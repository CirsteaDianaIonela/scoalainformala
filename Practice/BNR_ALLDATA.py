from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
caps = options.to_capabilities()

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.bnr.ro/files/xml/nbrfxrates2021.htm')
# print(browser)

table = browser.find_element(by = By.XPATH, value= '//*[@id="Data_table"]')
table_text = table.text
# print(table_text) #toate datele inclusiv capul de tabel, unele sub altele, incepe cu elementul de pe prima coloana si itereaza pe rand
lista = table_text.split('\n')
# print(lista) - >reprezinta absolut toate elementele care se regasesc in tabel
header_len = browser.find_element(by = By.XPATH, value= '//*[@id="Data_table"]/table/thead/tr') #vreau sa preiau capul de tabel, merg la tr-ul aferent id-ului pe care l-am folosit
# print(header_len)
header = header_len.text.split('\n')
print(header) #o lista cu tot capul de tabel, adica data + toate monedele
# dictionar = {i: [] for i in header} #pentru fiecare element din header (monedele) se va crea o lista, cheile dictionarului sunt monedele + data
# for j in range(0, len(header)): #pentru fiecare element intre 0 si nr de elemente ale capului de tabel -1
#     for i in range(len(header) + int(j), len(lista), len(header)): # pentru fiecare cheie incepand cu elementul 33-> parcurge tot tabelul excluzand capul de tabel, apoi pana la finalul tabelului (len lista), cu pasul din 33 in 33
#         dictionar[header[int(j)]].append(lista[i])
# print(dictionar)
# # print(len(header))
# # print(lista)
# df = pd.DataFrame(dictionar)
# df.to_csv('BNR ALL DATA.csv')
