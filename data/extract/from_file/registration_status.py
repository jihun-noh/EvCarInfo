import os
import sys
import pandas as pd
sys.path.append('..')
import settings

def registration_status(filename):
    excel = pd.ExcelFile(filename)
    for sheet in excel.sheet_names:
        if '연료별_등록현황' in sheet:
            fuel_sheet = sheet
    data = pd.read_excel(excel, sheet_name=fuel_sheet)
    df = pd.DataFrame(data)
    year_month = df.iat[0, 1].replace('.', '_')

    df_gasoline = df.loc[3:19]
    df_diesel = df.loc[20:36]
    df_electric = df.loc[71:87]

    df_gasoline.to_csv(os.path.join(settings.output_csv_dir, year_month + '_registration_gasoline.csv'), mode='w')
    df_diesel.to_csv(os.path.join(settings.output_csv_dir, year_month + '_registration_diesel.csv'), mode='w')
    df_electric.to_csv(os.path.join(settings.output_csv_dir, year_month + '_registration_electric.csv'), mode='w')

for file in os.listdir(settings.input_dir):
    if '자동차_등록자료_통계' in file:
        registration_status(os.path.join(settings.input_dir, file))
