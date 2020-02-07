import numpy as npy
import pandas as pds
from matplotlib import pyplot as plt
from datetime import datetime
from pathlib import Path

str_province = ['湖北', '广东']
cols = [
    'time',
    'city',
    'new_confirmed',
    'new_death',
    'new_recovered',
    'accumulated_confirmed',
    'accumulated_death',
    'accumulated_recovered',
    'new_suspected',
    'accumulated_suspected',
    'accumulated_close_contact',
    'accumulated_quit_medical_observation',
    'under_medical_observation',
]


def get_data(province='',
             city='',
             start_date='2020-01-10',
             end_date='2020-02-03'):
    if province == '':
        file = f'{Path().resolve()}/ncov/data/nation/nation.csv'
    elif city == '':
        file = f'{Path().resolve()}/ncov/data/nation/allcity.csv'
        city = '全省'
    elif province == str_province[0]:
        file = f'{Path().resolve()}/ncov/data/hubei/hubei.csv'
    elif province == str_province[1]:
        file = f'{Path().resolve()}/ncov/data/guangdong/guangdong.csv'
    else:
        file = f'{Path().resolve()}/ncov/data/nation/allcity.csv'
    data = pds.read_csv(file, parse_dates=['time'])
    if city != '':
        assert city in data['city'].unique()
        data = data[data['city'] == city]
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    data = data[(start_date <= data['time']) & (data['time'] <= end_date)]
    data = data.reset_index(drop=True)
    for col in cols:
        if col not in data.columns:
            data[col] = None
    data = data[cols]
    return data


def watch_data(province='',
               city='',
               start_date='2020-01-10',
               end_date='2020-02-05'):
    if province == '':
        file = f'{Path().resolve()}/ncov/data/nation/nation.csv'
    elif city == '':
        file = f'{Path().resolve()}/ncov/data/nation/allcity.csv'
        city = '全省'
    else:
        file = f'{Path().resolve()}/ncov/data/nation/allcity.csv'
    data = pds.read_csv(file, parse_dates=['time'])
    data = data[(data['province'] == province) & (data['city'] == city)]
    plt.xticks(pds.date_range(start_date, end_date), rotation=90)
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    data = data[(start_date <= data['time']) & (data['time'] <= end_date)]
    data = data.reset_index(drop=True)
    plt.plot(data['time'],
             data['accumulated_death'],
             color='red',
             marker='.',
             label="death")
    plt.plot(data['time'],
             data['accumulated_confirmed'],
             color='yellow',
             marker='.',
             label="confirmed")
    plt.plot(data['time'],
             data['accumulated_suspected'],
             color='blue',
             marker='.',
             label="suspected")
    plt.plot(data['time'],
             data['accumulated_recovered'],
             color='green',
             marker='.',
             label="recovered")
    plt.xlabel("day")
    plt.ylabel("number")
    plt.legend()
    plt.show()