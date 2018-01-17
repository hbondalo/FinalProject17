# Assign names of characters to variables
name_1 = input("Choose the name for the main character.")
name_2 = input("Choose a name for the cowboy.")
name_3 = input("Choose a name for the boring girl.")
name_4 = input("Choose a name for an alien.")
# Common sayings through the story by characters
question = 'Then, she asked, "Do you want to dance with me?"'
saying_2 = 'Yeeeeeeeeehawwwwwwwww!'
saying_3 = 'yeah, whatever'
saying_4 = 'zippidy zap zeep!'
# Use multiple line string for the common saying
dance = """And they danced
danced,
danced the night away.
All night. All day."""

# Use different formatting string methods to create story
print('Once upon a time,', name_1, 'woke up and wanted to dance.')
print(f'The problem was that {name_1} did not have anyone to dance with. So sad.')
print('{} has some friends that might want to dance with her. Their names are {}, {}, and {}.'.format(name_1, name_2, name_3, name_4))

print(f'First, {name_1} went to see {name_2} at the cowboy range.')
print(question)
print('He said, "{0} {0}"'.format(saying_2))
print(dance)

print('Next,', name_1, 'went to ask', name_3, 'at her house if she wanted to dance.', name_3,'is always at home watching Netflix.')
print(f'{name_1} went up to {name_3}.', question)
print('{} was not sure. She was a little undecided, but with the help of {} who said, "{}" Katie finally said {}.'.format(name_3, name_2, saying_2, saying_3))
print(dance)

print(f'Finally, {name_1} knew that she needed alien overlord, {name_4}, to complete her dance party.')
print('So, {}, {}, and {} went to {} in his spaceship to ask him to party that day.'.format(name_1, name_2, name_3, name_4))
print(f'{name_1} went up to Overlord {name_4}.', question)
print('He thought about it long and hard and asked what the other friends had to say.')
print('{} said, "{}" and {} said, "{}" so {} said, "{}"'.format(name_2, saying_2, name_3, saying_3, name_4, saying_4))
print('(In English, it means "of course!")')
print(dance)
print('The End.')
