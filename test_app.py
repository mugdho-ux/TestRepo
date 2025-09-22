from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Auto-download compatible ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://localhost:8000/index.html")

greeting = driver.find_element(By.ID, "greeting").text
assert greeting == "Hello, Jenkins CI/CD!"

button = driver.find_element(By.ID, "clickMe")
button.click()
time.sleep(1)

message = driver.find_element(By.ID, "message").text
assert message == "Button Clicked!"

print("Test Passed ✅")
driver.quit()
