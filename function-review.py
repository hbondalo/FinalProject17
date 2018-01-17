# imports
import random

"""
Review of functions
"""

# Functions are self-contained chunks of code that can be repeated by calling them
# Here, I've defined a function called very_simple_function
def very_simple_function():
    """print 'This isn't a very useful function' """
    print("This isn't a very useful function")
    # The line that says 'return' isn't strictly necessary, because the function will run as if it is there
    # I'm including it for consistency
    return

#################### STEP 1
# Call very_simple_function five times. What do you expect to happen?
# After you're done with this review section, you may comment out the five calls you made to very_simple_function
for x in range(5):
    very_simple_function()


# ################### STEP 2
# Now you're going to complete a function I've already defined
# Replace the comment with your own line of code
def say_hello():
    """print 'Hello World' """
    # What goes here?
    print('Hello World')
    return

# This line should cause Hello World to be printed to the terminal. If it doesn't, you'll need to figure out what you did wrong
say_hello()



# # ################### STEP 3
# # If I print the results of the say_hello() function, I can see that it prints "Hello World" followed by "None"
# Why does it print None? If you don't know why, think about what return values are - the next few steps will help
# Uncomment the line below and run it
print(say_hello())



# ################### STEP 4
# You may comment out step 2 and step 3 if you wish. This will make it easier to see what's happening in the next few sections
# In step 3, I mentioned return values. What are they?
def roll_a_die():
    """Generate and return a random number 1-6"""
    n = random.randint(1, 6)
    return n

# Because the roll_a_die function returns the value of n, we can use it as the value it returns
# Just calling the function will not print anything to the terminal, because we didn't use a print function

roll_a_die()    # Nothing is printed

# On the next line, write a line of code that will print the value returned by the roll_a_die() function
print(roll_a_die())


# ################### STEP 5
# I've created most of a function. Modify it so it returns

def choose_random_color():
    """Choose and return a random color from the list"""
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    random_color = random.choice(colors)
    # Insert a line to return the random color that was chosen
    return random_color

# If you've modified the function correctly, this should print a random color five times
for x in range(5):
    print(choose_random_color())



#################### STEP 6
# You may comment out the steps above
# Sometimes you want to give additional information to a function. We use arguments for this
# Arguments are variables that belong to the function.
# They're local to the function, which means they don't exist outside of it
# When you call the function, the arguments you include in the parentheses are assigned to the variables in the function, in order
# The function below is complete

def roll_gaming_die(sides):
    """Generate and return a random number from a die with an arbitrary number of sides"""
    # Generate a random number from 1 to the chosen number of sides
    n = random.randint(1, sides)
    return n

# What can you put into the parentheses for the print function to have it print out a random number from 1 through 20 (including 20)?

for x in range(30):
    print(roll_gaming_die(20))