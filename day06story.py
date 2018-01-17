# Assign names of characters to variables
noun_1 = "Vanna"
noun_2 = "Virendra"
noun_3 = "Katie"
noun_4 = "Arthur"
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
print('Once upon a time,', noun_1, 'woke up and wanted to dance.')
print(f'The problem was that {noun_1} did not have anyone to dance with. So sad.')
print('{} has some friends that might want to dance with her. Their names are {}, {}, and {}.'.format(noun_1, noun_2, noun_3, noun_4))

print(f'First, {noun_1} went to see {noun_2} at the cowboy range.')
print(question)
print('He said, "{0} {0}"'.format(saying_2))
print(dance)

print('Next,', noun_1, 'went to ask', noun_3, 'at her house if she wanted to dance.', noun_3,'is always at home watching Netflix.')
print(f'{noun_1} went up to {noun_3}.', question)
print('{} was not sure. She was a little undecided, but with the help of {} who said, "{}" Katie finally said {}.'.format(noun_3, noun_2, saying_2, saying_3))
print(dance)

print(f'Finally, {noun_1} knew that she needed alien overlord, {noun_4}, to complete her dance party.')
print('So, {}, {}, and {} went to {} in his spaceship to ask him to party that day.'.format(noun_1, noun_2, noun_3, noun_4))
print(f'{noun_1} went up to Overlord {noun_4}.', question)
print('He thought about it long and hard and asked what the other friends had to say.')
print('{} said, "{}" and {} said, "{}" so {} said, "{}"'.format(noun_2, saying_2, noun_3, saying_3, noun_4, saying_4))
print('(In English, it means "of course!")')
print(dance)
print('The End.')








