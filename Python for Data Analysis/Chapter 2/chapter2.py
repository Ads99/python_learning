# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 16:45:31 2014

@author: ABaker
"""

import json
import os

'''
1. usa.gov data from bit.ly
'''
os.getcwd()
os.chdir('C:\\Users\\ABaker\\Documents\\Python Scripts\\Python for Data Analysis\Chapter 2')
path = 'usagov_bitly_data2012-03-16-1331923249.txt'

open(path).readline()
records = [json.loads(line) for line in open(path)]

records[0]['tz']
print records[0]['tz']

'''
Suppose we were interested in the most often-occurring time zones in the data set (the
tz field). There are many ways we could do this. First, let’s extract a list of time zones
again using a list comprehension:
'''
time_zones = [rec['tz'] for rec in records]

'''
Oops! Turns out that not all of the records have a time zone field. This is easy to handle
as we can add the check if 'tz' in rec at the end of the list comprehension:
'''
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones[:10]

'''
2 ways to do counting
a) the hard way using standard python libraries
b) the easy way using pandas
'''

# a) the hard way
def get_counts(sequence):
    counts = {}
    
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    
    return counts

'''
Or if you know a bit more about the Python standard library, you might prefer to write the same thing more briefly
'''
from collections import defaultdict

def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    
    return counts
    
'''
To use the logic on time zones just pass in the time_zones list
'''
counts = get_counts(time_zones)
counts['Europe/London']
len(counts)
len(time_zones)

'''
If we wanted the top 10 time zones and their counts we have to do a little bit of dictionary acrobatics
'''
def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
    
top_counts(counts)

'''
If you search the Python standard library, you may find the collections.Counter class, which makes this task a lot easier
'''
from collections import Counter

counts = Counter(time_zones)
counts.most_common(10)

'''
Counting Time Zones with pandas
The main pandas data structure is the DataFrame, which you can think of as representing
a table or spreadsheet of data. Creating a DataFrame from the original set of
records is simple:
'''
from pandas import DataFrame, Series

import pandas as pd

frame = DataFrame(records)

frame

frame['tz'][:10]

tz_counts = frame['tz'].value_counts()

'''
Then, we might want to make a plot of this data using plotting library, matplotlib. You
can do a bit of munging to fill in a substitute value for unknown and missing time zone
data in the records. The fillna function can replace missing (NA) values and unknown
(empty strings) values can be replaced by boolean array indexing:
'''
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10]

'''
Making a horizontal bar plot can be accomplished using the plot method on the counts objects:
'''
tz_counts[:10].plot(kind='barh', rot=0)

frame['a'][1]
frame['a'][50]
frame['a'][51]

'''
Parsing all of the interesting information in these “agent” strings may seem like a
daunting task. Luckily, once you have mastered Python’s built-in string functions and
regular expression capabilities, it is really not so bad. For example, we could split off
the first token in the string (corresponding roughly to the browser capability) and make
another summary of the user behavior:
'''

results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
results.value_counts()[:8]

'''
Now suppose you wanted to decompose the top time zones into Windows vs. non-Windows users.
As a simplification let's say that a user is on Windows if the string 'Windows' is in the agent
string. Since some of the agents are missing, we exclude these from the data
'''
cframe = frame[frame.a.notnull()]

# We want to then compute a value whether each row is Windows or not:

operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
operating_system[:5]

# Then you can group the data by its time zone column and this new list of operating systems
by_tz_os = cframe.groupby(['tz', operating_system])

'''
The group counts, analogous to the value_counts function above, can be computed using size.
This result is then reshaped into a table with unstack
'''
agg_counts = by_tz_os.size().unstack().fillna(0)

agg_counts[:10]

'''
Finally, let's select the top overall time zones. To do so, I construct an indirect index
array from the row counts in agg_counts
'''
# Use to seot in ascending order
indexer = agg_counts.sum(1).argsort()

indexer[:10]

# I then user take to select the tows in that order, then slice off the last 10 rows
count_subset = agg_counts.take(indexer)[-10:]
count_subset

'''
Then, as shown in the preceding code block, this can be plotted in a bar plot; I’ll make
it a stacked bar plot by passing stacked=True
'''
count_subset.plot(kind='barh', stacked=True)

'''
The plot doesn’t make it easy to see the relative percentage of Windows users in the
smaller groups, but the rows can easily be normalized to sum to 1 then plotted again
'''
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)






