import os
import sys
import time
import json
import xmltodict
sys.path.append('../..')
import settings
sys.path.append(settings.BASE_DIR)
from apis import DataGoKr
from data.db import redis_module

def request_charging_station(page_no, page_size):
    datagokr = DataGoKr()
    res = datagokr.get_charging_station(page_no, page_size)
    if res.status_code != 200:
        raise Exception('data.go.kr has a problem. status_code [{}]'.format(res.status_code))

    dict_data = xmltodict.parse(res.text)
    result_code = dict_data['response']['header']['resultCode']
    if result_code != '00':
         result_msg = dict_data['response']['header']['resultMsg']
         raise Exception('result_code error [{}][{}]'.format(result_code, result_msg))

    return dict_data

r = redis_module.RedisModule()
pre_dict_data = request_charging_station(1, 1)
total_count = pre_dict_data['response']['header']['totalCount']
total_page = int(int(total_count) / 10000) + 1
print('total_page - [{}]'.format(total_page))

for i in range(1, total_page+1):
    print('page - [{}]'.format(i))
    dict_data = request_charging_station(i, 10000)
    json_data = json.dumps(dict_data, ensure_ascii=False)

    key = 'extract_chargingstation_{}'.format(i)
    if r.set(key, json_data):
        print('Redis saved key [{}]'.format(key))
