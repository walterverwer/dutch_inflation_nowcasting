import os
import pandas as pd
import numpy as np

from datetime import date
from pandas.tseries.offsets import DateOffset


#%% - Data cleaning

DATA = 'cpi_mm.csv'
path = os.path.join('.', 'data', DATA)
df = pd.read_csv(path, sep=';')

# Setting the correct date
'''
For setting correct date:
    De nieuwe cijfers worden doorgaans op de eerste donderdag van de maand gepubliceerd.
    Tenzij de eerste donderdag op de eerste, tweede of derde dag van de maand valt of er
    feestdagen vlak voor of op deze donderdag vallen. Dan worden de nieuwe cijfers de
    dinsdag daarna gepubliceerd.
    
    To do:
        1. Check what day of the month it is for every day in time.
        2. Publication Thursday should be at least the 4th day of the month, 
           which cannot be a holiday, e.g. 4th of may.
        3. If Thursday is on the 1st, 2nd, 3th day or falls on a holiday,
           then the publication day will be 5 days later, on a Tuesday 
           (check whether this is true!). E.g. Thursday the 1st -> Tuesday the 6th.
        4. For every date in time the above needs to hold.
'''

# Set perioden to time
df['Time'] = df['Perioden'].str.replace('MM','-')

# Time starting at the first of the month:
df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m')

# Create temp day frame, which contains weekday number based on df['Time']
df['Day'] = df['Time'].apply(date.isoweekday)


'''
- if thursday falls on any of the unallowed days:
    df['Time'] + DateOffset(days=5), for df['Time'] which cannot be a
    publication day.
'''
