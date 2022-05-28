from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
caps = options.to_capabilities()

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
table = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]')
table_text = table.text
lista = table_text.split('\n')
header_len = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody/tr[1]')
header = header_len.text.split('\n')
print(f'header total:', header) # returneaza tot capul de tabel
# print(lista) #returneaza tot tabelul
nr_crt_len = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody/tr[1]/td[1]')
nr_crt = nr_crt_len.text.split('\n')
judet_len = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody/tr[1]/td[2]')
judet = judet_len.text.split('\n')
cazuri_len = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody/tr[1]/td[3]')
cazuri_total = cazuri_len.text.split('\n')
# print(nr_crt, judet, cazuri_total) #returneaza ['Nr. crt.'] ['Județ'] ['Număr de cazuri confirmate(total)']
a = nr_crt[0]
b = judet[0]
c = cazuri_total[0]
dictionar_3 = {a:[],
               b:[],
               c:[]}
header2=[a,b,c]
print(f'header 2:',header2)

dictionar = {i: [] for i in header2}  #pentru fiecare element din header avem o lista
# print(dictionar)
for j in range(0, len(header2)):  #parcurgem fiecare rand din tabel pana la ultmul element
    for i in range(len(header2) + int(j), len(lista), len(header2)):
        # print(lista[i])
        dictionar[header2[int(j)]].append(lista[i])
print(dictionar)
# for j in range(0, len(dictionar_3)):  #parcurgem fiecare rand din tabel pana la ultmul element
#     for i in range(len(dictionar_3) + int(j), len(lista), len(dictionar_3)):
#         # print(lista[i])
#         dictionar_3[dictionar_3[int(j)]].append(lista[i])
#
# print(dictionar_3)

# dictionar = {i: [] for i in header}  #pentru fiecare element din header avem o lista
# # print(dictionar)
# for j in range(0, len(header)):  #parcurgem fiecare rand din tabel pana la ultmul element
#     for i in range(len(header) + int(j), len(lista), len(header)):
#         # print(lista[i])
#         dictionar[header[int(j)]].append(lista[i])

# df = pd.DataFrame()
# df.to_csv('Covidx.csv')
# print(dictionar)
# df = pd.DataFrame(dictionar)
# df.to_csv('Covidxxx.csv')
