from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

First_N =input("Ingrese un nombre: ")
Last_N =input("Ingrese un apellido: ")
email = input("Ingrese un mail: ")
passw = input("Ingrese una password: ")
driver = webdriver.Firefox()
driver.get("https://totamona.com/es/")
driver.implicitly_wait(5) # 5 segundos de espera para cargar la pagina

registro = driver.find_element_by_xpath('/html/body/main/div[7]/div[1]/div[4]/div[2]/div/a')
registro.click()
registro = driver.find_element_by_xpath('/html/body/main/section/div/section/section/section/section/div/div[2]/a/span')
registro.click()

registro = driver.find_element_by_xpath('/html/body/main/footer/div[2]/div[2]/div/div[3]/div/div/button')
registro.click()


elem = driver.find_element_by_name("firstname")
elem.clear()
elem.send_keys(First_N)
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_name("lastname")
elem.clear()
elem.send_keys(Last_N)
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys(email)
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys(passw)
elem.send_keys(Keys.RETURN)

driver.execute_script("window.scrollBy(0, 100)","")
registro = driver.find_element_by_xpath('/html/body/main/section/div/section/section/section/div/div[1]/div/div/form/footer/div[2]/div/label/span[1]')
registro.click()

registro = driver.find_element_by_xpath('/html/body/main/section/div/section/section/section/div/div[1]/div/div/form/footer/button')
registro.click()

driver.implicitly_wait(5)
driver.close()