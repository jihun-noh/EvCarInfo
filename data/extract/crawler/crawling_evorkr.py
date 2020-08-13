import time
from selenium import webdriver
from bs4 import BeautifulSoup
from pandas import DataFrame

driver = webdriver.Chrome('../../files/chromedriver.exe')
driver.get('https://www.ev.or.kr/portal/buyersGuide/incenTive?pMENUMST_ID=21549')
driver.implicitly_wait(3)
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')
purchase_support = []
for tag in soup.select('table.table_02_2_1 tbody > tr'):
    td = tag.select('td')
    td_len = len(td)
    if td_len == 5:
        break;
    elif td_len == 4:
        manufacturer = td[1].contents[0]
        model = td[2].contents[0]
        amount = td[3].contents[0]
    elif td_len == 3:
        manufacturer = td[0].contents[0]
        model = td[1].contents[0]
        amount = td[2].contents[0]
    elif td_len == 2:
        model = td[0].contents[0]
        amount = td[1].contents[0]
    purchase_support.append(
        {
            'manufacturer' : manufacturer,
            'model' : model,
            'amount' : amount
        }
    )

data = DataFrame(purchase_support)
data.to_csv('../../files/csv/evorkr_{}.csv'.format(time.time()), mode='w')
