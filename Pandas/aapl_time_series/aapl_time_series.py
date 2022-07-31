# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:45:12 2022

@author: sunil
"""
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("aapl.csv", parse_dates=['Date'],index_col="Date")

df_may=df["2017-05"]
df['2017-05'].Close.mean()
df['2017-06'].Close.mean()

df_range=df['2017-05-01':'2017-06-30']

df_resample=df['Close'].resample('M').max().plot(kind='bar')

for i in df_resample:
    print(i)