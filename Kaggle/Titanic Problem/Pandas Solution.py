__author__ = 'ABaker'

'''
This is not a cohesive script to be run, nor part of a sample .py found on the Data Page.
Instead, this tutorial is meant to entered line by line on your python command line,
so that you can learn some of the methods at your disposal and see what occurs.
You might even deviate from this tutorial with other variables that interest you.
Finally, at times the output from your command will be very long-winded,
so not everything is printed in its entirety here.
'''

import csv as csv
import numpy as np
import pandas as pd

csv_file_object = csv.reader(open('Kaggle - Titanic Problem\\train.csv', 'rb'))
header = csv_file_object.next()
data = []

for row in csv_file_object:
    data.append(row)
data = np.array(data)

print data
print data[0:15, 5]
print type(data[0::,5])

# Numpy will error here as some numbers are missing
ages_onboard = data[0::,5].astype(np.float)

# We therefore use Pandas
# For .read_csv, always use header=0 when you know row 0 is the header row
df = pd.read_csv('Kaggle - Titanic Problem\\train.csv', header=0)

# See what is in the data frame by typing the data frame name
df
df.head(3)
df.tail(3)

# Get the type of the object ("pandas.core.frame.DataFrame")
type(df)

# Using NumPy the elements were all imported as strings.
# In Pandas each element has it's own data type
df.dtypes

'''
Pandas is able to infer numerical types whenever it can detect them.
So we have values already stored as integers. When it detected the
existing decimal points somewhere in Age and Fare, it converted those
columns to float.
There are two more very valuable commands to learn on a dataframe:
'''
df.info()

'''
Now try this. Pandas takes all of the numerical columns and quickly
calculates the mean, std, minimum and maximum value.
'''

df.describe()

'''
DATA MUNGING

One step in any data analysis is the data cleaning. Thankfully pandas make things
easier to filter, manipulate, drop out, fill in, transform and replace values
inside the dataframe. Below we also learn the syntax that pandas allows for
referring to specific columns
'''

# Let's acquire first 10 rows of the Age column
df['Age'][0:10]
# Alternatively
df.Age[0:10]

# Find the type of the column 'Age'
type(df['Age'])  # pandas.core.series.Series

# At this point we'd really like to get the mean value
df['Age'].mean()
# And the median?
df['Age'].median()

'''
The next thing we'd like to do is look at more specific subsets of the
dataframe. Again pandas makes this very convenient to write. Pass it
a [list] of the columns desired
'''

df[ ['Sex', 'Pclass', 'Age'] ]

'''
Filtering data is another important tool if we are investigating the
data by hand. The .describe() command has indicated that the max age
was 80. What to the older passengers look like in this data set?
This is written by passing the criteria of df as a 'where' clause into df
'''
df[df['Age'] > 60]

'''
If you were most interested in the mix of gender and Passenger class of
these older people, you would want to combine the two skills you just
learned and get only a few columns for the same 'where' filter
'''
df[df['Age'] > 60][['Sex', 'Pclass', 'Age', 'Survived']]

'''
From visual examination of all 22 cases, it seems they were mostly men,
mostly(?) 1st class, and mostly perished.

Now it's time to investigate all of those missing Age values, because
we will need to address them in our model if we hope to use all the
data for more advanced algorithms. To filter for missing values, use :
'''

df[df['Age'].isnull()][['Sex', 'Pclass', 'Age']]

'''
It will also be useful to combine multiple criteria (with the '&' syntax)
To practice even more functionality in the same line of code, let's take a
count of the males in each class
'''
for i in range(1,4):
    print i, len(df[ (df['Sex'] == 'male') & (df['Pclass'] == i) ])

'''
Before we finish the initial investigation by hand, let's use one other
convenience function of pandas to derive a histogram of any numerical
column. The histogram function is really a shortcut to the more powerful
features of the matplotlib/pylab packages, so let's be sure that's imported
'''
import pylab as P
df['Age'].hist()
P.show()

'''
Inside the parentheses of hist() you can also be more explicity about options of
this function. Before you invoke it you can also be explicit that you are dropping
the missing values of Age
'''
df['Age'].dropna().hist(bins=16, range=(0,80), alpha=.5)
P.show()

'''
CLEANING THE DATA

Now we transform the values in the dataframe into the shape we need for machine learning.
First of all, it's hard to run analysis on the string values of "male" and "female".
Let's practice transforming it in three ways -- twice for fun and once to make it useful.
We'll store our transformation in a new column, so the original Sex isn't changed.

In Pandas, adding a column is as easy as naming it and passing it new values.
'''

df['Gender'] = 4

# Now let's make it mean something that's actually derived from the Sex column.
df['Gender'] = df['Sex'].map(lambda x: x[0].upper())

'''
"lambda x" is a built-in function of python for generating an anonymous function
in the moment, at runtime. Remember that x[0] of any string returns it's first character.

What we really need is a binary integer for female and male, similar to the way Survived is stored
As a matter of consistency, let's also make Gender into values of 0 and 1's. We have a precedent
of analyzing the women first in all of our previous arrays, so let's decide female = 0 and male = 1
'''
df['Gender'] = df['Sex'].map({'female': 0, 'male': 1}).astype(int)

