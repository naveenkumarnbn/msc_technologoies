from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()
time.sleep(5)

user = driver.find_element(By.ID,"name")
user.send_keys("pavan")
time.sleep(4)

mail = driver.find_element(By.ID,"email")
mail.send_keys("rajeshbabu123@gmail.com")
time.sleep(5)

ph = driver.find_element(By.ID,"phone")
ph.send_keys("7338495510")
time.sleep(5)

add = driver.find_element(By.ID,"textarea")
add.send_keys("#19 MARATHAHALLI BANGLORE EAST")
time.sleep(5)

male = driver.find_element(By.NAME,"gender")
male.click()
time.sleep(5)

wed = driver.find_element(By.ID,"wednesday")
wed.click()
time.sleep(5)

coun = driver.find_element(By.ID,"country")
coun.click()
time.sleep(5)

green = driver.find_element(By.XPATH,"//*[@id='colors']/option[2]")
green.click()
time.sleep(5)

date = driver.find_element(By.ID,"datepicker")
date.send_keys("19/01/2024")
time.sleep(5)

tab = driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input")
tab.send_keys("https://www.google.com/")
time.sleep(5)

win = driver.find_element(By.XPATH,"//*[@id='HTML4']/div[1]/button")
win.click()
time.sleep(5)

actions = ActionChains(driver)
element = driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
time.sleep(5)

actions.double_click(element).perform()


