from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
pyautogui.PAUSE = 3


email = input("Ingrese un mail: ")
passw = input("Ingrese una password: ")
newpass = input("Ingrese Nueva password: ")
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

registro = driver.find_element_by_xpath('/html/body/main/footer/div[2]/div[2]/div/div[3]/div/div/button')
registro.click()#esto elimina un boton que tapa otro boton mas adelante xD


pyautogui.moveTo(x=1090,y=540,duration=2)
pyautogui.click(x=1090,y=540)


elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys(passw)
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_name("new_password")
elem.clear()
elem.send_keys(newpass)
elem.send_keys(Keys.RETURN)

login = driver.find_element_by_xpath('/html/body/main/section/div/section/section/div/div/form/div[1]/div[1]/div/label/span[1]')
login.click()
login = driver.find_element_by_xpath('/html/body/main/section/div/section/section/div/div/form/div[1]/div[3]/div/label/span[1]')
login.click()
pyautogui.moveTo(x=1090,y=540,duration=2)#para agregar tiempo
login = driver.find_element_by_xpath('/html/body/main/section/div/section/section/div/div/form/footer/button')
login.click()
driver.close()