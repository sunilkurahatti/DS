# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 16:54:22 2022

@author: sunil
"""
import pandas as pd

df=pd.read_csv("aapl_no_data.csv")


rng=pd.date_range(start="7/1/2022",end="7/31/2022", freq='B')

from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

CBD=CustomBusinessDay(calendar=USFederalHolidayCalendar())

rng=pd.date_range(start="7/1/2022",end="7/31/2022", freq=CBD)

################# Custom birthday as holiday  and weekmask ##################

from  pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday


class my_birth_day(AbstractHolidayCalendar):

    rules = [
        Holiday("Sunil birth day", month=7, day=20, observance=nearest_workday),]
    
my_b_d=CustomBusinessDay(weekmask = 'Mon Tue Wed Thu', calendar=my_birth_day())

rng=pd.date_range(start="7/1/2022",end="7/31/2022", freq=my_b_d)


############### Pandas to_date ###################################

import pandas as pd



dates = ['2017-01-05 1:30:00', 'Jan 5, 2017 14:30:00', '01/05/2017', '2017.01.05', '2017/01/05','20170105']

pd_t_d=pd.to_datetime(dates, errors='coerce')

dates = ['2017-01-05 1:30:00', 'Jan 5, 2017 14:30:00', '01/05/2017', '2017.01.05', '2017/01/05','20170105','abc']

pd_t_d=pd.to_datetime(dates, errors='coerce')
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         