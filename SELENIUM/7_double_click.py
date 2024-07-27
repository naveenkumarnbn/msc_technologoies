from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(r"C:\INSTITUTE_COURSES\INST\2_ONLINE_CLASS\3_SELENIUM\DOUBLE_CLICK.html")

## Move cursor on specified element and click
time.sleep(5)

actions = ActionChains(driver)
element = driver.find_element(By.XPATH,'/html/body/div/button')

actions.move_to_element(element)
time.sleep(3)

actions.double_click()
time.sleep(3)
actions.perform()

time.sleep(10)
driver.close()

