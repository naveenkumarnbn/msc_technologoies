from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org")

## click on specified element
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="top"]/nav/ul/li[3]/a').click()
time.sleep(10)
driver.back()
time.sleep(10)
driver.forward()
time.sleep(7)
driver.close()

