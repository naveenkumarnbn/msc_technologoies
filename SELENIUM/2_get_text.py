from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome Browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org")
time.sleep(4)

## Get text based on xpath
download_text = driver.find_element(By.XPATH,'//*[@id="downloads"]/a').text

print('\n Text is :', download_text)

assert download_text == 'Downloads123', ' DOWNLOAD BUTTON TEXT IS NOT EXPECTED '

time.sleep(4)
driver.close()


