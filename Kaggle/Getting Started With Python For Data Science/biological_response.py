__author__ = 'ABaker'

from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt


#def main():

    # create the training and test sets
    dataset = genfromtxt(open('Kaggle/Getting Started With Python For Data Science/train.csv', 'r'), delimiter=',', dtype=2.8f)[1:]
    print type(dataset)