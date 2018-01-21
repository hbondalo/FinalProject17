#Make sure to include an empty dictionary to start a blank inventory.
#Import math and randomfor future math questions in the game later
import random
import math

#List each key with its value in different lines to be organized.
inventory = {
    "ID": 0,
    "Calculator" : 0,
    "100 on Sanservino's Pop Quiz": 0,
    "Graduation Cap and Gown": 0,
    "Extra Credit": 0
    "Engineering Notebook": 0
    "Scale": 0}


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
q_01 = Question("How often should I save my work? Every __ minutes.\n\n", "5", "YOU LOST ALL OF YOUR WORK! Try again. ", "Good work! You saved your file just in time!")
q_02 = Question("A bike accelerates uniformly from rest to a speed of 7.10 m/s over a distance of 35.4 m. Determine the acceleration of the bike to 3 sig figs. (Just give the number. Already understood that it is in m/s^2)\n\n", "0.712\n", "GOTCHA! Try again.", "Ugh. You're too smart.")
q_03 = Question("The __________ is the powerhouse of the cell.\n\n", "mitochondria\n".lower(), "C'mon it's a meme. Try again. ", "Correctamundo!")
q_04 = Question("An input function on Python always returns a _____.\n\n", "string\n".lower(), "Are you kidding me? Try again. ", "Ah yes! Correct, my good sir!")
q_05 = Question("How many periods are in the second paragraph of page 376?\n\n", "26\n", "Mwahahaha. 0 for you. Try again. ", "Dang it. Mr. Sanservino wanted to fail you, but you got it right....")
q_06 = Question("What is considered as 'the heart of Magnet'? (One-word answer)\n\n", "makerspace\n".lower(), "It's literally right next to Mrs. Gerstein's room...Try again. ", "YAYYYYYYYYY!!!!!!")



#Quick function when user needs to see what's in their inventory.
def show_inventory():
    input("Let's check your inventory. Press enter. ")
    for key, value in inventory.items():
        print(f"{key}: {value}")


#For adding an item into the inventory
def add_item():
    inventory[random.choice(inventory.keys())] += 1


#Create a function when the user is asked a question in the game.
def ask(q):
    response = input(q.question)
    for response in range(5):
        if response == q.answer:
            print(q.correct)
        elif response != q.answer:
            response = input(q.wrong).lower()
        else:
            print("I don't know I'm bad at coding.")


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
        print("I guess we'll just skip this, because you're incompetent.")


def future():
    if sum(inventory.values()) <= 10:
        print("Yikes. Looks like the college made a mistake and you're not going to your dream school.\nBetter luck next time...oh wait")
    elif sum(inventory.values()) <= 20:
        print("hi")
    elif sum(inventory.values()) <= 30:
        print("hi")
    elif sum(inventory.values()) <= 40:
        print("hi")
    else:
        print("perfect")




#Begin game with allowing the user to input their name for a more personal experience.
name = input("What is your name? \n")
n = input(f"Welcome, {name}, to your worst nightmare. It's time to escape Magnet! Are you ready? ")

if n == "yes":
    print("It doesn't matter. You're going to play. Let's begin the journey.\n")
else:
    print("It doesn't matter. You're going to play. Let's begin the journey.\n")


#The beginning of the game includes some introduction.
input(f"""Good morning, {name}! I have some good news and some bad news. Congratulations! Today's graduation!
Bad news is that you're stuck in Magnet, and you need to figure out a way to get to the AIT gym in time for graduation!
You don't want to be THAT kid. Press enter. """)

input("""-----

BRINNNGGGGG!! BRINGGGGGGGG!! That's the bell!\nPress enter.""")

choose("Go straight to period 1/2.", "Hm. Interesting choice.", "Pull the fire alarm.", "Whoops! The fire alarm doesn't work! Time for period 1/2.", "Cry.", "ThErE iS No CrYiNg HeRe! Pull it together! Get to class!")


###################THIS IS LEVEL 1##########################

input(f"\nLooks like you've landed in {T_01.teacher}'s room. This is the {T_01.subject} room. Welcome to Level 1. Press enter. ")


input("""\nTo pass each level, you must answer a question correctly.
If you correctly answer a question, you get a random item added to your inventory for extra points!
The amount of extra points you earn determines your life after high school if you get to graduation!
Each item has various point amounts, but you won't know how much each item is worth until the very end!
Press enter to continue. """)

input("\nHere comes your first question! Press enter to continue. ")

ask(q_01)


print(f"As you defeat {T_01.teacher}, she uses her {T_01.special} to try to stop you! What do you do?\n")

choose("Allow the T-Square to hit you.", "You do not get any items to add to your inventory. Sorry.", "Jump and dodge the T-Square.", "Excellent choice! Items will be added to your inventory!", "Block the T-Square with an architectural scale that is next to you.", "Effective enough for you to have item(s) added to your inventory!")
add_item()
show_inventory()


###################THIS IS LEVEL 2##########################

input("\nLet's see where we're headed to next. Press enter.")


input("\nOh my! It's {T_02.teacher}! What's he's doing here?\nIt looks like this is Level 2!\nHere comes the question!")

ask(q_02)



###################THIS IS LEVEL 3##########################





###################THIS IS LEVEL 4##########################




###################THIS IS LEVEL 5##########################





###############THIS IS LEVEL 6/BOSS LEVEL####################







#End of the game narrative/Conclusion
