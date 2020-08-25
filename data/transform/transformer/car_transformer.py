import sys
sys.path.append('..')
import settings
sys.path.append(settings.BASE_DIR)

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
        pass

    def check_exceptions(self, type, old, **kargs):
        if type == 'manufacturer':
            if old == '한불모터스':
                if kargs['model'] in ['e-208', 'e-2008']:
                    return '푸조'
                else:
                    return 'DS'
            else:
                return False
        elif type == 'trim':
            exceptions = ['재규어', 'Peugeot']
            for e in exceptions:
                if e in old:
                    return True
                else:
                    continue
            return False
        else:
            pass

    def transform_to_standard(self, type, old, **kargs):
        st = Standard()
        st_type = getattr(st, type)
        for _list in st_type:
            for _str in _list:
                if _str in old:
                    new = self.check_exceptions(type, old, **kargs)
                    if new:
                        return new
                    else:
                        return _list[0]
        return old

    def get_trim(self, old_model, new_model):
        if '(' in old_model:
            start_idx = old_model.find('(')
            end_idx = old_model.find(')')
            return old_model[start_idx+1:end_idx].strip()
        elif self.check_exceptions('trim', old_model):
            return ''
        else:
            st_model_list = Standard().model
            for st_model in st_model_list:
                for m in st_model:
                    if m in old_model:
                        return old_model.replace(m, '').strip()

    def regstatus(self):
        pass
