import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/Users/Jihun/Desktop/chromedriver.exe')
driver.get('http://www.encar.com/ev/ev_carsearchlist.do?carType=ev&searchType=model&TG.R=D#!%7B%22action%22%3A%22(And.Hidden.N._.CarType.A._.(C.GreenType.Y._.EvType.%EC%A0%84%EA%B8%B0%EC%B0%A8.)_.FuelType.%EC%A0%84%EA%B8%B0.)%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A20%7D');   	# 구글에 접속
time.sleep(1)

html = driver.page_source
bs = BeautifulSoup(html, 'html.parser')
manufacturer = bs.select('span.cls > strong')
model = bs.select('span.cls > em')
trim = bs.select('span.dtl > strong')
year = bs.select('span.detail > span.yer')
km = bs.select('span.detail > span.km')
location = bs.select('span.detail > span.lo') + bs.select('span.detail > span.loc')

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
print(old_cars)
print(len(old_cars))
