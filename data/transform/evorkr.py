import sys
import json
sys.path.append('..')
import settings
sys.path.append(settings.BASE_DIR)
from data.db import redis_module
from transformer import evcar_transformer

def evorkr(extract_json_data):
    tf = evcar_transformer.Transformer()
    extract_dict_data = json.loads(extract_json_data)
    new_data = []
    for d in extract_dict_data:
        new_manufacturer = tf.transform_to_standard(
            type='manufacturer', old=d['manufacturer'], model=d['model'])
        new_model = tf.transform_to_standard(
            type='model', old=d['model'])
        new_trim = tf.get_trim(d['model'], new_model)
        new_dict = {
            'manufacturer' : new_manufacturer,
            'model' : new_model,
            'trim' : new_trim,
            'support_amount' : d['support_amount']
        }
        new_data.append(new_dict)
    new_json_data = json.dumps(new_data, ensure_ascii=False)
    return new_json_data

r = redis_module.RedisModule()
extract_json_data = r.get('extract_evorkr').decode('utf-8')
transform_json_data = evorkr(extract_json_data)

key = 'transform_evorkr'
if r.set(key, transform_json_data):
    print('Redis saved key [{}]'.format(key))
