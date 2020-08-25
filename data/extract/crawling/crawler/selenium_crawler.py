import sys
import os
import time
from selenium import webdriver
from pandas import DataFrame
import settings

class SeleniumCrawler():
    WAIT_TIME = 20

    def __init__(self, url, scrapping):
        self.webdriver = settings.WEBDRIVER
        self.url = url
        self.scrapping = scrapping

    def set_crawler(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        driver = webdriver.Chrome(self.webdriver, chrome_options=options)
        driver.get(self.url)
        driver.implicitly_wait(SeleniumCrawler.WAIT_TIME)
        self.html = driver.page_source
        driver.quit()

    def crawling(self):
        data = self.scrapping(self.html)
        self.dataframe = DataFrame(data)
        return self.dataframe
