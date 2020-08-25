import sys
import json
sys.path.append('..')
import settings
sys.path.append(settings.BASE_DIR)
from data.db import redis_module
from transformer import car_transformer

def encar(extract_json_data):
    tf = car_transformer.CarTransformer()
    extract_dict_data = json.loads(extract_json_data)
    new_data = []
    for d in extract_dict_data:
        new_manufacturer = tf.transform_to_standard(
            type='manufacturer', old=d['manufacturer'], model=d['model'])
        new_model = tf.transform_to_standard(
            type='model', old=d['model'])
        new_trim = d['trim'].strip()
        new_year = d['year'].replace('/', '년').replace('식', '월')
        new_km = d['km'].replace(',', '').replace('km', '')
        new_dict = {
            'manufacturer' : new_manufacturer,
            'model' : new_model,
            'trim' : new_trim,
            'year' : new_year,
            'km' : new_km,
            'location' : d['location']
        }
        new_data.append(new_dict)
    new_json_data = json.dumps(new_data, ensure_ascii=False)
    return new_json_data

r = redis_module.RedisModule()
extract_json_data = r.get('extract_encar')
transform_json_data = encar(extract_json_data)

key = 'transform_encar'
if r.set(key, transform_json_data):
    print('Redis saved key [{}]'.format(key))
