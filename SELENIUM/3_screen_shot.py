from selenium import webdriver
import time

d = webdriver.Chrome()
d.maximize_window()
d.get('https://www.python.org')

time.sleep(5)

# Take screenshot
d.save_screenshot(r'C:\INSTITUTE_COURSES\INST\2_ONLINE_CLASS\RRR.png')


d.close()