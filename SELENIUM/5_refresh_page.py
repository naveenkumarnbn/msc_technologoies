from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org")


time.sleep(5)
driver.refresh()
time.sleep(10)
driver.refresh()
time.sleep(5)
driver.close()


