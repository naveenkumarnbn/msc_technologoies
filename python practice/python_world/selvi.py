from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
time.sleep(2)

driver. maximize_window()
time.sleep(2)

user_name = driver.find_element(By.XPATH,("//*[@name='username']"))
user_name.send_keys("naveen")
time.sleep(3)

pwd = driver.find_element(By.XPATH,("//*[@name='password']"))
pwd.send_keys("manasa@123")
time.sleep(3)

text = driver.find_element(By.XPATH,("//*[@name='comments']"))
text.clear()
text.send_keys("i love my india")
time.sleep(3)

file_upload = driver.find_element(By.XPATH,("//*[@name='filename']"))
file_upload.send_keys(r"C:\Users\Naveenkumar bn\OneDrive\Desktop\new scan")
time.sleep(3)

cb1 = driver.find_element(By.XPATH,("//*[@value='cb1']"))
cb1.click()
time.sleep(3)

cb3 = driver.find_element(By.XPATH,("//*[@value='cb3']"))
cb3.click()
time.sleep(2)

rd1 = driver.find_element(By.XPATH,("//*[@value='rd1']"))
rd1.click()
time.sleep(2)

rd2 = driver.find_element(By.XPATH,("//*[@value='rd2']"))
rd2.click()
time.sleep(2)

select1 =Select(driver.find_element(By.XPATH,("//*[@name='multipleselect[]']")))
select1.select_by_value("ms1")
time.sleep(2)

select2 = Select(driver.find_element(By.XPATH,("//*[@name='dropdown']")))
select2.select_by_value("dd4")
time.sleep(3)

cancel = driver.find_element(By.XPATH,("//*[@name='submitbutton']"))
cancel.click()
time.sleep(3)

submit = driver.find_element(By.XPATH,("//*[@value='submit']"))
submit.click()
time.sleep(3)

driver.back()
time.sleep(3)

driver.forward()
time.sleep(4)

driver.execute_script("window.scrollTo(0,800)")
time.sleep(4)

driver.execute_script("window.scrollTo(800,0)")
time.sleep(4)

driver.execute_script("window.open('https://www.facebook.com/')")
time.sleep(3)

driver.save_screenshot("naveen.png")
time.sleep(4)

driver.close()
time.sleep(3)

driver.quit()
time.sleep(3)

