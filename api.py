from pageCrawler import BbcPageCrawler,FlightsPageCrawler
from operations.saveContentModule import SaveContentModule
from operations.search import NewsSearch, FlightSearch

"""
the api gives the user operation to Scrap website and search in all download files
"""


def get_bbc_content(driver):
    bbc = BbcPageCrawler(driver, "https://bbc.com")
    list_data = bbc.get_content()
    SaveContentModule.save(list_data, "bbc")


def get_flights_content(driver):
    flights_crawler = FlightsPageCrawler(driver, "https://www.iaa.gov.il/airports/ben-gurion/flight-board")
    list_data = flights_crawler.get_content()
    SaveContentModule.save(list_data, "flights")


def search_in_articles(wanted,result):
    sn = NewsSearch(wanted)
    result.append(sn.search())


def search_in_flights(wanted,result):
    sn = FlightSearch(wanted)
    result.append(sn.search())


def print_result(result):
    print(*result, sep='\n')


def get(driver):
    get_bbc_content(driver)
    get_flights_content(driver)


def search():
    wanted = input("please enter wanted expression OR E to finish\n")
    while wanted != 'E':
        result = []
        search_in_articles(wanted, result)
        search_in_flights(wanted, result)
        print_result(result)
        wanted = input("please enter search code OR E to finish\n")

