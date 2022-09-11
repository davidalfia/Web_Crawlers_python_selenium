import time
from abc import abstractmethod
from locator import *
from entity.article import Article
import requests
from bs4 import BeautifulSoup
from entity.flight import Flight


def get_p_elements_in_page(url):
    request = requests.get(url)
    data = request.text
    html = BeautifulSoup(data, features="html.parser")
    p_list = html.select('p')
    return p_list


class PageCrawlerBase(object):

    def __init__(self, driver, url):
        self.url = url
        self.driver = driver
        self.driver.get(self.url)

    @abstractmethod
    def get_content(self):
        pass


class BbcPageCrawler(PageCrawlerBase):

    def get_content(self):
        url_list = self.driver.find_elements(*BbcArticlesListPageLocator.ARTICLES_LIST)
        articles = []
        for li in url_list:
            a = li.find_element(*BbcArticlesListPageLocator.ARTICLE_LI_ELEMENT)
            url = a.get_attribute('href')
            p_list = get_p_elements_in_page(url)
            article_text = ''
            for t in p_list:
                article_text += t.text + ' '
            article = Article(url, article_text)
            articles.append(article)
        return articles


class FlightsPageCrawler(PageCrawlerBase):

    def get_content(self):
        time.sleep(5)
        tr_list = self.driver.find_elements(*FlightsTablePageLocator.Flights_Table)
        flights = []
        for tr in tr_list:
            td_list = tr.find_elements(*FlightsTablePageLocator.Table_Td_Element)
            flights.append(Flight(td_list[0].text,
                                  td_list[1].text,
                                  td_list[2].text,
                                  td_list[3].text,
                                  td_list[4].text,
                                  td_list[5].text,
                                  td_list[6].text))
        return flights
