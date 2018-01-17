# Define x as 0 for starting point.
x = 0
# Create a while loop with restrictive domain so that the while loop ends when x gets to 10,000.
while x < 10000:
    x = x + 1
# x%n == 0 represents that the remainder is 0 as x is divisible by a number. If divisible by 3, print bycicle. If divisible by 11, print car. If divisible by both 3 and 11, print motorcycle.
    if x%3 == 0 and x%11 == 0:
        print('motorcycle')
    elif x%3 == 0:
        print('bicycle')
    elif x%11 == 0:
        print('car')
# Print number as defined by x if x is not divisible by 3 or 11.
    else:
        print(x)