# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 18:28:16 2022

@author: sunil
"""

import pandas as pd
temperature_df= pd.DataFrame({'city':["mumbai","dehli","bangalore"],
                             'temperature':[38,40,21]
    })

windspeed_df=pd.DataFrame({'city':["mumbai","dehli","bangalore"],
                             'windspeed':[6,4,5]
    })

new_df=pd.concat([temperature_df, windspeed_df], axis=1)

##################### Merge data frame #########

df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})

df3=pd.merge(df1, df2, on='city' )


df4 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35, 38],
})

df5 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "humidity": [65,68,71],
})


df6=pd.merge(df4,df5, on='city', how='inner')

df7=pd.merge(df4,df5, on='city', how='left')

df8=pd.merge(df4,df5, on='city', how='right')

df9=pd.merge(df4,df5, on='city', how='outer', indicator=True)

