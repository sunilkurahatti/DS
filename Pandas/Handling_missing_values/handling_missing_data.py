# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 08:07:41 2022

@author: sunil

topic: Handling missing data
"""
import pandas as pd
df=pd.read_csv("weather_data.csv", parse_dates=['day'])
df1=pd.read_csv("weather_data.csv", parse_dates=['day'])
#df1.temperature.fillna(method="ffill")

df.iloc[0:,0:2].interpolate(method="time")
df1=df.iloc[0:,0,1].interpolate(method="time")
df1.iloc[0:,[0,1]].interpolate()

df3=df[['temperature']].interpolate(),df[['windspeed']].interpolate(),df[['event']]

df.set_index('day', inplace=True)

new_df=df.fillna('0')

new_df=df.fillna({
    'temperature': '0',
    'windspeed':0,
    'event':'no event'
    })


new_df=df.fillna(method="ffill")

new_df=df.fillna(method="bfill")

new_df=df.dropna(how="all")

new_df=df.interpolate(method='time')

dt=pd.date_range(start='2017-01-01',end='2017-01-11')
idx=pd.DatetimeIndex(dt)
df=df.reindex(idx)

df[['temperature','windspeed']]=df.iloc[0:,0:2].interpolate(method="time")




