__author__ = 'ABaker'

'''
The first thing to do is to import the relevant packages
that I will need for my script,
these include the Numpy (for maths and arrays)
and csv for reading and writing csv files
If I want to use something from this I need to call
csv.[function] or np.[function] first
'''

import csv as csv
import numpy as np

# Open up the csv file into a python project
csv_file_object = csv.reader(open('train.csv', 'rb'))
header = csv_file_object.next()  # The next() command just skips the first line which is a header

data = []                        # Create a variable called 'data'.
for row in csv_file_object:      # Run through each row in the csv file,
    data.append(row)             # adding each row to the data variable
data = np.array(data)            # Then convert from a list to an array
                                 # Be aware that each item is currently
                                 # a string in this format

'''
The size() function counts how many elements are in
the array and sum() (as you would expect) sums up
the elements in the array
'''

number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
proportion_survivors = number_survived / number_passengers

'''
Numpy has some lovely functions. For example, we can search the gender column, find where
any elements equal female (and for males, 'do not equal female'), and then use
this to determine the number of females and males that survived
'''

women_only_stats = data[0::,4] == "female"  # This finds all
                                            # the elements in the gender
                                            # column that equals "female"
men_only_stats = data[0::,4] != "female"    # This fins where all the
                                            # elements do not equal
                                            # female (i.e. male)
'''
We use these two new variables as a "mask" on our original train data, so we can select
only those women, and only those men on board, then calculate the proportion of those
who survived:
'''

# Using the index from above we select the females and males separately
women_onboard = data[women_only_stats,1].astype(np.float)
men_onboard = data[men_only_stats,1].astype(np.float)

# Then we find the proportions of them that survived
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)

print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived

'''
Now that I have my indication that women were much more likely to survive, I am done
with the training set

We now read in the test file by opening a python object to read and another to write.
First we read the test.csv file and skip the header line
'''
test_file = open('test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()

'''
Now let's open a pointer to a new file so we can write to it (this file does not exist yet).
Call it something descriptive so that it is recognizable when we upload it
'''
prediction_file = open("genderbasedmodel.csv", "wb")
prediction_file_object = csv.writer(prediction_file)

'''
We now want to read in the test file row by row, see if it is female or male, and write
our survival prediction to a new file
'''
prediction_file_object.writerow(["PassengerID", "Survived"])

for row in test_file_object:                            # For each row in test.csv
    if row[3] == 'female':                              # is it a female, if yes then
        prediction_file_object.writerow([row[0],'1'])   # predict 1
    else:
        prediction_file_object.writerow([row[0],'0'])   # predict 0
test_file.close()
prediction_file.close()

'''
Pythonising the second submission
  We now need to bin up the ticket price into 4 bins and model the outcome based on:
    class, gender, ticket price

  The idea is to create a table which contains just 1's and 0's. The array will be a
  survival reference table, whereby you read in the test data, find out passenger attributes,
  look them up in the survival table and determine if they should be predicted to survive or not.
  In this case of a model that uses gender, calss and ticket price you will need an array of
  2x3x4 ([female/male], [1st/2nd/3rd class], [4 bins of prices])

  The script will systematically loop through each combination and use the 'where' function in
  python to search the passengers that fit that combination of variables. Just like before, you can
  ask what indices in your data equals female, 1st class and paid more than $30. The problem is that
  looping through requires bins of equal sizes, i.e. $0-9, $10-19, $20-29, $30-39. For the sake of
  binning let's say everything equal to and above 40 "equals" 39 so it falls in this bin
'''

# So we add a ceiling
fare_ceiling = 40
# then modify the data in the Fare column to = 39, if it is greater or equal to the ceoling
data[ data[0::,9].astype(np.float) >= fare_ceiling, 9] = fare_ceiling - 1.0

fare_bracket_size = 10
number_of_price_brackets = fare_ceiling / fare_bracket_size

# I know there were 1st, 2nd and 3rd classes on board
number_of_classes = 3

# But it's better practice to calculate this from the data directly
# Take the length of an array of unique values in column index 2
number_of_classes = len(np.unique(data[0::,2]))

