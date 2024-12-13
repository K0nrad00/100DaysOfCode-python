import requests
from datetime import datetime
import smtplib

MY_LAT = 53.338329 # Your latitude
MY_LONG = -6.539810 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_close():
    return (MY_LAT-5) <= iss_latitude <= (MY_LAT+5) and (MY_LONG-5)<= iss_longitude <= (MY_LONG+5)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds. ---> while True: time.sleep(60)
gmail = "k3054294@gmail.com"
password = "uzls bkey zmgl qpyk"
# yahoo = "k3054@yahoo.com"

if (time_now.hour >= sunset or time_now.hour <= sunrise) and is_iss_close():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secure with tls connection
        connection.login(user=gmail, password=password)
        connection.sendmail(from_addr=gmail, to_addrs=gmail,
                            msg="Subject:ISS can be seen in your location\n\n"
                                "Look up the night sky - if clear you might see ISS passing")





