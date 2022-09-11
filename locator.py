from selenium.webdriver.common.by import By


class BbcArticlesListPageLocator(object):
    ARTICLES_LIST = (By.CSS_SELECTOR, ".module--promo .media-list li")

    ARTICLE_LI_ELEMENT = (By.TAG_NAME, 'a')


class FlightsTablePageLocator(object):
    Flights_Table = (By.CSS_SELECTOR, "#flight_board-arrivel_table tbody tr")

    Table_Td_Element = (By.TAG_NAME, 'td')
