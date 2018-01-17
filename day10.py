# Prompt question to ask what the user's favorite color is.
color = input('What\'s your favorite color in the rainbow? ').lower()

# First statement is if and starts with red. Every other color is elif. Else is for anything that isn't a color of the rainbow.
if color == 'red':
    print('Wow, I just red that you like the color red! Me too!')

elif color == 'orange':
    print('Orange you glad that this is your favorite color?')

elif color == 'yellow':
    print('Brrrrring bbrrringggg, yellow? That\'s my favorite color too!')

elif color == 'green':
    print('I love me some green eggs and ham!')

elif color == 'blue':
    print('Don\'t be so blue! That\'s a great color!')

elif color == 'indigo':
    print('Wow, what a unique choice!')

elif color == 'purple':
    print ('I love purple, too!')

else:
    print('That\'s not what I asked for. Please listen to instructions. >:(')



# Prompt user how much he/she likes her color.
number = int(input('On a scale of 1-10, how much do you like your favorite color? '))

# Start if with scale that equals 10, then use ranges for elif. Else tells user to try again.
if number == 10:
    print('If you love it so much, why don\'t you just marry it?')

elif number < 10 and number >= 8:
    print('That seems about right.')

elif number < 8 and number >= 5:
    print('Nice. Nice.')

elif number < 5 and number >= 1:
    print('You need to pick a new favorite color...')

else:
    print('That\'s not right?')