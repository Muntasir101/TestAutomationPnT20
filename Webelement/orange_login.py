import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.implicitly_wait(20)

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login_btn = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

username.send_keys("Admin")
password.send_keys('admin123')
login_btn.click()