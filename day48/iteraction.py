import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # to use 'Enter' action e.g. for searching 'Python' in search box

driver_ff = webdriver.Firefox()

# CHALLENGE: get number or articles (on the top) from main https://en.wikipedia.org/wiki/Main_Page
print("Challenge 1:")
driver_ff.get("https://en.wikipedia.org/wiki/Main_Page")
# 6,915,721 - <a href="/wiki/Special:Statistics" title="Special:Statistics">6,915,721</a>
# CSS: #articlecount > a:nth-child(1)
number_or_articles = driver_ff.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(number_or_articles.text)

# # HOw to click on something:
# number_or_articles.click()

## search by link name and click it - more common approach:
all_portals = driver_ff.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

## search for Python in search bar:
search = driver_ff.find_element(By.NAME, value="search")
search.send_keys("Python")

## send enter after 'Python' is in search box
search.send_keys(Keys.ENTER)


time.sleep(5)

driver_ff.quit()