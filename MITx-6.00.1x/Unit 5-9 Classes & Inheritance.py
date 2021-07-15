class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __repr__(self):
        return 'Coordinate(' + str(self.x) + ',' + str(self.y) + ')'

"""
c = Coordinate(1,3)
d = Coordinate(4,3)
print(c)
print(c == d)
print(repr(Coordinate))
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, s):
        """Assumes s is another object of Class intSet
        Returns a new intSet containing elements that appear in both sets"""
        r = intSet()
        for i in self.vals:
            if s.member(i):
                r.insert(i)
        return r

    def __str__(self):
        """Returns a string representation of itself"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def __len__(self):
        """Returns the length of the intSet"""
        return len(self.vals)

"""
x = intSet()
x.insert(1)
x.insert(4)
x.insert(7)
x.insert(4)
y = intSet()
y.insert(5)
print(x)
print(y)
print(x.intersect(y))
print(len(x))
"""

