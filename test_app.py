from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chrome driver path (উইন্ডোজে যেটা ইনস্টল করেছ)
driver_path = r"D:\mugdho\jenkins-projects\my-website\tests\chromedriver.exe"


driver = webdriver.Chrome(executable_path=driver_path)

# ওয়েবসাইট লোকালহোস্টে রান করছে ধরি (http://localhost:8000)
driver.get("http://localhost:8000/index.html")

# টেস্ট স্টেপস
greeting = driver.find_element(By.ID, "greeting").text
assert greeting == "Hello, Jenkins CI/CD!"

button = driver.find_element(By.ID, "clickMe")
button.click()
time.sleep(1)

message = driver.find_element(By.ID, "message").text
assert message == "Button Clicked!"

print("Test Passed ✅")
driver.quit()
