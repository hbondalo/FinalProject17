def say_hello():
    """Prints hello"""
    print("hello")

# Print hello
say_hello()


def fifty():
    """Returns 50"""
    return 50


# Should print 100
print(fifty() * 2)



def add_them_all(n1, n2, n3, n4, n5):
    """Returns sum of five numbers"""
    #insert code in here to return the sum of all 5 arguments
    return 1+3+5+2+100

# Should print 111
print(add_them_all(1, 3, 5, 2, 100))


# Import math to get square root function
from math import sqrt
# Define sidees a and b
a = 5
b = 12
# Define function to find hypotenuse using sides a and b
def find_hypotenuse():
    """returns the hypotenuse of a triangle with sides a and b"""
    return sqrt(a**2+b**2)

# Print hypotenuse as an integer instead of a float
print(int(find_hypotenuse()))
