from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()

driver.get("	https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(4)

driver.maximize_window()
time.sleep(4)

driver = driver.find_element(By.NAME,"radioButton2")
ime.sleep(2)

driver.click()
time.sleep(4)

driver = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/fieldset/input")
time.sleep(2)

driver.send_keys("SURYA")
time.sleep(4)

select1=Select(driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/fieldset/select"))
select1.select_by_value("dd2")
time.sleep(4)

#cb2=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/fieldset/label[2]/input")
#time.sleep(2)

#cb2.click()
#time.sleep(4)

#driver = driver.find_element(By.ID,"openwindow")
#time.sleep(2)

#driver.click()
#time.sleep(5)

#driver = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/fieldset/a")
#time.sleep(5)

#driver.click()
#time.sleep(4)

#driver= driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/fieldset/input[1]")
#time.sleep(2)

#driver.send_keys("ramcharan")
#time.sleep(4)

#driver.save_screenshot("ramraj.png")
#ime.sleep(4)

#driver.back()
#time.sleep(10)

#driver.forward()
#time.sleep(4)

#driver.refresh()
#time.sleep(5)

#driver.execute_script("window.scrollTo(0,600)")
#time.sleep(10)

#driver.execute_script("window.scrollTo(600,0)")
#time.sleep(10)

#driver.execute_script("window.open('https://www.amazon.in/')")
#time.sleep(4)

#driver.implicitly_wait(10)

#driver.execute_script("document.body.style.zoom='200%'")
#time.sleep(5)



