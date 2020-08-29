import os
import json

file_path = os.path.abspath(os.path.dirname(__file__))
config_file = os.path.join(file_path, 'config.json')
with open(config_file, 'r') as f:
    config = json.load(f)

# Common
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DIR = os.path.join(BASE_DIR, config['COMMON']['DIR']['INPUT'])

# DB
# Redis
REDIS_HOST = config['DATABASE']['REDIS']['HOST']
REDIS_PORT = config['DATABASE']['REDIS']['PORT']
REDIS_PASSWORD = config['DATABASE']['REDIS']['PASSWORD']
# Postgresql
POSTGRES_HOST = config['DATABASE']['POSTGRESQL']['HOST']
POSTGRES_PORT = config['DATABASE']['POSTGRESQL']['PORT']
POSTGRES_USER = config['DATABASE']['POSTGRESQL']['USER']
POSTGRES_PASSWORD = config['DATABASE']['POSTGRESQL']['PASSWORD']
POSTGRES_DB = config['DATABASE']['POSTGRESQL']['DB']

# Third Party Api settings
DATA_GO_KR_SERVICE_KEY = config['THIRD_PARTY_API']['DATA_GO_KR']['SERVICE_KEY']

# Crawler settings
WEBDRIVER = os.path.join(BASE_DIR, config['CRAWLING']['SELENIUM']['WEB_DRIVER'])
