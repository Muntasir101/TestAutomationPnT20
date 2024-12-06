from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()

urls = [
    "http://google.com",
    "http://www.apple.com"
]

driver.get(urls[0])

# open a new tab
driver.execute_script("window.open('');")

# switch to  new tab
driver.switch_to.window(driver.window_handles[-1])

driver.get("https://apple.com")

# back to parent tab
driver.switch_to.window(driver.window_handles[0])