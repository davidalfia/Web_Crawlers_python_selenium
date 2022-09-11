import json
from abc import abstractmethod

"""
-- this module gives a search service in all downloaded files --  
"""

"""
base search gets the requested value to be searched
@:param wanted = requested value to be searched
"""


class SearchBase(object):
    def __init__(self, wanted):
        self.wanted = wanted

    @abstractmethod
    def search(self):
        pass


"""
derived from BaseSearch, allows search in Articles results
"""


class NewsSearch(SearchBase):

    def search(self):
        result = []
        with open('bbc.json', 'r', encoding='utf8') as file:
            data = json.load(file)
        for article in data:
            result.append(article['url']) if self.wanted in article['text'] else None
        return result if result else "No match found at articles"

"""
derived from BaseSearch, allows search in Flights results
"""


class FlightSearch(SearchBase):

    def search(self):
        result = []
        with open('flights.json', 'r', encoding="utf8") as file:
            data = json.load(file)
        for flight in data:
            for value in flight.values():
                if self.wanted in value:
                    result.append(flight)

        return result if result else "No match found at Flights"
