# -*- coding: utf-8 -*-
"""
Lesson 7

Outliers
"""

from pandas import DataFrame, date_range, concat
import pandas as pd

# Create a dataframe with dates as your index
States = ['NY', 'NY', 'NY', 'NY', 'FL', 'FL', 'GA', 'GA', 'FL', 'FL']
data = [1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
idx = date_range('1/1/2012', periods=10, freq='MS')
df1 = DataFrame(data, index=idx, columns=['Revenue'])
df1['State'] = States
df1

# Create a second dataframe
data2 = [10.0, 10.0, 9, 9, 8, 8, 7, 7, 6, 6]
idx2 = date_range('1/1/2013', periods=10, freq='MS')
df2 = DataFrame(data2, index=idx2, columns=['Revenue'])
df2['State'] = States
df2

# Combine dataframes
df = concat([df1,df2])
df

'''
Ways to Calculate Outliers

Note: Average and Standard Deviation are only valid for gaussian distributions
'''

# Method 1
df['x-Mean'] = abs(df['Revenue'] - df['Revenue'].mean())
df['1.96*std'] = 1.96*df['Revenue'].std()
df['Outlier'] = abs(df['Revenue'] - df['Revenue'].mean()) > 1.96*df['Revenue'].std()
df

# Reset dataframe to prevent error
df = concat([df1,df2])

# Method 2a - Group by item
State = df.groupby('State')

df['Outlier'] = State.transform( lambda x: abs(x-x.mean()) > 1.96*x.std() )
df['x-Mean'] = State.transform( lambda x: abs(x-x.mean()) )
df['1.96*std'] = State.transform( lambda x: 1.96*x.std() )

# Reset dataframe to prevent error
df = concat([df1,df2])

# Method 2b - Group by multiple items
StateMonth = df.groupby(['State', lambda x: x.month])

df['Outlier'] = StateMonth.transform( lambda x: abs(x-x.mean()) > 1.96*x.std() )
df['x-Mean'] = StateMonth.transform( lambda x: abs(x-x.mean()) )
df['1.96*std'] = StateMonth.transform( lambda x: 1.96*x.std() )
df

df = concat([df1,df2]) #reset dataframe to prevent error

# Method 3a
# Group by item

State = df.groupby('State')

def s(group):
    group['x-Mean'] = abs(group['Revenue'] - group['Revenue'].mean())
    group['1.96*std'] = 1.96*group['Revenue'].std()  
    group['Outlier'] = abs(group['Revenue'] - group['Revenue'].mean()) > 1.96*group['Revenue'].std()
    return group

Newdf = State.apply(s)
Newdf

df = concat([df1,df2]) #reset dataframe to prevent error

# Method 3b
# Group by multiple items

StateMonth = df.groupby(['State', lambda x: x.month])

def s(group):
    group['x-Mean'] = abs(group['Revenue'] - group['Revenue'].mean())
    group['1.96*std'] = 1.96*group['Revenue'].std()  
    group['Outlier'] = abs(group['Revenue'] - group['Revenue'].mean()) > 1.96*group['Revenue'].std()
    return group

Newdf = StateMonth.apply(s)
Newdf

df = concat([df1,df2]) #reset dataframe to prevent error

State = df.groupby('State')

df['Lower'] = State['Revenue'].transform( lambda x: x.quantile(q=.25) - (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
df['Upper'] = State['Revenue'].transform( lambda x: x.quantile(q=.75) + (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
df['Outlier'] = (df['Revenue'] < df['Lower']) | (df['Revenue'] > df['Upper']) 
df
