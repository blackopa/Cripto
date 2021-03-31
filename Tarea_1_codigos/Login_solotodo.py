from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


num = input("Para un login Normal ingrese 0, Para intentar fuerza bruta ingrese 1")
if num==1 :
 	email = input("Ingrese el mail registrado: ")
 	while(1)
	passw = input("Ingrese la contraseña: ")
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
else:

	email = input("Ingrese el mail registrado: ")
	passw = input("Ingrese la contraseña: ")
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
	driver.implicitly_wait(5)
	driver.close()