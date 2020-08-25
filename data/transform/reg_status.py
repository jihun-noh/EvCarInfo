import sys
import json
sys.path.append('..')
import settings
sys.path.append(settings.BASE_DIR)
from data.db import redis_module

r = redis_module.RedisModule()
pattern = 'extract_reg_status_fuel*'
keys = r.keys(pattern)
dict_datas = []
if not keys:
    print('Redis key is not exist [{}]'.format(pattern))
    sys.exit()

keys.sort()
for k in keys:
    key = k[k.find('2'):]
    dict_data = {key : r.get(k)}
    dict_datas.append(dict_data)

transform_json_data = json.dumps(dict_datas)
new_key = 'transform_reg_status_fuel'
if r.set(new_key, transform_json_data):
    print('Redis saved key [{}]'.format(new_key))
