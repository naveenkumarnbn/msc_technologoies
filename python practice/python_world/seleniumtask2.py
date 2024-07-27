from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initiating driver
driver = webdriver.Chrome()

# Launching url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/fieldset/label[2]/input").click()
time.sleep(4)

driver.find_element(By.ID, ("autocomplete")).send_keys('kiran')
time.sleep(3)

driver.find_element(By.ID, ("checkBoxOption2")).click()
time.sleep(4)

abc = Select(driver.find_element(By.ID, "dropdown-class-example"))
abc.select_by_visible_text("Option2")
time.sleep(3)

driver.find_element(By.ID, ("openwindow")).click()
title = driver.title
print("abd:", title)
time.sleep(4)
