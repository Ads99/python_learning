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

# print header
# print data[1]

'''
The size() function counts how many elements are in
the array and sum() (as you would expect) sums up
the elements in the array
'''

number_passengers = np.size(data[0::, 1].astype(np.float))
number_survived = np.sum(data[0::, 1].astype(np.float))
proportion_survivors = number_survived / number_passengers

'''
Numpy has some lovely functions. For example, we can search the gender column, find where
any elements equal female (and for males, 'do not equal female'), and then use
this to determine the number of females and males that survived
'''

women_only_stats = data[0::, 4] == "female"  # This finds all
                                            # the elements in the gender
                                            # column that equals "female"
men_only_stats = data[0::, 4] != "female"    # This fins where all the
                                            # elements do not equal
                                            # female (i.e. male)
'''
We use these two new variables as a "mask" on our original train data, so we can select
only those women, and only those men on board, then calculate the proportion of those
who survived:
'''

# Using the index from above we select the females and males separately
women_onboard = data[women_only_stats, 1].astype(np.float)
men_onboard = data[men_only_stats, 1].astype(np.float)

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
        prediction_file_object.writerow([row[0], '1'])   # predict 1
    else:
        prediction_file_object.writerow([row[0], '0'])   # predict 0
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
# then modify the data in the Fare column to = 39, if it is greater or equal to the ceiling
data[data[0::, 9].astype(np.float) >= fare_ceiling, 9] = fare_ceiling - 1.0

fare_bracket_size = 10
number_of_price_brackets = fare_ceiling / fare_bracket_size

# I know there were 1st, 2nd and 3rd classes on board
number_of_classes = 3

# But it's better practice to calculate this from the data directly
# Take the length of an array of unique values in column index 2
number_of_classes = len(np.unique(data[0::,2]))

# Initialise the survival table with all zeros
survival_table = np.zeros((2, number_of_classes, number_of_price_brackets))

'''
Now that these are set up, you can loop through each variable and find all those
passengers that agress with the statements:
'''

for i in xrange(number_of_classes):                 # loop through each class
    for j in xrange(number_of_price_brackets):      # loop through each price bin

        women_only_stats = data[                                            # Which element
            (data[0::, 4] == "female")                                      # is a female
            &(data[0::, 2].astype(np.float) == i+1)                         # and was ith class
            &(data[0::, 9].astype(np.float) >= j*fare_bracket_size)         # was greater than this bin
            &(data[0::, 9].astype(np.float) < (j+1)*fare_bracket_size)      # and less than the next bin
            , 1]                                                            # in the 2nd col

        men_only_stats = data[                                              # Which element
            (data[0::, 4] != "female")                                      # is a male
            &(data[0::, 2].astype(np.float) == i+1)                         # and was ith class
            &(data[0::, 9].astype(np.float) >= j*fare_bracket_size)         # was greater than this bin
            &(data[0::, 9].astype(np.float) < (j+1)*fare_bracket_size)      # and less than the next bin
            , 1]

        survival_table[0,i,j] = np.mean(women_only_stats.astype(np.float))
        survival_table[1,i,j] = np.mean(men_only_stats.astype(np.float))

survival_table[ survival_table != survival_table ] = 0

print survival_table

'''
For our second model, let's again assume any probability greater than or equal to 0.5
should result in our predicting survival -- and less than 0.5 should not. We can
update our survival table with:
'''

survival_table[ survival_table < 0.5 ] = 0
survival_table[ survival_table >= 0.5 ] = 1

print survival_table

'''
When we go through each row of the test file we can find what criteria fit each new
passenger and assign them a 1 or 0 according to our survival table. As previously,
let's open up the test file to read (and skip the header row), and also a new file
to write to, called 'genderclassmodel.csv'
'''
test_file = open('test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()
predictions_file = open('genderclassmodel_AB.csv', 'wb')
p = csv.writer(predictions_file)
p.writerow(["PassengerId", "Survived"])

'''
As with the previous model, we can take the first passenger, look at his/her gender,
class and price of ticket, and assign a Survived label. The problem is that each
passenger in the test.csv file is not binned. We should loop through each bin and see
if the price of their ticket falls in that bin. If so, we can break the loop (so we don't
go through all the bins) and assign that bin:
'''

for row in test_file_object:                                                    # Loop through each passenger in data
    for j in xrange(number_of_price_brackets):                                  # For each passenger we loop thru each
                                                                                # price bin
        try:                                                                    # Some passengers have no
            row[8] = float(row[8])                                              # Fare data so try to make a float
        except:                                                                 # If fails: no data, so bin the fare
            bin_fare = 3 - float(row[1])                                        # according Pclass
            break                                                               # Break from the loop
        if row[8] > fare_ceiling:                                               # If there is data see if
                                                                                # it is greater than fare
                                                                                # ceiling we set earlier
            bin_fare = number_of_price_brackets-1                               # If so set to highest bin
            break                                                               # And then break loop
        if row[8] >= j * fare_bracket_size\
                and row[8] < \
                (j+1) * fare_bracket_size:                                      # If passes these tests
                                                                                # then loop through each bin
            bin_fare = j                                                        # then assign index
            break

        if row[3] == 'female':                                                  # If the passenger is female
            p.writerow([row[0], "%d" %\
                       int(survival_table[0, float(row[1])-1, bin_fare])])
        else:                                                                   #else if male
            p.writerow([row[0], "%d" % \
                       int(survival_Table[1, float(row[1])-1, bin_fare])])

# Close out the files.
test_file.close()
predictions_file.close()