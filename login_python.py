from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()  # Opens a Chrome browser window

# Open your HTML login form
driver.get("file:///D:/python/project/login%20project/login.html")

# ----- Test Case 1: Valid Login -----
driver.find_element(By.ID, "username").send_keys("admin")       # Enters username
driver.find_element(By.ID, "password").send_keys("admin123")    # Enters password
driver.find_element(By.TAG_NAME, "button").click()              # Clicks Login button

# Pause to observe result (the alert)
time.sleep(2)

# Close the browser
driver.quit()
