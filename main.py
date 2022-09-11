from entity.driver import ChromeDriver
from api import get, search


def run():
    driver = ChromeDriver().driver
    get(driver)
    driver.quit()
    search()


if __name__ == "__main__":
    run()
