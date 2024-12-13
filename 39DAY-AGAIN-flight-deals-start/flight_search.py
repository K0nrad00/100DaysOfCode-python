import os
import requests
from datetime import datetime as dt, timedelta

AMADEUS_URL_AUTH = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_LOCATIONS = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
AMADEUS_PRICES = "https://test.api.amadeus.com/v2/shopping/flight-offers"
ORIGIN_IATA = "DUB" # Dublin airport
AMADEUS_FLIGHT_DATES = "https://test.api.amadeus.com/v1/shopping/flight-dates"

# from serpapi import GoogleSearch
# G_SEARCH_URL = "https://serpapi.com/search.json?engine=google_flights"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        # self.data = {}
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self._get_new_token()
        self.header = {
            "Authorization" : f"Bearer {self._token}"
        }


    def _get_new_token(self):
        base_header = {
            "Content-Type" : "application/x-www-form-urlencoded",
        }
        body = {
            "grant_type" : "client_credentials",
            "client_id" : self._api_key,
            "client_secret" : self._api_secret,
        }
        response = requests.post(url=AMADEUS_URL_AUTH, headers=base_header, data=body)
        return response.json()["access_token"]
        # {'type': 'amadeusOAuth2Token', 'username': 'konrad.wrobel.tidal@gmail.com', 'application_name': 'Flight Deals',
        #  'client_id': 'eGkBOqK9LGBpLZ6jB8JGShO2tmzDhXHf', 'token_type': 'Bearer',
        #  'access_token': 'DIwPMj4ZAGGMzKJtW2M9oQiyelhs', 'expires_in': 1799, 'state': 'approved', 'scope': ''}
        # None


    def get_iataCode(self, city_name):
        # iata_code = "TESTING"

        parameters = {
            "keyword" : city_name,
            "max" : 2, # google sheet cant have more than 10 cities , ref: https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/city-search/api-reference
            "include": "AIRPORTS",
        }
        response = requests.get(url=AMADEUS_LOCATIONS, headers=self.header , params=parameters)
        try:
            iata_code = response.json()['data'][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return iata_code

    ## my own + copied from: https://gist.github.com/TheMuellenator/2ebb13d348c4a91b4ab27d1fd3627fb0#file-flight_search-py-L85
    # def get_flight_prices(self, destination_city_code):
    #     tomorrow = ((dt.today() + timedelta(1)).strftime("%Y-%M-%d"))
    #     date_in_6_months = ((dt.today() + timedelta(182)).strftime("%Y-%M-%d")) # 182
    #     parameters = {
    #         "originLocationCode" : ORIGIN_IATA,
    #         "destinationLocationCode": destination_city_code,
    #         "departureDate" : f"{tomorrow}",
    #         "returnDate":f"{date_in_6_months}",
    #         "adults": 1,
    #         "nonStop": "true",
    #         "currencyCode" : "EUR",
    #     }
    #
    #     response = requests.get(url=AMADEUS_PRICES, headers=self.header, params=parameters)
    #     # currency = response.json()["data"][1]["currency"]
    #     # price = response.json()["data"][1]["grandTotal"]
    #     # print(f"Getting flights for {self.get_iataCode}:\n Price: {currency}{price}")
    #     if response.status_code != 200:
    #         print(f"get_flight_prices() response code: {response.status_code}")
    #         print("There was a problem with the flight search.\n"
    #               "For details on status codes, check the API documentation:\n"
    #               "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
    #               "-reference")
    #         print("Response body:", response.text)
    #         return None
    #
    #     return response.json()

    # https://developers.amadeus.com/self-service/category/flights/api-doc/flight-cheapest-date-search/api-reference
    # def check_flights(self, destination_city_code):
    #     tomorrow = str((dt.today() + timedelta(1)).strftime("%Y-%M-%d"))
    #     date_in_6_months = str((dt.today() + timedelta(182)).strftime("%Y-%M-%d")) # 182
    #     parameters = {
    #         "origin" : ORIGIN_IATA,
    #         "destination" : destination_city_code,
    #         "departureDate": f"{tomorrow},{date_in_6_months}",
    #         # "duration": "10", # optional
    #         "nonStop" : "true",
    #     }
    #     response = requests.get(url=AMADEUS_FLIGHT_DATES, headers=self.header, params=parameters)
    #     if response.status_code != 200:
    #         print(f"Status code from check_flights: {response.status_code}")
    #         print("Response body: ", response.json())
    #
    #     return response.json()

    # RESPONSE: Status code from check_flights: 400
    # Response body:  {'errors': [{'status': 400, 'code': 425, 'title': 'INVALID DATE', 'detail': 'Date does not exist.', 'source': {'parameter': 'departureDate'}}]}
    # {'errors': [{'status': 400, 'code': 425, 'title': 'INVALID DATE', 'detail': 'Date does not exist.', 'source': {'parameter': 'departureDate'}}]}

## THIS ^ DOESNT WORK, maybe this: https://serpapi.com/google-flights-api is an option?

    # def check_flights(self, destination_city_code):
    #     tomorrow = str((dt.today() + timedelta(1)).strftime("%Y-%M-%d"))
    #     date_in_6_months = str((dt.today() + timedelta(182)).strftime("%Y-%M-%d"))