import time

from selenium import webdriver
from selenium.webdriver.common.by import By



driver_f = webdriver.Firefox()

driver_f.get("http://secure-retreat-92358.herokuapp.com/")
print("Challenge 2: use website in driver_f.get() to fill in your details; first, last, email and 'Sign Up' option to sign up for fake newsletter")
first_name = driver_f.find_element(By.NAME, value="fName")
first_name.click()
first_name.send_keys("my-fake-fname")

last_name = driver_f.find_element(By.NAME, value="lName")
last_name.click()
last_name.send_keys("my-fake-lname")

email_add = driver_f.find_element(By.NAME, value="email")
email_add.click()
email_add.send_keys("my-fake-email@email.com")

sign_up_button = driver_f.find_element(By.XPATH, value='/html/body/form/button')
sign_up_button.click()



time.sleep(5)
driver_f.quit()
