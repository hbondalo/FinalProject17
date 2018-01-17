class Book(object):
    """Book class"""

    def __init__(self, author, title, summary):
        self.author = author
        self.title = title
        self.summary = summary

a = Book('Brandon Sanderson', 'The Rithmatist', 'Chalk boiiiiis save the world')
b = Book('F. Scott Fitzgerald', 'The Great Gatsby', 'Down with Gatsby')
c = Book('Ernest Cline', 'Ready Player One', 'Basically the futureeeeee')

def describe(self):
    print(f"{self.title} - {self.summary}")
    print(self.summary)

def identify_self(self):
    print(self.title)






class Human(object):
    """Human class"""

    def __init__(self, name, gender):
        """Parameters of class"""
        self.name = name
        self.gender = gender

h = Human('Hannah', 'girl')
p = Human('Preston', 'boy')
m = Human('Monge', 'girl')
g = Human('Griffin', 'boy')

def introduce(self):
    print(f'This Human is {self.name}, who is a {self.gender}. Say hello!')