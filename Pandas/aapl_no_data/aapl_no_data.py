# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 12:48:11 2022

@author: sunil
"""

import pandas as pd

df=pd.read_csv("aapl_no_data.csv")

rng=pd.date_range(start="6/1/2017", end="6/30/2017", freq='B')

df.set_index(rng, inplace=True)

df_week_end_include=df.asfreq(freq='D', method='pad')

rng1=pd.date_range(start="6/1/2017",periods=72, freq='B')

import numpy as np
rand=np.random.randint(1,10, len(rng1)) 
ts=pd.Series(np.random.randint(1,10, len(rng1)), index=rng1)
ts.asof(where='2017-06-07')
df.Close.mean()