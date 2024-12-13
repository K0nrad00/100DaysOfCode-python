from selenium import webdriver
from selenium.webdriver.common.by import By

## Keep Chrome opened after program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

##initialize object of chrome webdriver with options above
## driver = webdriver.Chrome(options=chrome_options)

driver_ff= webdriver.Firefox()
# driver_ff.get("https://www.amazon.com")

# driver_ff.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
driver_ff.get("https://www.python.org/")
## as per Day 47 - scraping with bs4:
## https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6
## price:  name=span, class_="a-price-whole" + . + name=span, class_="a-price-decimal"
# price_dollar = driver_ff.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver_ff.find_element(By.CLASS_NAME, value="a-price-fraction")
## get text content of a class ref: https://www.selenium.dev/documentation/webdriver/elements/information/#text-content
# print(f"{price_dollar.text}.{price_cents.text}")

search_bar_python_org = driver_ff.find_element(By.NAME, value="q")
# This .tag_name or .get_attribute() that is all selenium documented
print(search_bar_python_org.tag_name) #input - which is searchbar
print(search_bar_python_org.get_attribute("placeholder")) # Search

button = driver_ff.find_element(By.ID, value="submit")
print(button.text) # GO
print(button.size) # size of element

# find by CSS selector:
documentation_link = driver_ff.find_element(By.CSS_SELECTOR, value=".documentation-widget a") # its anchor tag within documentation-widget class on python.org web
print(documentation_link.text)

## Xpath search - used when even CSS fails to find element
## example: search for 'Submit Website Bug' on python.org
## /html/body/div/footer/div[2]/div/ul/li[3]/a

bug_link = driver_ff.find_element(By.XPATH, value='/html/body/div/footer/div[2]/div/ul/li[3]/a')
print(bug_link.text)            # get link text
print(bug_link.tag_name)               # get element name, tag name
print(bug_link.get_attribute("href")) # get link

## find_elements()
get_all_css = driver_ff.find_elements(By.CSS_SELECTOR, value=".site-base")
# print(get_all_css.text)
print("\nGET ALL CSS ELEMENTS WITH CLASS 'site-base'")
for element in get_all_css:
    print(element.text)


## CHALLENGE:
print("\nCHALLENGE - get 'Upcoming events in dictionary like so "
      "{0: "
      "{'time' :  '<time>',"
      " 'event': '<event>'}, "
      "1 : "
      "{'time' :  '<time>',"
      " 'event': '<event>'}, ")

## dates: /html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li[1]/time
## events: /html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li[1]/a

# /html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li[2]/time
get_event_dates = driver_ff.find_elements(By.XPATH, value="/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li/time")
get_event_descs = driver_ff.find_elements(By.XPATH, value="/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li/a")

# print(get_event_date.text, get_event_desc.text)
dates = [date.text for date in get_event_dates]
events = [event.text for event in get_event_descs]

print(dates)
print(events)
events_dict = {}

for n in range(len(get_event_dates)):
    events_dict[n] = {
        "time" : get_event_dates[n].text,
        "name" : get_event_descs[n].text,
    }

print(events_dict)




# driver.close() # closes tab programatically
driver_ff.quit()     # closes browser
