# Exercise: gcd iter
# The greatest common divisor of two positive integers is the largest integer that divides each of them without
# remainder. For example,
# >> gcd(2, 12) = 2
# >> gcd(6, 12) = 6
# >> gcd(9, 12) = 3
# >> gcd(17, 12) = 1

# Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test
# value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either
# reach a case where the test divides both a and b without remainder, or you reach 1.

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    minarg = min(a, b)

    for i in range(minarg,0,-1):
        if a % i == 0 and b % i == 0:
            return i

#print(gcdIter(7,4))

# Exercise: gcd recur
# A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are
# two positive integers:
#   If b = 0, then the answer is a
#   Otherwise, gcd(a, b) is the same as gcd(b, a % b)
# Write a function gcdRecur(a, b) that implements this idea recursively. This function takes in two positive integers
# and returns one integer.

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

#print(gcdIter(7,4))

# Exercise: is in
# We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in
# alphabetical order.
# First, test the middle character of a string against the character you're looking for (the "test character"). If they
# are the same, we are done - we've found the character we're looking for!
# If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only
# consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can
# compare characters using Python's < function.)
#
# Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char
# will be a single character and aStr will be a string that is in alphabetical order. The function should return a
# boolean value. As you design the function, think very carefully about what the base cases should be.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    midStr = round(len(aStr) / 2)
    #print("Current aStr value: " + aStr)
    #print("Current aStr midway point: " + aStr[len(aStr) // 2])
    #print("Current ")
    #print("")

    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return char == aStr
    elif char == aStr[len(aStr) // 2]:
        return True
    elif char < aStr[len(aStr) // 2]:
        return isIn(char, aStr[0:len(aStr) // 2])
    else:
        return isIn(char, aStr[len(aStr) // 2 + 1: len(aStr)])

print(isIn('x', 'bbeghlmvvxy'))

