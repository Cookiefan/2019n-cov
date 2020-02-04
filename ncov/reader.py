import numpy as npy
import pandas as pds
from matplotlib import pyplot as plt
from datetime import datetime
from pathlib import Path

str_province = ['湖北', '广东']


def get_data(province='湖北',
             city='武汉',
             start_date='2020-01-10',
             end_date='2020-02-03'):
    assert province in str_province
    if province == str_province[0]:
        file = f'{Path().resolve()}/ncov/data/hubei/hubei.csv'
    else:
        file = f'{Path().resolve()}/ncov/data/guangdong/guangdong.csv'
    data = pds.read_csv(file, parse_dates=['time'])
    assert city in data['city'].unique()
    data = data[data['city'] == city]
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    data = data[(start_date <= data['time']) & (data['time'] <= end_date)]
    return data.reset_index(drop=True)