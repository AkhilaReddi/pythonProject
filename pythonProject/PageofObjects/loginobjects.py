from concurrent.futures import thread

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Testurl = "https://dev.d26zcxki5b6f7x.amplifyapp.com/loginpage"
# admin Texting URL
WusernameT="Abdullll"
#Wrong User name
WpasswordT="password"
usernamex: str = "/html/body/div/div[3]/container/div/div/div[2]/input"
# Xpath for user name in login screen
passwordx: str = "/html/body/div/div[3]/container/div/div/div[4]/input"
# Xpath for password in login screen
loginbutx = "/html/body/div/div[3]/container/div/div/div[6]/button"
# Xpath for Login button
usert = "abdulnovone"
passwordt = "P@$$W0rd"
# Login username & Password
expectedURL = "https://dev.d26zcxki5b6f7x.amplifyapp.com"
s = Service("C://Users//home//Desktop//pythonProject//Airdriven//chromedriver.exe")
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
class Testloginpage:
def test_validuser():
     driver = webdriver.Chrome(service=s)
     driver.maximize_window()
     driver.get(Testurl)
     driver.find_element(By.XPATH, (usernamex)).send_keys(usert)
     driver.find_element(By.XPATH, (passwordx)).send_keys(passwordt)
     driver.find_element(By.XPATH, (loginbutx)).click()
     ActualURL = driver.current_url
     if expectedURL == ActualURL:
         print("Fail")
     else:
        print("pass")


 def test_invalid_user():
     driver = webdriver.Chrome(service=s)
     driver.maximize_window()
     driver.get(Testurl)
     driver.find_element(By.XPATH, (usernamex)).send_keys(WusernameT)
     driver.find_element(By.XPATH, (passwordx)).send_keys(WpasswordT)
     driver.find_element(By.XPATH, (loginbutx)).click()
     ActualURL = driver.current_url
     if expectedURL == ActualURL:
         print("Fail")
     else:
         print("pass")

