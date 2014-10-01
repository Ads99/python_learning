# -*- coding: utf-8 -*-

# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library:
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions:
##import (library) as (alias)
import matplotlib.pyplot as plt
import pandas as pd #only needed to determine version number

#Enable inline plotting
#%matplotlib inline

print 'Pandas version ' + pd.__version__

# The initial set of baby names and birth rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

# To merge these two lists together we will use the 'zip' function
'''
zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]
Return a list of tuples, where each tuple contains the i-th element
from each of the argument sequences.  The returned list is truncated
in length to the length of the shortest argument sequence.
'''
#zip?

BabyDataSet = zip(names,births)
print BabyDataSet

# We are basically done creating the data set. We now ill use the pandas library to export this data to a csv file
# df will be a DataFrame object. You can think of this object holding the contents of the BabyDataSet in a format similar
# to a SQL table or an Excel spreadsheet. Let's take a look at the contents of df
df = DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
df

'''
df.to_csv(self, path_or_buf, sep=',', na_rep='', float_format=None, cols=None, header=True, index=True, index_label=None, mode='w', nanRep=None, encoding=None, quoting=None, line_terminator='\n')
Write DataFrame to a comma-separated values (csv) file
'''

#df.to_csv?

df.to_csv('births1880.csv', index=False, header=False)

#read_csv?

Location = r'C:\Users\ABaker\Downloads\Bitbucket Python Lessons\births1880.csv'
df = read_csv(Location)

# The above brings us our first problem of the exercise. The read_csv function treated the first record in the text file
# as the header names. This is obviously incorrect since the text file did not provide us with header names
# To correct this we will pass the header parameter to the read_csv function and set it to None (means null in python)
df = read_csv(Location, header=None)
df

# If we wanted to give the columns specific names, we would have to pass another paramter called names.
# We can also omit the header parameter.
df = read_csv(Location, names=['Names','Births'])
df

import os
os.remove(Location)

# Check data type of the columns
print df.dtypes

# Check data type of Births column
df.Births.dtype

# To find the most popular name or the baby name with the higest birth rate, we can do one of the following.

# Method 1
Sorted = df.sort(['Births'], ascending=[0])
Sorted.head(1)

# Method 2
df['Births'].max()

'''
Here we can plot the Births column and label the graph to show the end user the highest point on the graph.
In conjunction with the table, the end user has a clear picture that Mel is the most popular baby name in the data set.

plot() is a convinient attribute where pandas lets you painlessly plot the data in your dataframe.
We learned how to find the maximum value of the Births column in the previous section.
Now to find the actual baby name of the 973 value looks a bit tricky, so lets go over it.

Explain the pieces:
 df['Names'] - This is the entire list of baby names, the entire Names column
 df['Births'] - This is the entire list of Births in the year 1880, the entire Births column
 df['Births'].max() - This is the maximum value found in the Births column
 
 [df['Births'] == df['Births'].max()] IS EQUAL TO [Find all of the records in the Births column where it is equal to 973]
 df['Names'][df['Births'] == df['Births'].max()] IS EQUAL TO Select all of the records in the Names column WHERE [The Births column is equal to 973]

An alternative way could have been to use the Sorted dataframe:
Sorted['Names'].head(1).value

The str() function simply converts an object into a string.
'''

# Create graph
df['Births'].plot()

# Maximum value in the data set
MaxValue = df['Births'].max()

# Name associated with the max value
MaxName = df['Names'][df['Births'] == df['Births'].max()].values

# Text to display on graph
Text = str(MaxValue) + " - " + MaxName

# Add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points')

print "The most popular name"
df[df['Births'] == df['Births'].max()]
#Sorted.head(1) can also be used