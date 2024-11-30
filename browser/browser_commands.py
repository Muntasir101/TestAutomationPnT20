import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://muntasir101.github.io/Conference-Room-Booking/")
time.sleep(10)

website_title = driver.title
print(website_title)

website_url = driver.current_url
print(website_url)

driver.quit()