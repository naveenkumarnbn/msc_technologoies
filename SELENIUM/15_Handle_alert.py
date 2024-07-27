from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

d = webdriver.Chrome()
d.maximize_window()
d.get(r'C:\INSTITUTE_COURSES\INST\2_ONLINE_CLASS\3_SELENIUM/ALERT.html')
sleep(5)

d.find_element(By.XPATH, '/html/body/button').click()

alert = d.switch_to.alert
sleep(5)

## To accept alert
#alert.accept()

## To dismiss alert
#alert.dismiss()

#  To get alert message
print(' \n\n ALERT TEXT :: ' , alert.text)
assert alert.text == 'HI SRIRAM', ' Alert Text is not expected '


sleep(10)
d.close()

