# What is Selenium
    Selenium is a free (open source) automated testing tool for web applications across different browsers and platforms. 

    Selenium has four components.
        1. Selenium Integrated Development Environment (IDE)
        2. Selenium Remote Control (RC)
        3. WebDriver
        4. Selenium Grid

# How to install selenium
    python -m pip install selenium

# To Know selenium VERSION
import selenium
print(' \n SELENIUM VERSION IS :: ', selenium.__version__)

# What are web drivers ?
    Selenium provides few drivers that help you to perform actions on browser. 

    Below are the drvers: 
        1. ChromeDriver   --> for Chrome
        2. GeckoDriver    --> for Firefox
        3. IEDriverServer --> for Internet InternetExplorer

# How to select required Chrome driver
    We have to download ChromeDriver based on Chrome Version

# How to find element(Address) in Webpage
    Using Developer tools

# Ways to open Developer tools ?
    1. Right click on webpage --> inspect
    2. By clicking F12 key

## If Chrome driver in different path
driver = webdriver.Chrome(r'C:\Users\TEST\chromedriver.exe')


