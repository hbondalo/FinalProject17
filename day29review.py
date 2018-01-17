gatsby = {'Author': 'F. Scott Fitzgerald', 'Genre': 'Realistic Fiction'}
rithmatist = {'Author': 'Brandon Something', 'Genre': 'Fantasy/Adventure'}
books = {'The Great Gatsby': gatsby, 'The Rithmatist': rithmatist}

def find(title):
    if title in books:
        print(books[title])
    else:
        print('Not in dictionary.')