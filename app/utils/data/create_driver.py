from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--enable-javascript")
    options.add_argument("--headless")
    options.add_argument("--disable-logging")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver