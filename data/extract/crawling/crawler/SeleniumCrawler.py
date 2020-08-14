import sys
import os
import time
from selenium import webdriver
from pandas import DataFrame
sys.path.append('..')
import settings

class SeleniumCrawler():
    def __init__(self, url, scrapping):
        self.webdriver = settings.webdriver
        self.url = url
        self.scrapping = scrapping

    def set_crawler(self):
        driver = webdriver.Chrome(self.webdriver)
        driver.get(self.url)
        driver.implicitly_wait(5)
        self.html = driver.page_source
        driver.quit()

    def crawling(self):
        data = self.scrapping(self.html)
        self.dataframe = DataFrame(data)

    def save_to_csv(self, filename):
        save_file = os.path.join(settings.output_csv_dir, '{}_{}.csv'.format(filename, time.time()))
        self.dataframe.to_csv(save_file, mode='w')
