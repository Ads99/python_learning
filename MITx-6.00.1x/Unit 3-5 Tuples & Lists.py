# Exercise: odd tuples
# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other
# element of the input tuple is copied, starting with the first one. So if test is the tuple
# ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    rTup = ()
    i = 0

    while i < len(aTup):
        if i % 2 == 0:
            rTup += (aTup[i],)
        i += 1

    return rTup

#t = ('I', 'am', 'a', 'test', 'tuple')
#print(oddTuples(t))

# Exercise 3
listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

print(listA.sort)
print(listA.sort())
print(listA)

print(listA.insert(0, 100))
print(listA)
print(listA.remove(3))
print(listA)
print(listA.append(7))
print(listA)
print(listA + listB)
listB.sort()
print(listB.pop())
print(listA.extend([4, 1, 6, 3, 4]))
print(listA)
print(listA.pop(4))
print(listA.reverse())
print(listA)
