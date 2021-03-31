from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


email = input("Ingrese el mail registrado: ")
driver = webdriver.Firefox()
driver.get("https://www.solotodo.cl/")
driver.implicitly_wait(5) # 5 segundos de espera para cargar la pagina
login = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/nav/div/ul[2]/li[2]/a')
login.click()
login = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/nav/div/ul[2]/li[2]/div/a[1]')
login.click()
olvidar_pass = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/form/div[3]/a')
olvidar_pass.click()
elem = driver.find_element_by_id("exampleInputEmail1")
elem.clear()
elem.send_keys(email)
elem.send_keys(Keys.RETURN)
enviar = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/form/input')
enviar.click()

driver.implicitly_wait(5)
driver.close()
