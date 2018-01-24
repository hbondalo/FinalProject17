from random import randint

class Character(object):
    def __init__(self, name, life):
        self.name = name
        self.life = life

Bob = Character("Bob", 100)

def attack():
    while Bob.life > 0:
        input("Hit enter to make his health go down!")
        Bob.life -= randint(0,20)
        print(f"{Bob.name}'s life is now {Bob.life}! Keep going!")
    print(f"You've defeated {Bob.name}!")

print(f"Your mission: Attack {Bob.name}")
attack()