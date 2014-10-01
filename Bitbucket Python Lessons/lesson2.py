# -*- coding: utf-8 -*-
# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library:
##from (library) import (specific library function)
from pandas import DataFrame, read_csv
from numpy import random

# General syntax to import a library but no functions:
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd
import sys # only needed to determine Python version number

print 'Python version ' + sys.version
print 'Pandas version ' + pd.__version__

'''
CREATE DATA
The data set will consist of 1,000 baby names and the number of births recorded for that year (1880).
We will also add plenty of duplicates so you will see the same baby name more than once.
We will start by creating the random set of baby names.
'''
# The initial set of baby names
names = ['Bob','Jessica','Mary','John','Mel']

'''
This will ensure the random samples below can be reproduced.
This means the random samples will always be identical
'''
#random.seed?

'''
randint(low, high=None, size=None)
Return random integers from 'low' (inclusive) to 'high' (exclusive).
'''
#random.randint?

'''
len(object) -> integer
Return the number of items of a sequence or mapping.
'''
#len?

'''
range([start,] stop[, step]) -> list of integers
Return a list containing an arithmetic progression of integers.
'''
#range?

'''
zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]
Return a list of tuples, where each tuple contains the i-th element
from each of the argument sequences.  The returned list is truncated
in length to the length of the shortest argument sequence.
'''
#zip?

'''
seed(500)                       => Create seed
randint(low=0,high=len(names))  => Generate a random integer between zero and the length of the list "names".
names[n]                        => Select the name where its index is equal to n.
for i in range(n)               => Loop until i is equal to n, i.e. 1,2,3,....n.
random_names                    => Select a random name from the name list and do this n times.
'''

random.seed(500)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]

print random_names[:10]

# The number of births per name for the year 1880
births = [random.randint(low=0,high=1000) for i in range(1000)]
print births[:10]

# Merge the names and the births data set using the zip function
BabyDataSet = zip(random_names,births)
print BabyDataSet[:10]

'''
We are basically done creating this data set. We will now use the pandas library to export this data set into a csv file
df will be a DataFrame object. You can think of this object holding the contents of the BabyDataSet in a format similar
to a sql table or an excel spreadsheet. Let's take a look below at the contents inside df
'''
df = DataFrame(data = BabyDataSet, columns=['Names','Births'])
df[:10]

'''
df.to_csv(self, path_or_buf, sep=',', na_rep='', float_format=None, cols=None, header=True, index=True, index_label=None, mode='w', nanRep=None, encoding=None, quoting=None, line_terminator='\n')
Write DataFrame to a comma-separated values (csv) file
'''
#df.to_csv?

df.to_csv('births1880.txt',index=False,header=False)

Location = r'C:\Users\ABaker\Documents\Python Scripts\Bitbucket Python Lessons\births1880.txt'
df = read_csv(Location)

df.info()

df.head()

df = read_csv(Location, header=None)
df.info()

df.tail()

df = read_csv(Location, names=['Names','Births'])
df.head(5)

import os
os.remove(Location)

'''
PREPARE DATA
The data we have consists of baby names and the number of births in the year 1880.
We already know that we have 1,000 records and none of the records are missing (non-null values).
We can verify the "Names" column still only has five unique names.
We can use the unique property of the dataframe to find all the unique records of the "Names" column.
'''

# Method 1:
df['Names'].unique()

# If you actually want to print the unique values:
for x in df['Names'].unique():
    print x
    
# Method 2:
print df['Names'].describe()

'''
Since we have multiple values per baby name, we need to aggregate this data so we only have a baby name
appear once. This means the 1000 rows will need to become 5. We can accomplish this by using the 
groupby function.

df.groupby(self, by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True)
Group series using mapper (dict or key function, apply given function
to group, return result as series) or by a series of columns

'''
#df.groupby?

# Create a groupby object
Name = df.groupby('Names')

# Apply the sum function to the groupby object
df = Name.sum()
df

'''
ANALYSE DATA
To find the most popular name or the baby name with the highest birth rate, we can do one of the following
- Sort the dataframe and select the top row
- Use the max() attribute to find the maximum value
'''

# Method 1
Sorted = df.sort(['Births'], ascending=[0])
Sorted.head(1)

# Method 2
df['Births'].max()

'''
PRESENT DATA
Here we can plot the Births column and label the graph to show the end user the highest point on the graph.
In conjunction with the table, the end user has a clear picture that Bob (?) is the most popular name in the data set
'''

# Create graph
df['Births'].plot(kind='bar')

print "The most popular name"
df.sort(columns = 'Births', ascending = False)