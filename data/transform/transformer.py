import sys
import json
sys.path.append('..')
import settings
sys.path.append(settings.BASE_DIR)
from data.db import redis_module

class Manufacturer():
    manufacturer = [
        ['현대자동차', '현대'],
        ['기아자동차', '기아'],
        ['르노삼성'],
        ['BMW', '비엠더블유코리아'],
        ['쉐보레', '한국지엠'],
        ['닛산', '한국닛산'],
        ['테슬라'],
        ['재규어', '재규어랜드로버코리아'],
        ['벤츠'],
        ['푸조', '한불모터스'],
        ['대창모터스'],
        ['캠시스'],
    ]

class Transformer():
    def __init__(self):
        self.r = redis_module.RedisModule()

    def transform_manufacturer(self, old):
        mf = Manufacturer()
        for m in mf.manufacturer:
            if old in m:
                return m[0]
        return old

    def encar(self):
        value = self.r.get('encar').decode('utf-8')


    def evorkr(self):
        json_data = self.r.get('evorkr').decode('utf-8')
        dict_data = json.loads(json_data)
        new_data = []
        for d in dict_data:
            print(d['manufacturer'])
            new_manufacturer = self.transform_manufacturer(d['manufacturer'])
            new_dict = {
                'manufacturer' : new_manufacturer,
                'model' : d['model'],
                'trim' : 'trim',
                'support_amount' : d['support_amount']
            }
            new_data.append(new_dict)
        new_json_data = json.dumps(new_data, ensure_ascii=False)
        self.r.set('transform_evorkr', new_json_data)
        print(new_json_data)

    def regstatus(self):
        pass

tr = Transformer()
tr.evorkr()
