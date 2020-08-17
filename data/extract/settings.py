import os
import json

file_path = os.path.abspath(os.path.dirname(__file__))
config_file = os.path.join(file_path, 'config.json')
with open(config_file, 'r') as f:
    config = json.load(f)

# Common
base_dir = config['COMMON']['DIR']['BASE']
input_dir = os.path.join(base_dir, config['COMMON']['DIR']['INPUT'])
output_csv_dir = os.path.join(base_dir, config['COMMON']['DIR']['OUTPUT']['CSV'])
output_xml_dir = os.path.join(base_dir, config['COMMON']['DIR']['OUTPUT']['XML'])

# DB
redis_host = config['COMMON']['DB']['REDIS']['HOST']
redis_port = config['COMMON']['DB']['REDIS']['PORT']

# Third Party Api settings
data_go_kr_service_key = config['THIRD_PARTY_API']['DATA_GO_KR']['SERVICE_KEY']

# Crawler settings
webdriver = os.path.join(base_dir, config['CRAWLING']['SELENIUM']['WEB_DRIVER'])
