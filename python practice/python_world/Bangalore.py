from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)

driver.maximize_window()
time.sleep(3)



rd1 = driver.find_element(By.XPATH,("//*[@value='radio1']"))
rd1.click()
time.sleep(3)

rd3 = driver.find_element(By.XPATH,("//*[@value='radio3']"))
rd3.click()
time.sleep(3)

text = driver.find_element(By.XPATH,"//*[@id='autocomplete']")
text.send_keys("I LOVE MY INDIA")
time.sleep(2)

select1= Select(driver.find_element(By.XPATH,("//*[@name='dropdown-class-example']")))
select1.select_by_value("option2")
time.sleep(3)

cb2 =driver.find_element(By.XPATH,("//*[@id='checkBoxOption2']"))
cb2.click()
time.sleep(3)

swe = driver.find_element(By.XPATH,("//*[@id='openwindow']"))
swe.click()
time.sleep(3)

ste = driver.find_element(By.XPATH,("//*[@class='btn-style class1 class2']"))
ste.click()
time.sleep(3)

eyn = driver.find_element(By.XPATH,("//*[@placeholder='Enter Your Name']"))
eyn.send_keys("RL jalappa")
time.sleep(2)

rows =len(driver.find_elements(By.XPATH,("/html/body/div[3]/div[1]/fieldset")))

columns= len(driver.find_elements(By.XPATH,(" /html/body/div[3]/div[1]/fieldset")))
print(rows)
print(columns)
time.sleep(6)








