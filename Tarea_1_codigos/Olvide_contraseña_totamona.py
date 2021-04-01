from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



email = input("Ingrese un mail: ")

driver = webdriver.Firefox()
driver.get("https://totamona.com/es/")
login = driver.find_element_by_xpath('/html/body/main/div[7]/div[1]/div[4]/div[2]/div/a')
login.click()
login = driver.find_element_by_xpath('/html/body/main/section/div/section/section/section/section/form/section/div[2]/div/a')
login.click()
elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys(email)
elem.send_keys(Keys.RETURN)

login = driver.find_element_by_xpath('/html/body/main/section/div/section/section/section/div/form/section/div/div[2]/button')
login.click()

driver.close()