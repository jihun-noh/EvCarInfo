import json

with open('config.json', 'r') as f:
    config = json.load(f)

# Third Party Api settings
data_go_kr_sercret_key = config['THIRD_PARTY_API']['DATA_GO_KR']['SERVICE_KEY']

# Crawler settings
webdriver = config['CRAWLING']['SELENIUM']['WEB_DRIVER']
