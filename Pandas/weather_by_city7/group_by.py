# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 13:06:11 2022

@author: sunil
"""

import pandas as pd

df=pd.read_csv("weather_by_city.csv")
gp=df.groupby('city')

for city, city_df in gp:
    print(city)
    print(city_df)
    
mumbai=gp.get_group('mumbai')

c_max=gp.max()
c_mean=gp.mean()
c_desc=gp.describe()