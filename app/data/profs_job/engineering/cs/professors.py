from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re, random
import time
from .....utils.data.create_objectid import create_objectid

def generate_random_number(x, y):
  return random.randint(x, y)

def collect_prof_data(driver, logger):
  try:
    prof_links = get_prof_profile_links(driver)
    ans = []
    for i in prof_links:
      ans.append(get_prof_info(driver, i))
    return ans
  except Exception as e:
    logger.error("Error while collecting professor data. Error: " + str(e))


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
  ret["FULLNAME"] = " ".join(name[2:]) + " " + name[1][:-1]
  ret["EMAIL"] = text[text.index("Email:") + 1]
  ret["PROFILE_LINK"] = url
  ret["FACULTY"] = "Engineering"
  ret["DEPARTMENT"] = "Computer Science"
  ret["PROF_ID"] = create_objectid(ret["EMAIL"].split("@")[0] + "_cs")
  ret["ENGAGEMENT"] = generate_random_number(0,5)
  ret["CLARITY"] = generate_random_number(0,5)
  return ret