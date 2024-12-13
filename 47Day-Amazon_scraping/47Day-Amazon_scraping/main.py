from fileinput import close

from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

# TEST_URL = "https://appbrewery.github.io/instant_pot/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:132.0) Gecko/20100101 Firefox/132.0",
    "Accept-Language": "en-US,en;q=0.5",
}

# AMAZON_URL= "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6" # this is for pot
AMAZON_HEADPHONES = "https://www.amazon.co.uk/Sony-WH-CH520-Wireless-Bluetooth-Headphones-Black/dp/B0BTJD6LCL/ref=sr_1_3?crid=3PB6AKW1UW67B&dib=eyJ2IjoiMSJ9.czqDi7nK5ti_uPH6fjbPeH1E7_TQszZjcEE_MdrUY5RY6VhguK5K28jSulMnaCcV9ghxCMJs0KZbguI6uJwWV5WsZPOKRk5-OYZo5E10UaL_-iQe_DLgDfBUnowsfNCN_xajXIB2BvFnyNhYFuZmIis0qqjp5ExEdY6_vEi_P3CBtu9yxJ_bNK9HzU5IHUOle96mxajI-eIt7fsU_PeOWi2sGC5GAfV4TqtNTQBQObM.YzkV0X7AU-v7w57sQxyDWy2Q5qRJa9Yym-ZkOIsX1gA&dib_tag=se&keywords=ch520&nsdOptOutParam=true&qid=1732275295&sprefix=ch520%2Caps%2C101&sr=8-3"

response = requests.get(url=AMAZON_HEADPHONES, headers=HEADERS)
response.raise_for_status()
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.title)   # test

# get_price = soup.find(name="span", class_="aok-offscreen").getText().split("$")
price_in_UK = soup.find(name="span", class_="aok-offscreen").getText()
# price_without_currency = get_price[1]
print(price_in_UK)
# https://www.udemy.com/course/100-days-of-code/learn/lecture/44701301#overview
price_gbp = price_in_UK.split()[0]
price_gbp_float = price_gbp.split("£")[1]

product_name = soup.find(name="span", id="productTitle").getText()#.replace(" ", "") # strip() could be used here

print(product_name)
# print(type(product_name))
# print(product_name.replace(" ", ""))


if float(price_gbp_float) < 100:
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"]) as connection:
        connection.starttls()  # secure with tls connection
        connection.login(user=os.environ["EMAIL_ADDRESS"], password=os.environ["EMAIL_PASSWORD"])
        connection.sendmail(from_addr=os.environ["EMAIL_ADDRESS"], to_addrs=os.environ["EMAIL_ADDRESS"],
                            msg=f"Subject:Amazon price alert\n\nThis item: {product_name} is of price £{price_gbp_float}, check {AMAZON_HEADPHONES}".encode("utf-8"))