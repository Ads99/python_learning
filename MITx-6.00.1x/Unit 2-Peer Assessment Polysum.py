# Regular Polygons: polysum
# A regular polygon has 'n' number of sides. Each side has length 's'.
#  - The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
#  - The perimeter of a polygon is: length of the boundary of the polygon

import math

def polysum(n,s):
    """
    This function sums the area and square of the perimeter of the regular polygon.

    :param n: number of sides of the polygon
    :param s: length of each side of polygon
    :return: int: returns the sum rounded to 4 decimal places.
    """
    area = (0.25 * n * s ** 2) / math.tan(math.pi/n)
    perim_square = (n * s) **2

    return round((area + perim_square),4)


def testGen():
    yield

def fun():
    print("Hello")

x = testGen()
y = fun()

print(type(x))
print(type(y))