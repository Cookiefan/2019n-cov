import numpy as npy
import pandas as pds
from matplotlib import pyplot as plt
from datetime import datetime
from pathlib import Path


def get_data(key='wuhan', start_date='2020/1/20', end_date='2020/02/11'):
    assert key in ['guangdong', 'hubei', 'nation', 'shenzhen', 'wuhan']
    file = f'ncov/data/key/{key}.csv'
    data = pds.read_csv(file, parse_dates=['time'])
    # if city != '':
    #     assert city in data['city'].unique()
    #     data = data[data['city'] == city]
    start_date = datetime.strptime(start_date, '%Y/%m/%d')
    end_date = datetime.strptime(end_date, '%Y/%m/%d')
    data = data[(start_date <= data['time']) & (data['time'] <= end_date)]
    data = data.reset_index(drop=True)
    return data


def watch_data(key='wuhan', start_date='2020/01/10', end_date='2020/02/11'):
    assert key in ['guangdong', 'hubei', 'nation', 'shenzhen', 'wuhan']
    file = f'ncov/data/key/{key}.csv'
    data = pds.read_csv(file, parse_dates=['time'])
    # if city != '':
    #     assert city in data['city'].unique()
    #     data = data[data['city'] == city]
    start_date = datetime.strptime(start_date, '%Y/%m/%d')
    end_date = datetime.strptime(end_date, '%Y/%m/%d')
    data = data[(start_date <= data['time']) & (data['time'] <= end_date)]
    data = data.reset_index(drop=True)
    plt.plot(data['time'].values,
             data['dead'],
             color='red',
             marker='.',
             label="dead")
    plt.plot(data['time'].values,
             data['confirmed'],
             color='yellow',
             marker='.',
             label="confirmed")
    plt.plot(data['time'].values,
             data['suspected'],
             color='blue',
             marker='.',
             label="suspected")
    plt.plot(data['time'].values,
             data['cured'],
             color='green',
             marker='.',
             label="cured")
    plt.xlabel("day")
    plt.ylabel("number")
    plt.legend()
    plt.show()
    return data
