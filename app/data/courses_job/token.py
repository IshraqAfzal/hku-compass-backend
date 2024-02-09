import time, json, os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def get_bearer_token(driver, logger):
  logger.info("Fetching Auth Bearer Token")
  url = "https://class-planner.hku.hk/"
  driver.get(url)
  token = None

  try:
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.TAG_NAME, "button"))
    )
    driver.find_element(By.TAG_NAME, 'button').click()
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.TAG_NAME, "input"))
    )
    time.sleep(2)
    email_input = driver.find_element(By.TAG_NAME, 'input')
    email_input.send_keys(os.getenv("HKU_USERNAME"))
    email_input.send_keys(Keys.RETURN)
    time.sleep(2)
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "passwordInput"))
    )
    email_input = driver.find_element(By.ID, 'passwordInput')
    email_input.send_keys(os.getenv("HKU_PASSWORD"))
    email_input.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "idSIButton9"))
    )
    email_input = driver.find_element(By.ID, 'idSIButton9').click()
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CLASS_NAME, "MuiDataGrid-columnHeaderTitleContainer"))
    )
    local = driver.execute_script("return {...localStorage}")
    for key in local:
      local = local[key]
      break
    local = json.loads(local)
    secret = local['secret']
    token = 'Bearer ' + secret
    logger.info("Fetched Auth Bearer Token")
  except Exception as ex:
    logger.error(ex)
  
  return token