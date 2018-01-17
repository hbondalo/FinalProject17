# Assign these variables as strings
animal_1 = "squirrel"
animal_2 = "anteater"
# Assign these variables as numbers
animal_1_friends = 2
animal_2_friends = 12


# Formatting string method 1: Use the letter f in front of a string to input variables within {braces}
print(f'The {animal_1} is a wild animal.')
print(f'An {animal_2} is a "wild animal" according to Monica.')
print(f'The {animal_1} has {animal_1_friends} friends while the {animal_2} has {animal_2_friends} friends.')
# I attached a string to a variable
fact = f"The {animal_1} and the {animal_2} are Preston and Monica's favorite animals, respectively."
print(fact)


# Formatting string method 2: Use empty brackets in the string and add .format() right after string with a comma-separated list of variables wanted in order.
print("Preston and Monica fight a lot about whether the {} or the {} should have more friends".format(animal_1, animal_2))
print("They fight because the {} has {} while the {} has only {}".format(animal_2, animal_2_friends, animal_1, animal_1_friends))
# Brackets can be numbered to show which variable goes where to simplify
# 0 refers to first variable, other variables follow after 0
print("Preston's favorite animal, {}, is printed before Monica's favorite animal, the {}.".format(animal_1, animal_2))
print("Now, Monica's favorite animal,the {1}, is printed before Preston's favorite animal, the {0}. The animals are the {1} and the {0}.".format(animal_1, animal_2))


# Formatting string method 3: Save a string that has the brackets and use that repeatedly as a variable
f_string = "{} {} {} {} {}"
print(f_string.format('z', 'y', 'x', 'w', 'v'))
print(f_string.format('yah', 'yeet', 'skrt', 'mop', 'si'))
print(f_string.format(4, 'three', 2, 'uno', 0))
math_string = "{} + {} = {}"
print(math_string.format(1, 2, 3))
print(math_string.format(6, 9, 15))


# Formatting string method 4: You can join strings with variables
a = "I"
b = "Really"
c = "Want"
d = "To"
e = "Eat"
print(a + b + c + d + e)
# You can also join strings with the .join() function (inside the parentheses is called a tuple)
# The string before the .join() function indicated what goes inbetween each variable or string in the function
print(" ".join((a,b,c,d,e)))
print(" :) ".join(("a", "b", "c")))


# Formatting string method 5: Seperate lines using \n
print("This is one line\nand this is another line")


# Formatting string method 6: Use a multi-line string using three sets of double quotes
mega_string = """I don't really wanna do the work today
I don't reeeally want to do the work today
I don't really want to dooooo the woork today
I don't wanna do the work today!"""
print(mega_string)