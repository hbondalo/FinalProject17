# Import pi to use for equations in functions by using from math import pi.
from math import pi

# Prompt the user to insert a radius.
radius = float(input("Insert a number for the radius to solve for circumference, area, and surface area of a circle/sphere."))

# Define function to solve for circumference. Make sure radius is an integer.
def find_circumference(radius):
    """returns the appropriate number for the circumference of a circle or sphere with the specified radius"""
    circumference_circle = 2*pi*radius
    return circumference_circle

# Print so that it shows that the number is equivalent to circumference.
print('circumference =', find_circumference(radius))


def find_area(radius):
    """returns the appropriate number for the area of a circle or sphere with the specified radius"""
    area_circle = pi*radius**2
    return area_circle

print('area =', find_area(radius))


def find_surface_area(radius):
    """returns the appropriate number for the surface area of a circle or sphere with the specified radius"""
    surface_area_circle = 4*pi*radius**2
    return surface_area_circle

print('surface area =', find_surface_area(radius))
