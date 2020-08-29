import sys
import json
sys.path.append('..')
import settings
sys.path.append(settings.BASE_DIR)
from data.db import redis_module

r = redis_module.RedisModule()
pattern = 'extract_charging_station*'
keys = r.keys(pattern)
extract_dict_datas = []
if not keys:
    print('Redis key is not exist [{}]'.format(pattern))
    sys.exit()

for k in keys:
    dict_data = json.loads(r.get(k))
    items = dict_data['response']['body']['items']['item']
    extract_dict_datas.extend(items)

transform_json_data = json.dumps(extract_dict_datas, ensure_ascii=False)
key = 'transform_charging_station'
if r.set(key, transform_json_data):
    print('Redis saved key [{}]'.format(key))
