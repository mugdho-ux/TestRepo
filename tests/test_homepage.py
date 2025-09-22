from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_homepage_shows_welcome():
    options = webdriver.ChromeOptions()
    # headless so it runs on Jenkins without visible UI
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        driver.get("http://localhost:8000")
        assert "My Local Site" in driver.title
        el = driver.find_element(By.ID, "welcome")
        assert el.text == "Hello from Jenkins Demo"
    finally:
        driver.quit()
