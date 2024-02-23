from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions



# Create a new instance of the Chrome driver
options = ChromeOptions()
options.set_capability('sessionName', 'BStack Sample Test')
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open the Amazon sign-in page
driver.get("https://www.amazon.com")
time.sleep(5)

# Find the sign-in link and click on it
sign_in_link = driver.find_element(By.ID, 'nav-link-accountList')
sign_in_link.click()

# Wait for the page to load
time.sleep(5)

# Find the email input field and enter your email
email_input = driver.find_element(By.ID,'ap_email')
email_input.send_keys('jashabc@gmail.com')

# Find the continue button and click on it
continue_button = driver.find_element(By.ID,'continue')
continue_button.click()

# Wait for the page to load
time.sleep(5)

# Find the password input field and enter your password
password_input = driver.find_element(By.ID,'ap_password')
password_input.send_keys('abc@xyz')

# Find the sign-in button and click on it
sign_in_button = driver.find_element(By.ID,"signInSubmit")
sign_in_button.click()

# Wait for the login process to complete
time.sleep(5)

# Confirm successful login
if "Your Account" in driver.title:
    print("Login successful!")
else:
    print("Login failed.")

# Close the browser
driver.quit()