# We do something similar for the Embarked columns
df['Embarked_Coded'] = df['Embarked'].dropna().map({'C': 0, 'Q': 1, 'S': 2}).astype(int)

# As an aside here is how to get unique values
df['Embarked'].unique()

'''
Now it's time to deal with the missing values of Age, because most machine learning will need a
complete set of values in that column to use it. By filling it in with guesses, we'll be introducing
some noise into a model, but it we can keep our guesses reasonable, some of them should be close to
the historical truth and the overall predictive power of Age might still make a better model than
before.

We know the average [known] age of all passengers is 29.699 - we could fill in the null values
with that, but maybe the median would be better? (to reduce influence of a few rare 70 and 80 yo)
The Age histogram did seem positively skewed.

For now let's decide to be more sophisticated, that we want to use the age that was typical in each
passenger class. And decide that the median might be better. Let's build another reference table
to calculate what each of these medians are
'''

median_ages = np.zeros((2,3))
median_ages

# We then populate the array:
for i in range(0, 2):
    for j in range(0, 3):
        median_ages[i, j] = df[(df['Gender'] == i) & \
                               (df['Pclass'] == j+1)]['Age'].dropna().median()

median_ages

'''
We could fill in the missing ages directly into the Age column. But to be extra cautious and not
lost the state of the original data, a more formal way would be to create a new column, 'AgeFill',
and even record which ones were originally null (and thus artificially guessed)

First make a copy of Age
'''
df['AgeFill'] = df['Age']

# Take a look at just the rows with missing values and limit it to the columns important to us now
df[ df['Age'].isnull() ][['Gender', 'Pclass', 'Age', 'AgeFill']].head(10)

'''
Use some code to fill in AgeFill based on our median_ages table. Here we happen to use the
alternative syntax for referring to an existing column, like df.Age rather than df['Age'].
There's a 'where' clause on df and referencing its column AgeFill, then assigning it an
appropriate value out of median ages
'''
for i in range(0, 2):
    for j in range(0, 3):
        df.loc[ (df['Age'].isnull()) & (df['Gender'] == i) & (df['Pclass'] == j+1), 'AgeFill'] = median_ages[i, j]

# Now view the same 10 rows we viewed earlier
df[ df['Age'].isnull() ][['Gender', 'Pclass', 'Age', 'AgeFill']].head(10)

'''
This confirms we accomplished exactly what we wanted.

Let's also create a feature that records whether the Age was originally missing. This is relatively simple
by allowing pandas to use the integer conversion of the True/False evaluation of it's built-in function,
pandas.isnull()
'''

#df['AgeIsNull'] = df['Age'].isnull() # THIS IS THE WAY I DID IT - I THINK IT'S MORE SIMPLE???

df['AgeIsNull'] = pd.isnull(df['Age']).astype(int) # THIS WAY MAKES IT NUMERICAL THOUGH
df.describe()

'''
FEATURE ENGINEERING

Let's create a couple of other features, this time using simple math on existing columns. Since we know
that "Parch" is the number of parents of children onboard, and "SibSp" is the number of siblings or
spouses, we could collect those together as a FamilySize
'''
df['FamilySize'] = df['SibSp'] + df['Parch']

'''
We can also create artificial features if we think it may be advantageous to a machine learning
algorithm -- of course, it might not. For example, we know Pclass had a large effect on survival, and
it's possible Age will too. One artificial feature could incorporate whatever predictive power might be
available from both Age and Pclass by multiplying them. This amplifies 3rd class (3 is a higher multiplier)
at the same time it amplifies older ages. Both of these were less likely to survive, so in theory this
could be useful
'''
df['Age*Class'] = df['Age'] * df['Pclass']

# We can make some histograms of these new columns to understand them better
df['FamilySize'].hist()
P.show()

df['Age*Class'].hist()
P.show()

'''
We know we'd like to have better predictive power for the men, so you might be wishing you could pull
out more information from the Name column, e.g. honorary or pedestrian title of the men. We won't
accomplish that in this tutorial, but it might be helpful...
'''

'''
FINAL PREPARATION

We have our data almost ready for machine learning, but most basic ML techniques will not work on strings,
and in python they almost always require the data to be an array -- the implementations we will see in the
 "sklearn" package are not written to use a pandas dataframe. So the last two things we need to do are:

 1) determone what columns we have left which are not numeric
 2) send our pandas.DataFrame back to a numpy.array
'''
df.dtypes

'''
With a little manipulation we can require .dtypes to show only the columns which are 'object', which for
pandas means it has strings
'''
df.dtypes[df.dtypes.map(lambda x: x=='object')]

# The next step is to drop the columns which we will not use
df = df.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1)

'''
We can also drop 'Age' even though it's numeric since we copied and filled that to a better column: AgeFill
The original 'Age' still has the missing values which won't work well in our future model
'''
df = df.drop(['Age'], axis=1)

'''
An alternate command is to drop any rows which still have missing values.
N.B this removes observations even if only 1 column has a NaN anywhere
It could delete most of your dataset if you aren't careful with the state of missing values in other columns
'''
df = df.dropna()

'''
The final step is to convert it into a Numpy array. Pandas can always send back an array
using the .values method. Assign to a new variable, train_data
'''
train_data = df.values
type(train_data)
train_data

# Compare this to the original array we used in the last tutorial!
data