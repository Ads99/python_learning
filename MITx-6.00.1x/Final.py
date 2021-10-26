# Problem 3
# Write a function is_triangular that meets the specification below.
# A triangular number is a number obtained by the continued summation of integers starting from 1. For example,
# 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    total = 0
    if k == 1:
        return True
    else:
        for i in range(1, k):
            total += i
            #print(total)
            if total == k:
                return True
            else:
                next
        return False


#print(is_triangular(1))
#print(is_triangular(2))
#print(is_triangular(3))
#print(is_triangular(10))
#print(is_triangular(6))


# Problem 4
# Write a Python function that takes in two lists and calculates whether they are permutations of each other. The lists
# can contain both integers and strings. We define a permutation as follows:
#   - the lists have the same number of elements
#   - list elements appear the same number of times in both lists
# If the lists are not permutations of each other, the function returns False.
# If they are permutations of each other, the function returns a tuple consisting of the following elements:
#   - the element occuring the most times
#   - how many times that element occurs
#   - the type of the element that occurs the most times
#  If both lists are empty return the tuple (None, None, None). If more than one element occurs the most number of
#  times, you can return any of them.
# Examples:
# if L1 = ['a', 'a', 'b'] and L2 = ['a', 'b'] then is_list_permutation returns False
# if L1 = [1, 'b', 1, 'c', 'c', 1] and L2 = ['c', 1, 'b', 1, 1, 'c'] then is_list_permutation returns
# (1, 3, <class 'int'>) because the integer 1 occurs the most, 3 times, and the type of 1 is an integer (note that the
# third element in the tuple is not a string).

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    d1 = {}
    d2 = {}
    if len(L1) != len(L2):
        return False
    elif len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    else:
        # build a dict for each element in L1
        for i in L1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for i in L2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1

    # Now evaluate the crossover between dicts
    # We look at each key in d1 and evaluate whether the same key in d2 has the same number of occurences
    #print(d1.items())
    #print(d2.items())
    maxVal = 0
    for k1, v1 in d1.items():
        if d2[k1] != v1:
            #print(str(d2[k1]), "matches to: ", str(v1))
            return False

        # We additionally keep track of the highest value associated with the key
        if v1 > maxVal:
            maxVal = v1
            retTup = (k1, v1, type(k1))

    # If we've got this far we know that the dicts are identical
    # We can now return a tuple of the highest occuring key in the dict, along with the # occurences and the type of
    # the key
    return retTup

#print(is_list_permutation([1,2,"Hi"], ["Hi",2,1]))
#print(is_list_permutation([1,2,2,"Hi"], ["Hi",2,1,3]))
#print(is_list_permutation([1,2,"Hi","Hi","Hi"], ["Hi",2,"Hi","Hi",1]))

# Problem 5
# You are given a dictionary aDict that maps integer keys to integer values. Write a Python function that returns a list
# of keys in aDict that map to dictionary values that appear exactly once in aDict.
#  - This function takes in a dictionary and returns a list.
#  - Return the list of keys in increasing order.
#  - If aDict does not contain any values appearing exactly once, return an empty list.
#  - If aDict is empty, return an empty list.
# For example:
#   If aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0} then your function should return [1, 3, 8]
#   If aDict = {1: 1, 2: 1, 3: 1} then your function should return []

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    keyList = []
    keyDict = {}

    for key in list(aDict.keys()):
        if aDict[key] not in keyDict:
            keyDict[aDict[key]] = 1
        else:
            keyDict[aDict[key]] += 1

    # Now iterate over the newly created keyDict for values which appear only once
    for i in keyDict.keys():
        if keyDict[i] == 1:
            for j in aDict.keys():
                if aDict[j] == i:
                    keyList.append(j)

    return sorted(keyList)

#print(uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}))
#print(uniqueValues({1: 1, 2: 1, 3: 1}))

# Problem 6
# In this problem, you will implement a class according to the specifications in the template file usresident.py. The
# file contains a Person class similar to what you have seen in lecture and a USResident class (a subclass of Person).
# Person is already implemented for you and you will have to implement two methods of USResident.
# For example, the following code:
#     a = USResident('Tim Beaver', 'citizen')
#     print(a.getStatus())
#     b = USResident('Tim Horton', 'non-resident')
#     >> citizen
#     >> will show that a ValueError was raised at a particular line

class Person(object):
    def __init__(self, name):
        # create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank + 1:]
        except:
            self.lastName = name
        self.age = None

    def getLastName(self):
        # return self's last name
        return self.lastName

    def setAge(self, age):
        # assumes age is an int greater than 0
        # sets self's age to age (in years)
        self.age = age

    def getAge(self):
        # assumes that self's age has been set
        # returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age

    def __lt__(self, other):
        # return True if self's name is lexicographically less
        # than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        # return self's name
        return self.name


class USResident(Person):
    """
    A Person who resides in the US.
    """

    def __init__(self, name, status):
        """
        Initializes a Person object. A USResident object inherits
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        # Write your code here
        Person.__init__(self, name)
        self.status = status
        if self.status in ['citizen', 'legal_resident', 'illegal_resident']:
            pass
        else:
            raise ValueError('Invalid status entered.')

    def getStatus(self):
        """
        Returns the status
        """
        # Write your code here
        return self.status

#a = USResident('Tim Beaver', 'citizen')
#print(a.getStatus())
#b = USResident('Tim Horton', 'non-resident')

# Problem 7
# You are given the following superclass. Do not modify this.
# Write a class that implements the specifications below. Do not override any methods of Container.
# For example:
#   d1 = Bag()
#   d1.insert(4)
#   d1.insert(4)
#   print(d1)
#   d1.remove(2)
#   print(d1)
# prints...
#   >>> 4:2
#   >>> 4:2

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of
            times it occurs in self by 1. Otherwise does nothing. """
        try:
            self.vals[e] -= 1
        except:
            pass


    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        try:
            return self.vals[e]
        except:
            return 0

#d1 = Bag()
#d1.insert(4)
#d1.insert(4)
#print(d1)
#d1.remove(2)
#print(d1)

d1 = Bag()
d1.insert(4)
d1.insert(4)
d1.insert(4)
print(d1.count(2))