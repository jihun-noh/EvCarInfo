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
        driver = webdriver.Chrome(self.webdriver)
        driver.get(self.url)
        driver.implicitly_wait(SeleniumCrawler.WAIT_TIME)
        self.html = driver.page_source
        driver.quit()

    def crawling(self):
        data = self.scrapping(self.html)
        self.dataframe = DataFrame(data)
        return self.dataframe

    def save_to_csv(self, filename):
        save_file = os.path.join(settings.OUTPUT_CSV_DIR, '{}_{}.csv'.format(filename, time.time()))
        self.dataframe.to_csv(save_file, mode='w')
