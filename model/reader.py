import numpy as npy
import pandas as pds
from matplotlib import pyplot as plt
file = 'data/hubei/hubei.csv'
data = pds.read_csv(file)
print(data)