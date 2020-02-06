import numpy as npy
import pandas as pds
from matplotlib import pyplot as plt
from datetime import datetime
from pathlib import Path

str_province = ['湖北', '广东']


def get_data(province='',
             city='',
             start_date='2020-01-10',
             end_date='2020-02-03'):
    if province == '':
        file = f'{Path().resolve()}/ncov/data/nation/nation.csv'
    elif province == str_province[0]:
        file = f'{Path().resolve()}/ncov/data/hubei/hubei.csv'
    elif province == str_province[1]:
        file = f'{Path().resolve()}/ncov/data/guangdong/guangdong.csv'
    else:
        print("No province match")
        return
    data = pds.read_csv(file, parse_dates=['time'])
    if city != '':
        assert city in data['city'].unique()
        data = data[data['city'] == city]
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    data = data[(start_date <= data['time']) & (data['time'] <= end_date)]
    data = data.reset_index(drop=True)
    return data