# -*- coding: utf-8 -*-
"""
Lesson 4

Back to Basics! Working with a small data set in order to understand what's going on
- Adding columns
- Deleting columns
- Slicing the data in different ways
"""

# Import libraries
from pandas import DataFrame
import pandas as pd
import sys

print 'Python version ' + sys.version
print 'Pandas version ' + pd.__version__

# Small data set
d = [0,1,2,3,4,5,6,7,8,9]

# Create a dataframe
df = DataFrame(d)

# Let's change the name of the column
df.columns = ['Rev']

# Let's add a new column
df['NewCol'] = 5
df

# Let's modify our new column
df['NewCol'] = df['NewCol'] + 1
df

# We can delete columns
del df['NewCol']
df

# Let's add a couple of columns
df['test'] = 3
df['col'] = df['Rev']
df

# If we wanted to we could change the name of the index
i = ['a','b','c','d','e','f','g','h','i','j']
df.index = i
df

'''
We can now start to select pieces of the dataframe using 'loc'
Note: 'loc' is strictly label based.
'''

df.loc['a']

# df.loc[inclusive:inclusive]
df.loc['a':'d']

# df.iloc[inclusive:exclusive]
# Note: .iloc is strictly integer position based
df.iloc[0:3]

# We can also select using the column name
df['Rev']
df[['Rev','test']]

# df['ColumnName'][inclusive:exclusive]
df['Rev'][0:3]

df['col'][5:]

df[['col', 'test']][:3]

'''
There is also a handy function to select the top and bottom records of a dataframe
'''
# Select top N number of records (default = 5)
df.head()

# Select bottom N number of records (default = 5)
df.tail()








