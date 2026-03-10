from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# NOTE: Selenium Manager (bundled with Selenium 4.6+) will automatically download a suitable driver.
# If you run into driver issues, ensure your Chrome/Chromium is installed and up to date.

driver = webdriver.Chrome()

# Delay between actions to make the automation visibly slower.
step_delay = 1.0

try:
    driver.get("file:///C:/Users/arpan/OneDrive/Desktop/Work/SymbiosisForm/index.html")
    time.sleep(step_delay)

    driver.find_element(By.ID, "name").send_keys("Arpan")
    time.sleep(step_delay)

    driver.find_element(By.ID, "email").send_keys("arpan@gmail.com")
    time.sleep(step_delay)

    driver.find_element(By.ID, "password").send_keys("123456")
    time.sleep(step_delay)

    driver.find_element(By.ID, "confirm").send_keys("123456")
    time.sleep(step_delay)

    # Select gender and course (matches the updated form structure).
    driver.find_element(By.ID, "gender-male").click()
    time.sleep(step_delay)
    driver.find_element(By.ID, "course").send_keys("BTech")
    time.sleep(step_delay)

    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Wait for the alert to appear, then accept it.
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()

    # Give the browser a moment to settle before quitting.
    time.sleep(20)
finally:
    driver.quit()
