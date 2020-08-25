import sys
import requests
import settings

class DataGoKr():
    def __init__(self):
        self.service_key = settings.DATA_GO_KR_SERVICE_KEY

    def get_charging_station(self, page_no, page_size):
        params = {
            'serviceKey' : self.service_key,
            'pageNo' : page_no,
            'pageSize' : page_size,
        }
        url = 'http://open.ev.or.kr:8080/openapi/services/EvCharger/getChargerInfo'
        res = requests.get(url, params=params)
        return res
