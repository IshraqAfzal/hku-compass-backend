import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Create a selenium driver
def create_driver():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--enable-javascript")
        options.add_argument("--headless")  # Run the driver on the background
        options.add_argument("--disable-logging")
        options.add_argument("--no-sandbox")

        # Specify the path of the ChromeDriver
        chrome_driver_path = r"C:\Users\ishraq\Downloads\chromedriver.exe"
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    except Exception as e:
        logging.error(f"Error creating Chrome driver: {e}")
        raise e