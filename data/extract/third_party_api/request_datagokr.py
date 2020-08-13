import time
import xml.etree.ElementTree as ET
from apis import DataGoKr

datagokr = DataGoKr()
res = datagokr.get_charging_station(1, 5, '')

if res.status_code != 200:
    raise Exception('data.go.kr has a problem. status_code [{}]'.format(res.status_code))

root = ET.fromstring(res.text)
result_code = root.find('header').find('resultCode').text
if result_code != '00':
    result_msg = root.find('header').find('resultMsg').text
    raise Exception('result_code error [{}][{}]'.format(result_code, result_msg))

tree = ET.ElementTree(root)
tree.write('../../files/xml/charging_station_{}.xml'.format(time.time()))
