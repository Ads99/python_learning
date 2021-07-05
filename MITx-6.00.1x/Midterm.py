# Problem 1-1
#x = "pi"
#y = "pie"
#print(x, y)
#x,y = y, x
#print(x, y)

# Problem 1-7
#def f():
#    return 1.0
#a = f()
#print(type(a))

# Problem 2-5
#L = [1,2,3]
#d = {'a': 'b'}
#def f(x):
#    return 3

#for i in range(1000001, -1, -2):
#    print(f)

# Problem 2-6
#stuff = [("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")]
#stuff = "iQ"
#for thing in stuff:
#    if thing == 'iQ':
#        print("Found it")

#def Square(x):
#    return SquareHelper(abs(x), abs(x))

#def SquareHelper(n, x):
#    if n == 0:
#        return 0
#    return SquareHelper(n-1, x) + x

#x = Square(-2)
#print(x)

# Problem 3
# Write a simple procedure, myLog(x, b), that computes the logarithm of a number x relative to a base b. For example,#
# if x = 16 and b = 2, then the result is 4 (2^4 = 16). If x = 15 and b = 3, then the result is 2 (3^2=9, i.e. is the
# largest power of 3 less than 15.)
# In other words, myLog should return the largest power of b such that b to that power is still less than or equal to x.
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    p = 2
    if b**p > x and b**1 <= x:
        return 1
    elif b**p > x and b**1 > x:
        return 0
    else:
        while b**p <= x:
            if b**p == x:
                break
            elif b**(p+1) > x:
                break
            else:
                p += 1
        return p

#print(myLog(16, 2))
#print(myLog(15, 3))
#print(myLog(4, 16))
#print(myLog(26, 6))

# Problem 4
# Write a Python function that returns the sublist of strings in `aList` that contain fewer than 4 characters. For#
# example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]
# This function takes in a list of strings and returns a list of strings. Your function should not modify aList.

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    nList = []
    for i in aList:
        if len(i) <= 3:
            nList.append(i)
    return nList

aList = ["apple", "cat", "dog", "banana"]
#print(lessThan4(aList))

# Problem 5
# Write a Python function that returns a list of keys in aDict with the value `target`. The list of keys you return
# should be sorted in increasing order. The keys and values in aDict are both integers. (If aDict does not contain the
# value `target`, you should return an empty list.).
# This function takes in a dictionary and an integer and returns a list

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here
    l = []
    for k, v in aDict.items():
        if v == target:
            l.append(k)
    return sorted(l)

aDict = {1: 8,
         7: 4,
         3: 120}
#print(aDict)
#print(keysWithValue(aDict, 8))

# Problem 6
# Implement a function that meets the specifications below
# Examples:
#   max_val((5, (1,2), [[1],[2]])) returns 5.
#   max_val((5, (1,2), [[1],[9]])) returns 9

def max_val(t):
    """ t: tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # Your code here
    l = []
    for i in t:
        if isinstance(i, int):
            l.append(i)
        elif isinstance(i, list) or isinstance(i, tuple):
            for j in i:
                if isinstance(j, list):
                    for k in j:
                        l.append(k)
                else:
                    l.append(j)
    return max(l)

#print(max_val((5, (1,2), [[1],[2]])))
#print(max_val((5, (1,2), [[1],[9]])))
#print(max_val([[1,2,3], 18, (96, 97)]))

# Problem 7
# Write a Python function called satisfiesF that has the specification below. Then make the function call
# run_satisfiesF(L, satisfiesF). Your code should look like:

def f(s):
    return 'a' in s

#def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
#    newL = L[:]
#    for s in L:
#        if not(f(s)):
            #print("Removing: ", s, ", New Length:", len(newL)-1)
#            newL.remove(s)
            #print(newL)
#    L = newL
#    return len(newL)

#L = ['a', 'b', 'a', 'b', 'c']
#print(satisfiesF(L))
#print(L)

#run_satisfiesF(L, satisfiesF)

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    i = 0
    while len(L) > i:
        if f(L[i]):
            i += 1
        else:
            L.pop(i)
    return len(L)

#L = ['a', 'b', 'a', 'c', 'd']
L = ['a', 'b', 'a', 'b', 'c', 'u', 'a', 'x']
print(satisfiesF(L))  # 2
print(L)  # ['a', 'a']