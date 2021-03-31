from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

email = input("Ingrese un mail: ")
passw = input("Ingrese un pass de 8 caracteres minimo que no sea comun: ")
driver = webdriver.Firefox()
driver.get("https://www.solotodo.cl/")
driver.implicitly_wait(5) # 5 segundos de espera para cargar la pagina

registro = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/nav/div/ul[2]/li[2]/a')
registro.click()
registro = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/nav/div/ul[2]/li[2]/div/a[2]')
registro.click()

elem = driver.find_element_by_id("inputEmail")
elem.clear()
elem.send_keys(email)
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("inputPassword1")
elem.clear()
elem.send_keys(passw)
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("inputPassword2")
elem.clear()
elem.send_keys(passw)
elem.send_keys(Keys.RETURN)

driver.implicitly_wait(5)
driver.close()