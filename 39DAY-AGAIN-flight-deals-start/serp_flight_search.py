# f6a1252d9abf136ea8acc3a1824d115000733e114f196a9719f8d35477b025ad

from serpapi import GoogleSearch
G_SEARCH_URL = "https://serpapi.com/search.json?engine=google_flights"

class SerpFlightSearch:
    def __init__(self):
        self._token = "f6a1252d9abf136ea8acc3a1824d115000733e114f196a9719f8d35477b025ad"

    def get_iataCode(self, city_name):
        parameters = {

        }
