class Simple(object):
    def __init__(self):
        self.response = 'Hello'

new_object = Simple()
print(new_object.response)



class Pet(object):
    def __init__(self, name, species, color):
        self.name = name
        self.species = species
        self.color = color

gary = Pet('Gary', 'snail', 'purple')
garfield = Pet('Garfield', 'cat', 'yellow')
scooby_doo = Pet('Scooby Doo', 'dog', 'brown')
norman = Pet('Norman', 'doge', 'cream')





pets = []

while True:
    pets.append(Pet(input('Name?  '), input('Species?  '), input('Color?  ')))
    if input('Continue? Y/N  ').lower() == 'n':
        break

for pet in pets:
    print(f"{pet.name} is a {pet.species}")






class Human(object):

    def __init__(self, name, age, gender, alive):
        self.name = name
        self.age = age
        self.gender = gender
        self.alive = alive

people = []

for x in range(5):
    people.append(Human(input('name? '), input('age? '), input('gender? '), input('alive? ')))
