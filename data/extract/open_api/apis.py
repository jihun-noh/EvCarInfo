import sys
import requests
sys.path.append('..')
import settings

class DataGoKr():
    def __init__(self):
        self.service_key = settings.data_go_kr_service_key

    def get_charging_station(self, page, row, addr=None):
        params = {
            'serviceKey' : self.service_key,
            'pageNo' : page,
            'numOfRows' : row,
            'addr' : addr,
        }
        url = 'http://openapi.kepco.co.kr/service/EvInfoServiceV2/getEvSearchList'
        res = requests.get(url, params=params)
        return res
