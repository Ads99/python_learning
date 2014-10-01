# -*- coding: utf-8 -*-
"""
Lesson 5

Here we take a brief look at the stack and unstack functions
"""

# Import libraries
from pandas import DataFrame
import pandas as pd

# Our small data set
d = {'one':[1,1],'two':[2,2]}
i = ['a','b']

# Create dataframe
df = DataFrame(data = d, index = i)

df.index

# Bring the columns and place them in the index
stack = df.stack()
stack

# The index now includes the column names
stack.index

unstack = df.unstack()
unstack

unstack.index

# We can also flip the column names with the index using the T (transpose) function
transpose = df.T
transpose

transpose.index