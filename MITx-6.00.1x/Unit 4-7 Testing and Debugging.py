def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    print("Outside loop... x = " + str(x) + " a = " + str(a))
    if x == a:
        print("First clause... x = " + str(x) + " a = " + str(a))
        return 0
    elif x < a:
        print("Second clause... x = " + str(x) + " a = " + str(a))
        return x
    else:
        print("Else clause... x = " + str(x) + " a = " + str(a))
        return(rem(x-a, a))

#rem(7,5)
#rem(2,5)


def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n + 1
   else:
      return n * f(n-1)

print(f(0))
print(f(3))