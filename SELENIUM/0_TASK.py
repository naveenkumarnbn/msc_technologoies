## Please complete below steps one by one

1. Install Selenium
    python -m pip install selenium

2. Creare seperate folder(SELENIUM_SCRIPTS) to keep your selenium scripts

3. Find your Chrome Browser Version
    108

4. download required "chrome driver" based on your chrome browser version and place in your SELENIUM_SCRIPS folder
    # Link for download chrome driver : https://chromedriver.chromium.org/downloads

    Python Selenium script --> Chrome Driver --> Chrome Browser

5. create a login_page.py file inside SELENIUM_SCRIPS diractory

6. write code for below actions inside login_page.py file 
    1. import webdriver and By class from selenium module
    2. create a driver for Chrome brower
    3. Maximize browser window
    4. Enter login page URL :: (https://accounts.lambdatest.com/login)
    5. Find element(ADDRESS) for uname text box
    6. Enter uname
    7. Find element for password text box
    8. Enter password
    9. Find element for login button
   10. Click on login button
   11. Colse browser

