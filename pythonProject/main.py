from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("D://Airdriven//Dwnads//chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.airdriven.com/")
driver.maximize_window()
driver.close()
