# Using execute_script we can run java script
from selenium import webdriver
import time

# Open a Chrome Browser
d = webdriver.Chrome()
#d.maximize_window()
d.get("https://www.python.org/")
time.sleep(10)

# To Scroll down page
#d.execute_script("window.scrollTo(0, 800)")
#time.sleep(10)


# To Scroll up page
#d.execute_script("window.scrollTo(800, 0)")("window.scrollTo(800, 0)")
#time.sleep(5)

# To Scroll down page bottom
d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)

d.close()

