import sys
import json
sys.path.append('..')
import settings
sys.path.append(settings.BASE_DIR)
from data.db import redis_module

class Standard():
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
        ['DS', '한불모터스'],
        ['대창모터스'],
        ['캠시스'],
    ]
    model = [
        ['아이오닉 일렉트릭', '아이오닉 전기차'],
        ['코나 일렉트릭', '코나'],
        ['니로 EV', '니로EV'],
        ['쏘울 EV', '쏘울 전기차', '쏘울 부스터 EV'],
        ['SM3 Z.E.', 'SM3 Z.E'],
        ['조에', 'ZOE'],
        ['i3'],
        ['볼트 EV', 'BOLT EV'],
        ['리프', 'LEAF', '리프 (ZE1)'],
        ['모델 3', 'Model 3'],
        ['모델 S', 'Model S'],
        ['I-PACE', '재규어 I-PACE'],
        ['EQC', 'EQC N293'],
        ['e-208', 'Peugeot e-208'],
        ['e-2008', 'Peugeot e-2008 SUV'],
        ['DS3 Crossback E-tense'],
        ['트위지', 'TWIZY'],
        ['다니고', 'Danigo'],
        ['CEVO-C']
    ]

class Transformer():
    def __init__(self):
        self.r = redis_module.RedisModule()

    def check_exceptions(self, type, old, list, **kargs):
        if type == 'manufacturer':
            if old == '한불모터스':
                if kargs['model'] in ['e-208', 'e-2008']:
                    return '푸조'
                else:
                    return 'DS'
            else:
                return False
        else:
            pass

    def transform_to_standard(self, type, old, **kargs):
        st = Standard()
        standard = getattr(st, type)
        for _list in standard:
            for _str in _list:
                if _str in old:
                    if type == 'model':
                        print(old.replace(_str, ''))
                    new = self.check_exceptions(type, old, _list, **kargs)
                    if new:
                        return new
                    else:
                        return _list[0]
        return old

    def get_trim(self, model, new_model):
        if '(' in model:
            start_idx = model.find('(')
            end_idx = model.find(')')
            return model[start_idx+1:end_idx]
        # elif 띄어쓰기:
        #     trim =
        # else:
        #     trim =
        return 'trim'

    def encar(self):
        value = self.r.get('extract_encar').decode('utf-8')

    def evorkr(self):
        json_data = self.r.get('extract_evorkr').decode('utf-8')
        dict_data = json.loads(json_data)
        new_data = []
        for d in dict_data:
            new_manufacturer = self.transform_to_standard(
                type='manufacturer', old=d['manufacturer'], model=d['model'])
            new_model = self.transform_to_standard(
                type='model', old=d['model'])
            new_trim = self.get_trim(d['model'], new_model)
            new_dict = {
                'manufacturer' : new_manufacturer,
                'model' : new_model,
                'trim' : new_trim,
                'support_amount' : d['support_amount']
            }
            new_data.append(new_dict)
        new_json_data = json.dumps(new_data, ensure_ascii=False)
#        self.r.set('transform_evorkr', new_json_data)
        print(new_json_data)

    def regstatus(self):
        pass

tr = Transformer()
tr.evorkr()
