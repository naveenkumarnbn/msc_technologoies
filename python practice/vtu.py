from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(3)

driver.maximize_window()
time.sleep(2)

mick = driver.find_element(By.XPATH,"//*[@class='goxjub']")
mick.click()
time.sleep(3)

