import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import seaborn as sns
import time
import warnings
warnings.filterwarnings('ignore')

global_temp_country = pd.read_csv('C:\\Users\\alish\\PycharmProjects\\pythonProject\\climate global\\.csv files\\GlobalLandTemperaturesByCountry.csv') #change the path to your own
global_temp_country_clear = global_temp_country[~global_temp_country['Country'].isin(
    ['Denmark', 'Antarctica', 'France', 'Europe', 'Netherlands',
     'United Kingdom', 'Africa', 'South America'])]

global_temp_country_clear = global_temp_country_clear.replace(
    ['Denmark (Europe)', 'France (Europe)', 'Netherlands (Europe)', 'United Kingdom (Europe)'],
    ['Denmark', 'France', 'Netherlands', 'United Kingdom'])

# Let's average temperature for each country

countries = np.unique(global_temp_country_clear['Country'])
mean_temp = []
for country in countries:
    mean_temp.append(global_temp_country_clear[global_temp_country_clear['Country'] ==
                                               country]['AverageTemperature'].mean())

data = [dict(
    type='choropleth',
    locations=countries,
    z=mean_temp,
    locationmode='country names',
    text=countries,
    marker=dict(
        line=dict(color='rgb(0,0,0)', width=1)),
    colorbar=dict(autotick=True, tickprefix='',
                  title='# Average\nTemperature,\n°C')
)
]

layout = dict(
    title='Average land temperature in countries',
    geo=dict(
        showframe=False,
        showocean=True,
        oceancolor='rgb(0,255,255)',
        projection=dict(
            type='orthographic',
            rotation=dict(
                lon=60,
                lat=10),
        ),
        lonaxis=dict(
            showgrid=True,
            gridcolor='rgb(102, 102, 102)'
        ),
        lataxis=dict(
            showgrid=True,
            gridcolor='rgb(102, 102, 102)'
        )
    ),
)

fig = dict(data=data, layout=layout)
py.iplot(fig, validate=False, filename='worldmap')
