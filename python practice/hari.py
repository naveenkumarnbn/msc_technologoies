from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

driver.maximize_window()
time.sleep(4)

# name = driver.find_element(By.ID,"name")
# name.send_keys("RAMRAJ")
# time.sleep(5)

# email = driver.find_element(By.ID,"email")
# email.send_keys("ramraj123@gmail.com")
# time.sleep(4)

# phone = driver.find_element(By.ID,"phone")
# phone.send_keys("9986324110")
# time.sleep(3)

# add = driver.find_element(By.ID,"textarea")
# add.send_keys("#398,99 BUILDING NEAR GOLGONDA FORT HYDERABAD")
# time.sleep(5)

# male = driver.find_element(By.ID,"male")
# male.click()
# time.sleep(5)

# day = driver.find_element(By.ID,"friday")
# day.click()
# time.sleep(4)

# country = driver.find_element(By.ID,"country")
# country.click()
# time.sleep(4)

# green = driver.find_element(By.XPATH,"//*[@id='colors']/option[3]")
# green.click()
# time.sleep(5)

# date = driver.find_element(By.ID,"datepicker")
# date.send_keys("03/02/2024")
# time.sleep(4)

# wi = driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input")
# wi.click()
# time.sleep(5)

# wi.send_keys("https://www.amazon.in/")
# time.sleep(4)

# nn = driver.find_element(By.XPATH,"//*[@id='HTML4']/div[1]/button")
# nn.click()
# time.sleep(4)

actions = ActionChains(driver)
element  = driver.find_element(By.ID,"//*[@id='HTML10']/div[1]/button")
time.sleep(5)

actions.double_click(element).perform()




