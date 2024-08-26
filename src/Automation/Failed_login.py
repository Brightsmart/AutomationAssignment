import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(4)

Website = driver.get("")
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "passwo")
login = driver.find_element(By.ID, "loginButton")
errorMessage = driver.find_element(By.ID, "errorMessage")
username.send_keys("")
password.send_keys("")
login.click()
assert errorMessage.text == 'div'