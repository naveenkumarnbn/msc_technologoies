from selenium import webdriver
import time
from selenium.webdriver.common.by import By

###  IF driver in current path ###
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r'C:\INSTITUTE_COURSES\INST\2_ONLINE_CLASS\3_SELENIUM/DROP_DOWN.html')
time.sleep(5)


# Select Check box
obj = driver.find_element(By.ID, 'vehicle2')
obj.click()
time.sleep(5)

driver.find_element(By.ID, 'vehicle3').click()
time.sleep(5)

driver.close()



