import time
from selenium import webdriver
from bs4 import BeautifulSoup
from pandas import DataFrame

driver = webdriver.Chrome('../../files/chromedriver.exe')
driver.get('http://www.encar.com/ev/ev_carsearchlist.do?carType=ev&searchType=model&TG.R=D#!{"action":"(And.Hidden.N._.CarType.A._.(C.GreenType.Y._.EvType.전기차.)_.FuelType.전기.)","toggle":{},"layer":"","sort":"ModifiedDate","page":1,"limit":20}')
driver.implicitly_wait(3)
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')
manufacturer = soup.select('span.cls > strong')
model = soup.select('span.cls > em')
trim = soup.select('span.dtl > strong')
year = soup.select('span.detail > span.yer')
km = soup.select('span.detail > span.km')
location = soup.select('span.detail > span.lo') + soup.select('span.detail > span.loc')

old_cars = []
for car in zip(manufacturer, model, trim, year, km, location):
    old_cars.append(
        {
            'manufacturer' : car[0].text,
            'model' : car[1].text,
            'trim' : car[2].text,
            'year' : car[3].text,
            'km' : car[4].text,
            'location' : car[5].text,
        }
    )

data = DataFrame(old_cars)
data.to_csv('../../files/csv/encar_{}.csv'.format(time.time()), mode='w')
