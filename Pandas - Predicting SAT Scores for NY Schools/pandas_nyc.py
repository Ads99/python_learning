__author__ = 'ABaker'

'''
From the Kaggle blog here:
http://blog.kaggle.com/2013/01/17/getting-started-with-pandas-predicting-sat-scores-for-new-york-city-schools/

GOALS:

1) Using data from NYC Open Data, build a unified, tabular dataset ready for use with machine learning algorithms
to predict student SAT scores on a per school basis.

2) Learn and use the Pandas data analysis package.

3) Learn how data is typically prepared for machine learning algorithms (ingestion, cleaning, joining,
feature generation).
'''
#import os
#print os.getcwd()

import pandas as pd

# Load the data
dsProgReports = pd.read_csv('NYC_Schools\\School_Progress_Reports_-_All_Schools_-_2009-10.csv')

