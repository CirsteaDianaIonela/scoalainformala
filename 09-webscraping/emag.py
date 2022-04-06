from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options #ca sa nu se mai inchida pagina


browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.emag.ro/#opensearch')
get_element = browser.find_element(by = By.ID, value= 'searchboxTrigger')
get_element.send_keys('telefon') #vrem sa cautam in site dupa cuvantul telefon
get_element.submit()

def browser_function(): #functie ca sa nu mi se inchida pagina
    driver_path = "path/to/chromedriver"
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    chr_driver = webdriver.Chrome(driver_path, options=chr_options)
    chr_driver.get("https://target_website.com")

#vrem sa returnam un tabel cu produsele gasite pe pagina in functie de cuvantul cheie "telefon"
#dam search pe emag.ro dupa telefon, inspect, de indntificat div-ul de dinainte de toate containerele, copy xpath




