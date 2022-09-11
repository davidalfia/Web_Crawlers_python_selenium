from selenium import webdriver
from configure import *


class ChromeDriver(object):

    def __init__(self):
        self.driver = webdriver.Chrome(service=chrome_service)

    def get(self, path):
        self.driver.get(path)

    def quit(self):
        self.driver.quit()

