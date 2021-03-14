import numpy as np
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import scipy.stats as stats
from datetime import datetime
import gc
import seaborn as sns

# sns.set(style="darkgrid")
# sns.set_color_codes("pastel")
gc.enable()
from statsmodels.tsa.seasonal import seasonal_decompose


def datetime(x):
    return np.array(x, dtype=np.datetime64)


def runmean(x, N):
    return np.convolve(x, np.ones((N,)) / N, mode='valid')


np.warnings.filterwarnings('ignore')


def plots_stats(df, city="Hanoi"):
    df['AverageTemperature'].fillna(df.AverageTemperature.mean(), inplace=True)

    df_1800 = df[(datetime(df.dt) > datetime('1810-01-01')) & (datetime(df.dt) < datetime('1910-01-01'))]
    df_1900 = df[(datetime(df.dt) > datetime('1910-01-01')) & (datetime(df.dt) < datetime('2010-01-01'))]
    x_1800_1 = df_1800[df_1800.City == city]
    x_1900_1 = df_1900[df_1900.City == city]
    x_1800 = df_1800[df_1800.City == city].AverageTemperature
    x_1900 = df_1900[df_1900.City == city].AverageTemperature
    plt.subplot(2, 1, 1)
    xx_1800 = seasonal_decompose(x_1800, model='additive', filt=None, period=100)
    plt.plot(datetime(df_1800.dt[xx_1800.trend.index]), xx_1800.trend, color='blue');
    xx_1900 = seasonal_decompose(x_1900, model='additive', filt=None, period=100)
    plt.plot(datetime(df_1900.dt[xx_1900.trend.index]), xx_1900.trend, color='red');
    plt.title('Temperature Trend Shift in ' + city, fontsize=20)
    # plt.legend()
    plt.subplot(2, 1, 2)
    n, x, _ = plt.hist(xx_1800.trend, density=True, alpha=.6, color='blue', label='1810--1910')
    # plt.plot(x, density(x), alpha=.3, color="blue")
    x1 = x[1:]
    # find the mode of the first histogram

    dx = (x1.max() - x1.min()) / 20
    maxx = x1[n == n.max()] - dx
    #
    print(" ------------------------------------------------------------------------------------------- ")

    print(" ------------------------------------------------------------------------------------------- ")
    print("this much of the recent climate is greater than the past climate : ",
          (xx_1900.trend > maxx[0]).sum() / xx_1900.trend.shape[0])
    print(" ------------------------------------------------------------------------------------------- ")

    plt.axvline(x1[n == n.max()] - dx, color='k')
    n, x, _ = plt.hist(xx_1900.trend, density=True, alpha=.6, color='red', label='1910--2010')
    plt.legend()
    plt.xlabel('Temperature Trend in degree Celcius', fontsize=10)
    plt.ylabel('Density', fontsize=10)
    # plt.title(city, fontsize=20)

    plt.show()
glob.glob('./*.csv')
temp_land_cities = pd.read_csv('C:\\Users\\alish\\PycharmProjects\\pythonProject\\climate change global\\Climate_Change_CIties_world-master\\GlobalLandTemperaturesByCity.csv') #change the path to your own
temp_land_cities.head()
