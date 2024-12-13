import time
from data_manager import DataManager
from flight_data import FlightData
# import flight_data
from flight_search import FlightSearch

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

print("This")

# SHEETY_USERNAME="konw"
# SHEETY_PASSWORD="ThisIsMyPassword34!YOLO"
# SHEETY_TOKEN="Basic a29udzpUaGlzSXNNeVBhc3N3b3JkMzQhWU9MTw=="
# BEARER_TOKEN="Bearer x*@WiiypWbVZBdxt&TducHqEuNJ#wQbt!@W7t" # sheety
# AMADEUS_API_KEY="eGkBOqK9LGBpLZ6jB8JGShO2tmzDhXHf"
# AMADEUS_API_SECRET="Tf7x9AgpPdDpCSYy"

# test sheety:
# ==================== Set up the Flight Search ====================
data_manager = DataManager()
sheet_data = data_manager.get_sheets_data()
# print(sheet_data)
flight_search = FlightSearch()


# ==================== Update the Airport Codes in Google Sheet ====================
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_iataCode(row["city"])
        # print(flight_search.get_iataCode(row["city"])) # TEST
        # print(row["iataCode"]) # TEST
        time.sleep(2) # slowing down requests to avoid rate limit
# print(flight_search._get_new_token()) # TEST ONLY
print(f"sheet_data:\n {sheet_data}")

# data_manager.destination_data = sheet_data
# data_manager.update_sheet_iataCode()
# print("\nBREAK\n")
# print(flight_search.check_flights("PAR"))

# Copied from: https://gist.github.com/TheMuellenator/2ebb13d348c4a91b4ab27d1fd3627fb0#file-main-py-L29
# flight_data = FlightData()
#
# for destination in sheet_data:
#     print(f"Getting flights for {destination['city']}...")
#     flights = flight_search.get_flight_prices(destination["iataCode"])
#     cheapest_flight = flight_data.find_cheapest_flight(flights)
#     print(f"{destination['city']}: EUR{cheapest_flight.price}")
#     # Slowing down requests to avoid rate limit
#     time.sleep(2)


# GETTING ERROR with date:
# Potential solution:
# https://stackoverflow.com/questions/72439103/amadeus-flights-api-error-carrier-code-is-a-2-or-3-alphanum-except-yy-and-yyy