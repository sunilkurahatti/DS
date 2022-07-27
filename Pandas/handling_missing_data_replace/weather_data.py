# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 16:36:33 2022

@author: sunil
"""
import pandas as pd
import numpy as np

df=pd.read_csv("weather_data.csv", parse_dates=['day'])

new_df=df.replace([-99999,-88888],np.NaN)

new_df1=df.replace({'temperature': -99999,
                    'windspeed': -99999,
                    'event': '0'}, np.NaN)

new_df1.set_index('day', inplace= True)

new_df1[['temperature','windspeed']]=new_df1.iloc[0:,0:2].interpolate()
new_df1[['event']]=new_df1[['event']].fillna(method='ffill')

new_df1.to_csv("Cleansed_data.csv")