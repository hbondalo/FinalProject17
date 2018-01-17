#Make sure to include an empty dictionary to start a blank inventory.
#Import math and randomfor future math questions in the game later
import math
import random
inventory_initial = {
    'ID': 0,
    'Calculator' : 0,
    'Google Search': 0,
    'Back of the Textbook': 0,
    'Extra Credit': 0}

inventory = {
    'ID': 0,
    'Calculator' : 0,
    'Google Search': 0,
    'Back of the Textbook': 0,
    'Extra Credit': 0}

#Quick function when user needs to see what's in their inventory.
def show_inventory():
    storage_q = input("Would you like to check your inventory? ").lower()
    if storage_q == "yes":
        for key, value in inventory.items():
            print(f"{key}: {value}")
            use_inventory()
    else:
        print('Okay.\nContinue on, then.')




#Create a function for when the user wants to use an item to answer a question.
def use_inventory():
    i = input("Would you like to try to use an item in your inventory? ").lower()
    if i == "yes".lower():
        if inventory == inventory_initial:
                print("There's nothing in your inventory! Sorry!\nTime to answer the question!")
        else:
            u = input("What item would you like to use? ").lower()
            item(u)
    elif i == "no".lower():
        print("Alrighty then.")
    else:
        print("YOU DON'T DESERVE ACCESS TO YOUR INVENTORY. CONTINUE.")




#For adding an item into the inventory
def add_item(i_one, i_two, i_three):
    a = input(f"Choose an item to add to your inventory\n{i_one}\n{i_two}\n{i_three}")
    if a == i_one:
        inventory.append[i_one] += 1
    elif a == i_two:
        inventory.append[i_two] += 1
    elif a == i_three:
        inventory.append[i_three] += 1
    else:
        print("You are incompetent. You lost your priveleges.")

#Create a class for the teachers included in the game.
#Parameters include their subject and special personality.
class Teacher(object):
    """Teacher class for each level played in the game"""

    def __init__(self, teacher, subject, special):
        """Parameters of class for each teacher"""
        self.teacher = teacher
        self.subject = subject
        self.special = special

#List of all the teachers with their subjects and special ability that can inhibit the user to continue the game.
T_01 = Teacher("Mrs. Kipp", "Intro to Engineering & Digital Modeling", "T-Square")
T_02 = Teacher("Mr. Merkl", "Biology", "Dinosaurian Society")
T_03 = Teacher("Dr. Fang", "Physics I", "Degree from Columbia University")
T_04 = Teacher("Mrs. Gerstein", "Introduction for Programming", "Python")
T_05 = Teacher("Mr. Sanservino", "U.S. History II", "POP QUIZ")
T_06 = Teacher("Mr. Rafalowski", "Principal", "MakerSpace")


#Create a class for all of the questions with respective answers.
#Include the response if the user gets the question correct or wrong in the other parameters.
class Question(object):
    """Question class for all questions and answers presented in this game"""

    def __init__(self, question, answer, wrong, correct):
        """Parameters where 'q' is question and 'a' is its answer"""
        self.question = question
        self.answer = answer
        self.wrong = wrong
        self.correct = correct

#Variables for the 20 total questions asked in the game.
q_01 = Question("How often should I save my work? Every __ minutes.\n", "5", "YOU LOST ALL OF YOUR WORK! Try again. ", "Good work! You saved your file just in time!")
q_02 = Question("A bike accelerates uniformly from rest to a speed of 7.10 m/s over a distance of 35.4 m. Determine the acceleration of the bike to 3 sig figs. (Just give the number. Already understood that it is in m/s^2)\n", "0.712", "GOTCHA! Try again.", "Ugh. You're too smart.")
q_03 = Question("The __________ is the powerhouse of the cell.\n", "mitochondria\n".lower(), "C'mon it's a meme. Try again. ", "Correctamundo!")
q_04 = Question("An input function on Python always returns a _____\n.", "string".lower(), "Are you kidding me? Try again. ", "Ah yes! Correct, my good sir!")
q_05 = Question("How many periods are in the second paragraph of page 376? ", "26", "Mwahahaha. 0 for you. Try again. ", "Dang it. Mr. Sanservino wanted to fail you, but you got it right....")
q_06 = Question("What is considered as 'the heart of Magnet'? (One-word answer) ", "makerspace".lower(), "It's literally right next to Mrs. Gerstein's room...Try again. ", "YAYYYYYYYYY!!!!!!")


#Create a function when the user is asked a question in the game.
def ask(q):
    print(q.question.upper())
    show_inventory()
    use_inventory()
    response = input(q.question)
    while response != q.answer:
        response = input(q.wrong).lower()
    print(q.correct)


#Create a function for whenever the user has a choice of decision for either items or actions in the game.
def choose(first_c, first_r, second_c, second_r, third_c, third_r):
    print(f"1. {first_c}\n2. {second_c}\n3. {third_c}\n")
    x = input("Type the number you want to choose. ")
    if x == "1":
        print(first_r)
    elif x == "2":
        print(second_r)
    elif x == "3":
        print(third_r)
    else:
        print("You want to type an invalid response? Fine. We'll choose one for you.")




#Begin game with allowing the user to input their name for personal experience.
name = input("What is your name? \n")
n = input(f"Welcome, {name}, to your worst nightmare. It's time to escape Magnet! Are you ready? ")

if n == "yes":
    print("It doesn't matter. You're going to play. Let's begin the journey.\n")
else:
    print("It doesn't matter. You're going to play. Let's begin the journey.\n")


#The beginning of the game includes some introduction.
print(f"""Good morning, {name}! I have some good news and some bad news. Congratulations! Today's graduation!
Bad news is that you're stuck in Magnet, and you need to figure out a way to get to the AIT gym in time for graduation!
You don't want to be THAT kid.

-----

BRINNNGGGGG!! BRINGGGGGGGG!! That's the bell!\n""")

choose("Go straight to period 1/2.", "Hm. Interesting choice.", "Pull the fire alarm.", "Whoops! The fire alarm doesn't work! Time for period 1/2.", "Cry.", "ThErE iS No CrYiNg HeRe! Pull it together! Get to class!")


###################THIS IS LEVEL 1##########################

print(f"""Looks like you've landed in {T_01.teacher}'s room.
This is the {T_01.subject} room.
Welcome to Level 1.


To pass each level, you must answer a question correctly.
After each question is presented, you have a chance to check your inventory.
Some items might help you surpass questions.

Here comes your first question!""")

ask(q_01)


print (f"As you defeat {T_01.teacher}, she uses her {T_01.special} to try to stop you! What do you do?")

choose("Allow the T-Square to hit you.", "You do not get any items to add to your inventory. Sorry.", "Jump and dodge the T-Square.", "Excellent choice! Choose two items to add to your inventory!", "Block the T-Square with an architectural scale that is next to you.", "Effective enough for you to choose one item to add to your inventory!")
add_item(inventory[0], inventory[4], inventory[1])










