from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import time

def collect_prof_data(driver, logger):
  try:
    prof_links = get_prof_profile_links(driver)
    ans = []
    for i in prof_links:
      ans.append(get_prof_info(driver, i))
    return ans
  except Exception as e:
    logger.error("CS Job: Error while collecting professor data. Error: " + str(e))


def get_prof_profile_links(driver):
  prof_links = []
  url = "https://www.cs.hku.hk/people/academic-staff"
  unwanted_links = [
    "https://www.cs.hku.hk/index.php/people/academic-staff/%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20o"
  ]
  driver.get(url)
  time.sleep(3)
  elems = driver.find_element(By.CLASS_NAME, "article-details").find_elements(By.TAG_NAME, "a")
  for elem in elems:
    href = elem.get_attribute('href')
    if href is not None and re.search("^https://www.cs.hku.hk/index.php/people/academic-staff/.", href) is not None and href not in unwanted_links:
        if href not in prof_links:
          prof_links.append(href)
  return prof_links

def get_prof_info(driver, url):
  ret = {}
  driver.get(url)
  elem = driver.find_element(By.CLASS_NAME, "col-md-6")
  soup = BeautifulSoup(elem.get_attribute('innerHTML'), features="html.parser")
  name = soup.h1.get_text().split(" ")
  if name[0] == '\xa0':
    name = soup.h1.find_next_sibling().get_text().split(" ")
  text=soup.get_text().replace(" AT ", "@").replace(" [AT] ", "@").replace(" [DOT] ", ".").replace(u'\xa0', u' ').replace("\n", " ").split(" ")
  ret["title"] = name[0]
  ret["lastname"] = name[1][:-1]
  ret["firstname"] = " ".join(name[2:])
  ret["email"] = text[text.index("Email:") + 1]
  ret["profileLink"] = url
  ret["faculty"] = "Engineering"
  ret["department"] = "Computer Science"
  return ret