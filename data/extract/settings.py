import os
import json

file_path = os.path.abspath(os.path.dirname(__file__))
config_file = os.path.join(file_path, 'config.json')
with open(config_file, 'r') as f:
    config = json.load(f)

# Third Party Api settings
data_go_kr_service_key = config['THIRD_PARTY_API']['DATA_GO_KR']['SERVICE_KEY']

# Crawler settings
webdriver = config['CRAWLING']['SELENIUM']['WEB_DRIVER']
