import os
import sys
import datetime
import json
import pandas as pd
sys.path.append('../..')
import settings
sys.path.append(settings.BASE_DIR)
from data.db import redis_module

def registration_status_fuel(filename):
    excel = pd.ExcelFile(filename)
    for sheet in excel.sheet_names:
        if '연료별_등록현황' in sheet:
            fuel_sheet = sheet
    data = pd.read_excel(excel, sheet_name=fuel_sheet)
    df = pd.DataFrame(data)
    year_month = str(df.iat[0, 1]).replace('.', '_')

    df_gasoline = df.loc[3:19]
    df_diesel = df.loc[20:36]
    df_electric = df.loc[71:87]

    total_gasoline = df_gasoline.loc[19][20]
    total_diesel = df_diesel.loc[36][20]
    total_electric = df_electric.loc[87][20]

    key = '{}_total_reg_status_fuel'.format(year_month)
    value = json.dumps({
        'gasoline' : total_gasoline,
        'diesel' : total_diesel,
        'electric' : total_electric
    })
    print(key, value)
    r = redis_module.RedisModule()
    if r.set(key, value):
        print('Redis saved key [{}]'.format(key))

for file in os.listdir(settings.INPUT_DIR):
    if '자동차_등록자료_통계' or '자동차 등록자료 통계' in file:
        mtime = os.path.getmtime(os.path.join(settings.INPUT_DIR, file))
        mdate = datetime.date.fromtimestamp(mtime)
        today = datetime.date.today()
        if mdate == today:
            print(file)
            registration_status_fuel(os.path.join(settings.INPUT_DIR, file))
