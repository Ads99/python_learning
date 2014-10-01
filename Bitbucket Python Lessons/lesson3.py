# -*- coding: utf-8 -*-
'''
Lesson 3

Get Data - Our data set will consist of an Excel file containing customer counts per date. We will learn how to read in the excel file for processing.
Prepare Data - The data is an irregular time series having duplicate dates. We will be challenged in compressing the data and comming up with next years forecasted customer count.
Analyze Data - We use graphs to visualize trends and spot outliers. Some built in computatiopnal tools will be used to calculate next years forecasted customer count.
Present Data - The results will be graphed.
'''

# Import libraries
from pandas import DataFrame, date_range, read_excel, concat
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys

print 'Python version ' + sys.version
print 'Pandas version ' + pd.__version__

# set seed
np.seed(111)

# Function to generate test data
def CreateDataSet(Number=1):
    
    Output = []
    
    for i in range(Number):
        
        # Create a weekly (mondays) date range
        rng = date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')
        
        # Create random data
        data = np.randint(low=25,high=1000,size=len(rng))
        
        # Status pool
        status = [1,2,3]
        
        # Make a random list of statuses
        random_status = [status[np.randint(low=0,high=len(status))] for i in range(len(rng))]
        
        # State pool
        states = ['GA','FL','fl','NY','NJ','TX']
        
        # Make a random list of states
        random_states = [states[np.randint(low=0,high=len(states))] for i in range(len(rng))]
        
        Output.extend(zip(random_states, random_status, data, rng))
    
    return Output

# Now that we have a function to generate our test data, let's create some data and stick it into a dataframe
dataset = CreateDataSet(4)
df = DataFrame(data=dataset, columns=['State','Status','CustomerCount','StatusDate'])
df.info()
df.head()

# Save results to excel
df.to_excel('Lesson3.xlsx', index=False)
print 'Done'

# Grab data from excel
# read_excel?

Location = "C:\Users\ABaker\Documents\Python Scripts\Lesson3.xlsx"

# Parse a specific sheet
df = read_excel(Location, 0, index_col='StatusDate')
df.dtypes
df.head()

'''
PREPARE DATA
This section attempts to clean up the data for analysis:
    1) Make sure the state column is all in upper case
    2) Only select records where the account status is equal to "1"
    3) Merge (NJ and NY) to NY in the state column
    4) Remove any outliers (any odd results in the data set)
'''

df['State'].unique()

'''
To convert all the sate values to upper case we will user the upper() function and the dataframe's apply attribute. The lambda function
simply will apply the upper function to each value in the State column
'''

# Clean State column, convert to upper case
df['State'] = df.State.apply(lambda x: x.upper())
df['State'].unique()

# Only grab where Status == 1
mask = df['Status'] == 1
df = df[mask]

'''
To turn the 'NJ' states into 'NY' we simply...
df.State == 'NJ'] - Find all records in the State column where they are equal to NJ.
df.State[df.State == 'NJ'] = 'NY' - For all records in the State column where they are equal to NJ, replace them with NY.]
'''

# Convert NJ to NY
mask = df.State == 'NJ'
df['State'][mask] = 'NY'
df['State'].unique()

'''
At this point we want to graph the data to check for any outliers or inconsistencies in the data. We will be using the plot() attribute of the dataframe.
As you can see from the graph below it is inconclusive and probably a sign that we need to perform some more data preparation
'''

df['CustomerCount'].plot()

'''
If we take a look at the data, we begin to realize that there are multiple values for the same State, StatusDate, and Status combination.
It is possible that this means the data you are working with is dirty/bad/inaccurate, but we will assume otherwise.
We can assume this data set is a subset of a bigger data set and if we simply add the values in the CustomerCount column per State, StatusDate, and Status
 we will get the Total Customer Count per day.
'''

sortdf = df[df['State']=='NY'].sort(axis=0)
sortdf.head(10)

'''
Our task is now to create a new dataframe that compresses the data so we have daily customer counts per State and StatusDate.
We can ignore the Status column since all the values in this column are of value 1.
To accomplish this we will use the dataframe's functions groupby and sum().

Note that we had to use reset_index.
If we did not, we would not have been able to group by both the State and the StatusDate since the groupby function expects only columns as inputs.
The reset_index function will bring the index StatusDate back to a column in the dataframe.
'''

# Group by State and StatusDate
Daily = df.reset_index().groupby(['State','StatusDate']).sum()
Daily.head()

'''

The State and StatusDate columns are automatically placed in the index of the Daily dataframe.
You can think of the index as the primary key of a database table but without the constraint of having unique values.
Columns in the index as you will see allow us to easily select, plot, and perform calculations on the data.

Below we delete the Status column since it is all equal to one and no longer necessary.
'''
del Daily['Status']
Daily.head()

# What is the index of the dataframe
Daily.index

# Select the State index
Daily.index.levels[0]

# Select the StatusDate index
Daily.index.levels[1]

'''
Let's now plot the data per State
As you can see by breaking the graph up by the State column we have a much clearer picture on how the data looks like. Can you spot any outliers?
'''

Daily.loc['FL'].plot()
Daily.loc['GA'].plot()
Daily.loc['NY'].plot()
Daily.loc['TX'].plot();

