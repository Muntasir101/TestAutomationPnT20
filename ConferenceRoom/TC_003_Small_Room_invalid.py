from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://muntasir101.github.io/Conference-Room-Booking/")
driver.implicitly_wait(20)

Select_room = driver.find_element(By.CSS_SELECTOR, "select#room")
room_type = Select(Select_room)
room_type.select_by_value("Small Room")

Start_time = driver.find_element(By.CSS_SELECTOR, "input#start-time")
Start_time.click()
Start_time.send_keys("12")
Start_time.send_keys("21")
Start_time.send_keys("2024")
Start_time.send_keys("12")
Start_time.send_keys("00")

End_time = driver.find_element(By.CSS_SELECTOR, "input#end-time")
End_time.click()
End_time.send_keys("12")
End_time.send_keys("15")
End_time.send_keys("2024")
End_time.send_keys("01")
End_time.send_keys("00")
End_time.send_keys(Keys.ARROW_DOWN)

Book_room_button = driver.find_element(By.CSS_SELECTOR, "#booking-form button")
Book_room_button.click()

Expected_error_message = "Please fill out all fields correctly."

Actual_error_message = driver.switch_to.alert.text
driver.switch_to.alert.accept()


if Expected_error_message == Actual_error_message:
    print("Test Case Passed.")
else:
    print("Test Case Failed.")
    print("Expected error Message: ", Expected_error_message, "But Found: ", Actual_error_message)

driver.quit()