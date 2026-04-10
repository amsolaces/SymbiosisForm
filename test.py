from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Setup Chrome driver (auto-managed)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # ✅ FIX: Use relative path (works in Jenkins + local)
    file_path = os.path.abspath("index.html")
    driver.get("file:///" + file_path)

    # ✅ Use explicit wait instead of time.sleep
    wait = WebDriverWait(driver, 10)

    # Fill form
    wait.until(EC.presence_of_element_located((By.ID, "name"))).send_keys("Arpan")
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("arpan@gmail.com")
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("123456")
    wait.until(EC.presence_of_element_located((By.ID, "confirm"))).send_keys("123456")

    # Select options
    wait.until(EC.element_to_be_clickable((By.ID, "gender-male"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "course"))).send_keys("BTech")

    # Submit form
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']"))).click()

    # Handle alert
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()

finally:
    driver.quit()
