# import datetime
# import unittest
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# class LocationTest(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome(ChromeDriverManager().install()) #seteaza partea de autentificare si chormedrive
#         self.driver.get('http://127.0.0.1:8000/') #link-ul pe care il accesam prima data,link ul aplicatiei noastre
#         username = self.driver.find_element(by=By.CLASS_NAME, value='username')
#         username.send_keys('lenovo')
#         password = self.driver.find_element(by=By.CLASS_NAME, value='password')
#         password.send_keys('Feelingalive1.')
#         submit = self.driver.find_element(by=By.CLASS_NAME, value='btn-info')
#         submit.submit()
#         self.logs = open('logs.txt', mode='a')
#
#     def test_form(self):
#         if value := 'table' in self.driver.page_source:
#             self.logs.write(f"{value}, {datetime.datetime.now()}")
#         assert value

    # def test_add_location(self):


