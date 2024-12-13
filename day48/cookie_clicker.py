# https://www.udemy.com/course/100-days-of-code/learn/lecture/21752028#overview

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time

driver_cookie = webdriver.Firefox()
driver_cookie.get("http://orteil.dashnet.org/experiments/cookie/")

## find cookie:
cookie = driver_cookie.find_element(By.ID, value="cookie")  # to click
score = driver_cookie.find_element(By.ID, value="money")    # to check for score/money

updated_score = 0
play = True
# start_time = datetime.now().time()
# now = time.time()
five_seconds = time.time() + 5 # https://stackoverflow.com/questions/13293269/how-would-i-stop-a-while-loop-after-n-amount-of-time
# print(now)

print(five_seconds)

# while play:
#     time.sleep(0.1)
#     second_counter = 0
#     cookie.click()
#     updated_score += int(score.text)
#     if second_counter == 5 or time.time() > five_seconds :
#         print(updated_score)
#         break # instead of break wanna check what we can buy and continue
#     second_counter -= 1


def get_store_options():
    store = driver_cookie.find_element(By.ID, value="store")
    all_options = store.text.split("\n") # all the options from store
    return all_options

get_store_options()

def get_item_and_price(my_list):
    return my_list[0::2]

l = get_item_and_price(get_store_options())
print(f"every item and price: {l}")

def get_price(list_of_items):
    prices = [item.split("-") for item in list_of_items]
    return prices

print(get_price(l))




# print(updated_score)
# upgrades = driver_cookie.find_elements(By.ID, value="#rightPanel #store")
# for upgrade in upgrades:
#     print(len(upgrade))
# time.sleep(5)

# html body#whole div#game div#rightPanel div#store div#buyCursor b
# driver_cookie.quit()
