# -*- coding: utf-8 -*-
"""
Lesson 6

Let's take a look at the groupby function
"""

from pandas import DataFrame
import pandas as pd

d = {'one':[1,1,1,1,1],
     'two':[2,2,2,2,2],
     'letter':['a','a','b','b','c']}
    
# Create dataframe
df = DataFrame(d)
df

# Create group object
one = df.groupby('letter')

# Apply sum function
one.sum()

letterone = df.groupby(['letter','one']).sum()
letterone

letterone.index

# You may not want the columns you are grouping by become your index, this can easily be achieved as shown below
letterone = df.groupby(['letter','one'], as_index=False).sum()
letterone

letterone.index