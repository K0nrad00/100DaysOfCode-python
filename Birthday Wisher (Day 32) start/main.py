# import smtplib
#
# # test email:
# gmail = "k3054294@gmail.com"
# password = "uzls bkey zmgl qpyk" # gmail App Password
# yahoo = "k3054@yahoo.com"
#
# with smtplib.SMTP("smtp.gmail.com") as connection: # create connection
#     connection.starttls()                       # secure with tls connection
#     connection.login(user=gmail, password=password)
#
#     connection.sendmail(from_addr=gmail, to_addrs=yahoo,
#                         msg="Subject:Hello\n\n This is the body of email")
# # connection.close()


import datetime as dt
import random
import smtplib
# from dateutil.utils import today
#
# now = dt.datetime.now()
# print(now)
# year = now.year
# print(year, type(year))
#
# if year == 2024:
#     print(f"its year {year}")
#
# month = now.month
#
#
# date_of_birth = dt.datetime(year=1995 , month= 12, day= 15 )



# Challenge:
# Send email ourselves motivational quote on current day of the week
now = dt.datetime.now()
day_of_week = now.weekday()
# print(day_of_week) # indexed, so monday = 0, Tuesday = 1 etc
# today_day = now.today().weekday() # https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
# print(today)

# weekdays = {0 : "Monday", 1: "Tuesday", 2 : "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

def is_today_quote_day():
    return day_of_week == 1


def random_quote():
    with open("quotes.txt") as f:
        lines = f.readlines()
    return random.choice(lines)

if is_today_quote_day():
    # test email:
    gmail = "k3054294@gmail.com"
    password = "uzls bkey zmgl qpyk" # gmail App Password
    yahoo = "k3054@yahoo.com"
    with smtplib.SMTP("smtp.gmail.com") as connection: # create connection
        connection.starttls()                       # secure with tls connection
        connection.login(user=gmail, password=password)

        connection.sendmail(from_addr=gmail, to_addrs=yahoo,
                            msg=f"Subject:Motivational quote of the day \n\n {random_quote()}")

