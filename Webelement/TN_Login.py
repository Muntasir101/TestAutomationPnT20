import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

driver.implicitly_wait(20)

Email = driver.find_element(By.NAME, "email")
Password = driver.find_element(By.NAME, "password")
login_btn = driver.find_element(By.CSS_SELECTOR, "[action] .btn-primary")

Email.send_keys("Admin")
Password.send_keys('admin123')
login_btn.click()

expected_error_message_text = "Warning: No match for E-Mail Address and/or Password."

error_message_element = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
actual_error_message_text = error_message_element.text

if actual_error_message_text == expected_error_message_text:
    print("Error Message Verified.", actual_error_message_text)
else:
    print("Error Message Mismatched.")



