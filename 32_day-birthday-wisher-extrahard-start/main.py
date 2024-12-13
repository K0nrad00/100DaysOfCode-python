##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import random
import pandas
import smtplib

today = dt.datetime.today()
current_month = today.month
current_day = today.day

# data = pandas.DataFrame(read_csv("birthdays.csv"))
data = pandas.read_csv("birthdays.csv")
list_of_rows = data.to_dict(orient="records")

list_of_letter_files = ["letter_templates/letter_1.txt" , "letter_templates/letter_2.txt" , "letter_templates/letter_3.txt"]
random_letter = random.choice(list_of_letter_files)

gmail = "k3054294@gmail.com"
password = "uzls bkey zmgl qpyk"  # gmail App Password
# yahoo = "k3054@yahoo.com"

def pick_random_letter():
    global first_line, rest_of_letter
    with open(random_letter) as f:
        lines = f.readlines()
        first_line = lines[0].replace("[NAME]", row["name"])    # could use row.name  - pandas functionality but only if I used iterrows instead of orient="records"
        rest_of_letter = ''.join(lines[1:])

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secure with tls connection
        connection.login(user=gmail, password=password)
        connection.sendmail(from_addr=gmail, to_addrs=row['email'],
                            msg=f"Subject:Happy Birthday {row['name']}\n\n{first_line}\n{rest_of_letter}")


for row in list_of_rows:
    if current_month == row["month"] and current_day == row["day"]:
        pick_random_letter()
        send_email()
