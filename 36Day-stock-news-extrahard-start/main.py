import requests
from datetime import datetime, timedelta
from twilio.rest import Client


STOCK_API_KEY = ""
NEWS_API_KEY = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""


STOCK = "CRM"
COMPANY_NAME = "Salesforce"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

three_recent_articles = []
news_params = {
    # "q" : COMPANY_NAME,
    "qinTitle": COMPANY_NAME,
    "apikey" : NEWS_API_KEY,
    "pageSize" : "3",
    "page": "1",
    "sortBy": "publishedAt",
    # "category": "business",
    "language" : "en",
}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
news_response.raise_for_status()
# print(news_response.status_code)
news_data = news_response.json()
print(len(news_data["articles"]))
print(news_data["articles"])
def get_recent_articles():
    articles = news_data["articles"]
    for article in articles:
        three_recent_articles.append(f"Date: {article['publishedAt'][:10]} Headline: {article['title']}, Brief: {article['description']}, More: {article['url']}")
    return three_recent_articles


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#
def send_whatsapp(number_of_article):
    twilio_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    whatsapp_message = twilio_client.messages.create(
        from_='whatsapp:+14155238886',
        body=f"{STOCK}:{percentage_difference}%:\n{get_recent_articles()[number_of_article]}",
        to='whatsapp:+3538xxxxx' # update with ph no
    )
    print(whatsapp_message.status)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# https://www.alphavantage.co/documentation/#time-series-data

today = datetime.today()
today_date = datetime.date(today)
yesterday = today_date - timedelta(1)
# print(yesterday)
day_before_yesterday = yesterday - timedelta(1)
# print(day_before_yesterday)

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : STOCK_API_KEY,
}
response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
response.raise_for_status()

data = response.json()

print(data)
day_before_yesterday_close_price = 100.123
yesterday_close_price = 200.123
# Check for rate limit in stock API:
if "Information" not in data.keys():
    yesterday_close_price = float(data['Time Series (Daily)'][str(yesterday)]['4. close']) # this will not work if there was no news yesterday
    day_before_yesterday_close_price = float(data['Time Series (Daily)'][str(day_before_yesterday)]['4. close'])
elif "API rate limit" in data["Information"]:
    # use test data only if warned about API limit for alphavantage
    day_before_yesterday_close_price = 100.123
    yesterday_close_price = 200.123
else:
    day_before_yesterday_close_price = 100.123
    yesterday_close_price = 200.123


# else:

percentage_difference = round(((yesterday_close_price - day_before_yesterday_close_price) / yesterday_close_price)*100, 2)
absolute_percentage_difference = abs(percentage_difference)

if absolute_percentage_difference >= 5.0: # with abs() function that's all its needed
    print(get_recent_articles())
    # send_whatsapp(0)
    # send_whatsapp(1)
    # send_whatsapp(2)
    try:
        for msg in range(3):
            send_whatsapp(msg)
    except:
        print("Can't send whatsapp x 3")
else:
    print("In brackets")
    try:
        send_whatsapp(0)
    except:
        print("can't send whatsapp")



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

