from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


email = input("Ingrese el mail registrado: ")
passw = input("Ingrese la contraseña: ")
newpass = input("Ingrese la contraseña nueva de largo minimo 8 y que no sea comun: ")
driver = webdriver.Firefox()
driver.get("https://www.solotodo.cl/")
driver.implicitly_wait(5) # 5 segundos de espera para cargar la pagina
login = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/nav/div/ul[2]/li[2]/a')
login.click()
login = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/nav/div/ul[2]/li[2]/div/a[1]')
login.click()
elem = driver.find_element_by_id("exampleInputEmail1")
elem.clear()
elem.send_keys(email)
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("password")
elem.clear()
elem.send_keys(passw)
elem.send_keys(Keys.RETURN)
	
login = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/nav/div/ul[2]/li[2]/a')
login.click()
login = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/nav/div/ul[2]/li[3]/div/a[1]')
login.click()
elem = driver.find_element_by_id("inputOldPassword")
elem.clear()
elem.send_keys(passw)
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("inputPassword1")
elem.clear()
elem.send_keys(newpass)
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("inputPassword2")
elem.clear()
elem.send_keys(newpass)
elem.send_keys(Keys.RETURN)



driver.implicitly_wait(5)
driver.close()