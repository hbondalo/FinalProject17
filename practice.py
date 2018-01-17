def cleaned_string(string_to_clean):
    for letter in string_to_clean:
         if letter not in 'aeiou':
            print(letter, end='')


text= "i hope that in this year to come, you make mistakes. because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. you're doing things you've never done before, and more importantly, you're doing something.".lower()

def clean_text(text_to_clean, forbidden):
    for letter in text_to_clean:
        if letter not in forbidden:
            print(letter, end= '')
# cleaned_text = ''

# split_text = cleaned_text.split()
# split_text.sort()

def split_string(cleaned):


quantities = word_counter(word_list)
print(quantities)

def word_counter(words_to_count):
    counted = {}
    for word in words_to_count:
        if word in counted:
            counted[word] += 1
        else:
            counted[word] = 1
    return counted