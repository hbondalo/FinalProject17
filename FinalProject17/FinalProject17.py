#Start by creating functions for the user to check their inventory.
#Make sure to include an empty dictionary to start a blank inventory.
#Import math for future math questions in the game later
import math

inventory = {}
def check_inventory():
    storage_q = input("Would you like to check your inventory?").lower()
    if storage_q == "yes":
        print(inventory)
        use_inventory
    else:
        print("Guess you don't want to check your inventory. Let's continue.")

def use_inventory():
    input("Would you like to use an item in your inventory?").lower()
    if inventory == []:
        print("There's nothing in your inventory! Sorry!\nTime to answer the question!")
    else:
        print("fix this")



#Create a class for the teachers included in the game.
#Parameters include their subject and special personality.
class Teacher(object):
    """Teacher class for each level played in the game"""

    def __init__(self, teacher, subject, special):
        """Parameters of class for each teacher"""
        self.teacher = teacher
        self.subject = subject
        self.special = special

T_01 = Teacher("Mrs. Kipp", "Intro to Engineering & Digital Modeling", "T-Square")
T_02 = Teacher("Mr. Pantaleo", "SIA", "Gravity")
T_03 = Teacher("Mr. Merkl", "Biology", "Dinosaurian Society")
T_04 = Teacher("Mrs. O'Connor", "Technology and Design", "The Power of AutoCAD")
T_05 = Teacher("Dr. Fang", "Physics I", "Degree from Columbia University")
T_06 = Teacher("Ms. Monroy", "Chemistry", "Dimensional Analysis")
T_07 = Teacher("Mrs. Gerstein", "Introduction for Programming", "Python")
T_08 = Teacher("Mrs. Valley", "U.S. History I", "Her Strength")
T_09 = Teacher("Mr. Sanservino", "U.S. History II", "POP QUIZ")
T_10 = Teacher("Mr. Rafalowski", "Principal", "MakerSpace")


class Question(object):
    """Question class for all questions and answers presented in this game"""

    def __init__(self, q, a):
        """Parameters where 'q' is question and 'a' is its answer"""
        self.q = q
        self.a = a

q_01 = Question("What is the name of the computer-aided design program used for 2-D and 3-D design and drafting?", "AutoCAD".lower())



#Begin game with allowing the user to input their name for personal experience.
name = input("What is your name? \n")
n = input(f"Welcome, {name}, to your worst nightmare. It's time to escape Magnet! Are you ready? ")

if n == "yes":
    print("It doesn't matter. You're going to play. Let's begin the journey.\n")
else:
    print("It doesn't matter. You're going to play. Let's begin the journey.\n")

print(f"""Good morning, {name}! I have some good news and some bad news. Congratulations! Today's graduation!
Bad news is that you're stuck in Magnet, and you need to figure out a way to get to the AIT gym in time for graduation!
You don't want to be THAT kid.

-----

BRINNNGGGGG!! BRINGGGGGGGG!! That's the bell!\n""")

print("""1. Go to class.
2. Run to the bathroom.
3. Pull the fire alarm.
4. Cry.""")
x = input("Type the number you want to choose. ")

if x == "1":
    print("You turn right into Mrs. Kipp's class. This should be interesting")
elif x == "2":
    print("Mr. Rafalowski caught you cutting class. Go to class.")
elif x == "3":
    print("Fire alarm broke! Uh oh! Looks like you have to go to class.")
elif x == "4":
    print("ThErE iS nO cRyInG! Back to class!")
else:
    print("You want to type an invalid response? Fine. We'll choose one for you.")

print("-----\n10 MINUTES LATER\n-----\n")


###################THIS IS LEVEL 1##########################

print(f"""Looks like you've landed in {T_01.teacher}'s room.
This is the {T_01.subject} room.
Welcome to Level 1.




To pass each level, you must answer two questions correctly.
After each question is presented, you may be able to check your inventory.
Some items might help you surpass levels.


Here comes your first question!""")

print(q_01.q)
check_inventory()
use_inventory()
input(q_01.q)
while q_01.q != q_01.a:
    q_01.q = input("WRONG! Try again!").lower()
print("Excellent! This was the first program in Magnet to enhance your engineering knowledge!\nMrs. Kipp is proud...BUT NOT SATISFIED!")










