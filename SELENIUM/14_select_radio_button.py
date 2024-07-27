from selenium import webdriver
from selenium.webdriver.common.by import By
import time

###  IF driver in current path ###
driver = webdriver.Chrome()
driver.maximize_window()

# Open a URL
driver.get(r'C:\INSTITUTE_COURSES\INST\2_ONLINE_CLASS\3_SELENIUM/DROP_DOWN.html')
time.sleep(5)


# Select radio button
driver.find_element(By.ID, 'age2').click()

time.sleep(10)
driver.close()