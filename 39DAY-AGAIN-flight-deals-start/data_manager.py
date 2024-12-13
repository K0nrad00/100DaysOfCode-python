import requests
import os


SHEETY_URL = "https://api.sheety.co/61600b4f0c4e0d5ed5b52ba5d81edb12/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self._token = os.environ["SHEETY_TOKEN"]
        self.headers = {
            "Authorization" : self._token,
        }

    def get_sheets_data(self):
        response = requests.get(url=SHEETY_URL, headers=self.headers)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_sheet_iataCode(self):
        for city in self.destination_data:
            body = {
                "price": {"iataCode" : city["iataCode"]}
            }
            response_put = requests.put(url=f"{SHEETY_URL}/{city['id']}", headers=self.headers, json=body)

        print(response_put.text)