Daily.loc['FL']['2012':].plot()
Daily.loc['GA']['2012':].plot()
Daily.loc['NY']['2012':].plot()
Daily.loc['TX']['2012':].plot();

'''
We will assume that per month the customer count should remain relatively steady.
Any data outside a specific range in that month will be removed from the data set.
The final result should have smooth graphs with no spikes.

StateYearMonth - Here we group by State, Year of StatusDate, and Month of StatusDate.
Daily['Outlier'] - A boolean (True or False) value letting us know if the value in the CustomerCount column is ouside the acceptable range.

We will be using the attribute transform instead of apply.
The reason is that transform will keep the shape(# of rows and columns) of the dataframe the same and apply will not.
By looking at the previous graphs, we can realize they are not resembling a gaussian distribution, 
  this means we cannot use summary statistics like the mean and stDev.
We use percentiles instead. Note that we run the risk of eliminating good data.
'''

# Calculate Outliers
StateYearMonth = Daily.groupby([Daily.index.get_level_values(0), Daily.index.get_level_values(1).year, Daily.index.get_level_values(1).month])
Daily['Lower'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=.25) - (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
Daily['Upper'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=.75) + (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
Daily['Outlier'] = (Daily['CustomerCount'] < Daily['Lower']) | (Daily['CustomerCount'] > Daily['Upper']) 

# Remove Outliers
Daily = Daily[Daily['Outlier'] == False]

'''
The dataframe named Daily will hold customer counts that have been aggregated per day.
The original data (df) has multiple records per day.
We are left with a data set that is indexed by both the state and the StatusDate.
The Outlier column should be equal to False signifying that the record is not an outlier.
'''
Daily.head()

'''
We create a separate dataframe named ALL which groups the Daily dataframe by StatusDate.
We are essentially getting rid of the State column. The Max column represents the maximum customer count per month. The Max column is used to smooth out the graph.
'''
# Combine all markets

# Get the max customer count by Date
ALL = DataFrame(Daily['CustomerCount'].groupby(Daily.index.get_level_values(1)).sum())
ALL.columns = ['CustomerCount'] # rename column

# Group by Year and Month
YearMonth = ALL.groupby([lambda x: x.year, lambda x: x.month])

# What is the max customer count per Year and Month
ALL['Max'] = YearMonth['CustomerCount'].transform(lambda x: x.max())
ALL.head()

'''
As you can see from the ALL dataframe above, in the month of January 2009, the maximum customer count was 901. 
If we had used apply, we would have got a dataframe with (Year and Month) as the index and just the Max column with the value of 901.

There is also an interest to gauge if the current customer counts were reaching certain goals the company had established.
The task here is to visually show if the current customer counts are meeting the goals listed below.
We will call the goals BHAG (Big Hairy Annual Goal).

12/31/2011 - 1,000 customers
12/31/2012 - 2,000 customers
12/31/2013 - 3,000 customers
We will be using the date_range function to create our dates.

Definition: date_range(start=None, end=None, periods=None, freq='D', tz=None, normalize=False, name=None, closed=None)
Docstring: Return a fixed frequency datetime index, with day (calendar) as the default frequency

By choosing the frequency to be A or annual we will be able to get the three target dates from above.
'''
date_range?

# Create the BHAG dataframe
data = [1000,2000,3000]
idx = date_range(start='12/31/2011', end='12/31/2013', freq='A')
BHAG = DataFrame(data, index=idx, columns=['BHAG'])
BHAG

'''
Combining dataframes as we have learned in previous lesson is made simple using the concat function.
Remember when we choose axis = 0 we are appending row wise.
'''
# Combine the BHAG and the ALL data set 
combined = concat([ALL,BHAG], axis=0)
combined = combined.sort(axis=0)
combined.tail()

fig, axes = plt.subplots(figsize=(12, 7))

combined['BHAG'].fillna(method='pad').plot(color='green', label='BHAG')
combined['Max'].plot(color='blue', label='All Markets')
plt.legend(loc='best');

'''
There was also a need to forecast next year's customer count and we can do this in a couple of simple steps.
We will first group the combined dataframe by Year and place the maximum customer count for that year. This will give us one row per Year.
'''
# Group by Year and then get the max value per year
Year = combined.groupby(lambda x: x.year).max()
Year

# Add a column representing the percent change per year
Year['YR_PCT_Change'] = Year['Max'].pct_change(periods=1)
Year

'''
To get next year's end customer count we will assume our current growth rate remains constant.
We then will increase this years customer count by that amount and that will be our forecast for next year.
'''
(1 + Year.ix[2012,'YR_PCT_Change']) * Year.ix[2012,'Max']

'''
PRESENT DATA
'''
# First Graph
ALL['Max'].plot(figsize=(10, 5));plt.title('ALL Markets')

# Last four Graphs
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
fig.subplots_adjust(hspace=1.0) ## Create space between plots

Daily.loc['FL']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,0])
Daily.loc['GA']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,1]) 
Daily.loc['TX']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[1,0]) 
Daily.loc['NY']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[1,1]) 

# Add titles
axes[0,0].set_title('Florida')
axes[0,1].set_title('Georgia')
axes[1,0].set_title('Texas')
axes[1,1].set_title('North East');