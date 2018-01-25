#Make sure to include an empty dictionary to start a blank inventory.
#Import math and randomfor future math questions in the game later
import random

#List each key with its value in different lines to be organized.
inventory = {
    "ID": 0,
    "Calculator" : 0,
    "100 on Sanservino's Pop Quiz": 0,
    "Graduation Cap and Gown": 0,
    "Extra Credit": 0,
    "Engineering Notebook": 0,
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

#Variables for the 6 total questions asked in the game.
q_01 = Question("How often should I save my work? Every __ minutes.\n\n", "5", "YOU LOST ALL OF YOUR WORK! Try again. ", "Good work! You saved your file just in time!")
q_02 = Question("The __________ is the powerhouse of the cell.\n\n", "mitochondria", "C'mon it's a meme. Try again. ", "Correctamundo!")
q_03 = Question("For every action, there is an equal and opposite _____.\n\n", "reaction", "GOTCHA! Try again.", "Ugh. You're too smart.")
q_04 = Question("An input function on Python always returns a _____.\n\n", "string", "Are you kidding me? Try again. ", "Ah yes! Correct, my good sir!")
q_05 = Question("How many periods are in the last paragraph of page 595?\n\n", "3", "Mwahahaha. 0 for you. Try again. ", "Dang it. Mr. Sanservino wanted to fail you, but you got it right....")
q_06 = Question("What is considered as 'the heart of Magnet'? (One-word answer)\n\n", "makerspace", "It's literally right next to Mrs. Gerstein's room...Try again. ", "YAYYYYYYYYY!!!!!!")



#Quick function when user needs to see what's in their inventory.
#A for loop is used to print out an organized list of the items and the corresponding value in the dictionary.
def show_inventory():
    inventory[random.choice(list(inventory.keys()))] += random.randint(1,10)
    input("Let's check your inventory. Press enter. ")
    for key, value in inventory.items():
        print(f"{key}: {value}")


#For adding an item into the inventory
#import random is useful here to randomly add to a random value in the dictionary




def attempts_left(a):
    print(f"You have {a} attempts left.")

#Create a function when the user is asked a question in the game.
def ask(q):

    attempts = 3
    response = input(q.question).lower()
    while attempts >= 0:
        if response == q.answer:
            print(q.correct)
            break
        elif response != q.answer and attempts > 1:
            attempts -= 1
            attempts_left(attempts)
            response = input(q.wrong).lower()
        else:
            print("GAME OVER. YOU DIDN'T GRADUATE.")
            quit()


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

#This is the last function used at the very end, should the user finish the game.
#With given
def future():
    if sum(inventory.values()) <= 10:
        print("""Yikes. Looks like the college made a mistake and you're not going to your dream school.
You end up being single for the rest of your life and can't find happiness!
Good news is that you buy a cat. You name him Gunther.
Better luck next time...oh wait...this is the end of the game. Whoops. Sorry.
        Thanks for playing! :)""")
    elif sum(inventory.values()) <= 20:
        print("""Well, you just BARELY got through high school, and you end up going to college.
However, at college, you flunk 3 classes, which makes it hard for you to even get a job.
You and your nagging wife, Sherley, live in an abandoned RV in Alabama now, so that's fun.
Thanks for playing! :)""")
    elif sum(inventory.values()) <= 30:
        print("""Oooooo looks like you turned out all right. You live a normal lifestyle after earning a degree at your college.
It took you a couple of times to find the right spouse, but looks like you did it!
Your job's pretty stable, except things got rocky during the recession.
Overall, nice job at living life. Very adequate.
Thanks for playing! :)""")
    elif sum(inventory.values()) <= 40:
        print("""Mhm, you're living life pretty well if I do say so myself.
You pass your classes in an ivy league school, and get your dream job.
The only problem in your life is deciding which mansion to buy with your loving spouse, children, and dog, named Rufus.
High school did you well, and you're living life to the fullest!
Thanks for playing! :)""")
    else:
        print("""WOW! You're life is perfect after high school!
You pass your classes in the ivy league school with FLYING COLORS!
In college, you meet the love of your life and travel around the world happily.
Your job rakes up good money and your children are as successful as you are.
You have no worries in life, and everything is perfect.
Thanks for playing! :)""")




#Begin game with allowing the user to input their name for a more personal experience.
#Use the input function.
name = input("What is your name? \n")
input(f"Welcome, {name}, to your worst nightmare. It's time to escape Magnet! Are you ready? ")
print("It doesn't matter. You're going to play. Let's begin the journey.\n")



#The beginning of the game includes some introduction. Input function is used for the user to just press enter when finished reading.
input(f"""Good morning, {name}! I have some good news and some bad news. Congratulations! Today's graduation!
Bad news is that you're stuck in Magnet, and you need to figure out a way to get to the AIT gym in time for graduation!
You don't want to be THAT kid. Press enter. """)

input("""-----

BRINNNGGGGG!! BRINGGGGGGGG!! That's the bell!\nPress enter.""")

choose("Go straight to period 1/2.", "Hm. Interesting choice.\n", "Pull the fire alarm.", "Whoops! The fire alarm doesn't work! Time for period 1/2.\n", "Cry.", "ThErE iS No CrYiNg HeRe! Pull it together! Get to class!\n")


###################THIS IS LEVEL 1##########################
input(f"\nLooks like you've landed in {T_01.teacher}'s room. This is the {T_01.subject} room. Welcome to Level 1. Press enter. ")


input("""\nTo pass each level, you must answer a question correctly.
If you correctly answer a question, you get a random item added to your inventory for extra points!
The amount of extra points you earn determines your life after high school if you get to graduation!
Press enter to continue. """)

input("\nHere comes your first question! Press enter to continue. ")

ask(q_01)


print(f"As you defeat {T_01.teacher}, she uses her {T_01.special} to try to stop you! What do you do?\n")

choose("Allow the T-Square to hit you.", "Looks like you dodged it! Nice! Here's some items.\n", "Jump and dodge the T-Square.", "Excellent choice! Items will be added to your inventory!\n", "Block the T-Square with an architectural scale that is next to you.", "Effective enough for you to have item(s) added to your inventory!\n")
show_inventory()


###################THIS IS LEVEL 2##########################
input("\nLet's see where we're headed to next. Press enter.")


input(f"\nOh my! It's {T_02.teacher}! What's he's doing here?\nIt looks like this is Level 2!\nHere comes the question!")

ask(q_02)

print(f"Oh no! Just as you tried to escape, {T_02.teacher} uses the {T_02.special} in hopes of stopping you!\n")

choose("Stomp out the Dinosaurian Society", "Ahhhh you wiped them out! Get some items!\n", "Use the power of the mitochondria to stop him", "You did it!!! YAY!!!!!!!\n", "Play country music. ", "How'd you know that he loves that?! You pass!\n")
show_inventory()


###################THIS IS LEVEL 3##########################
input("\nMan, that was a tough one. I wonder where we're going next. Press enter. ")

input(f"\nWOAH! IT'S {T_03.teacher} in the {T_03.subject} ROOM! OH MY! SHE'S CHALLENGING YOU.\nTHIS IS LEVEL 3!\nHERE'S THE QUESTION! ")

ask(q_03)

print(f"Looks like you did it!\n\nOH NO! SHE USES {T_03.special}! What do you do?")

choose("Hide yo wife. Hide yo kids.", "Effective. Yes. Items for you.\n", "Use your dad's doctorate degree.", "Reasonable. Here's some items.\n", "Pull out a stick.", "Ah yes, you pull out her number and she answers incorrectly. Items for you!\n")
show_inventory()


###################THIS IS LEVEL 4##########################
input(f"\nLet's continue on with our journey.\nWell, would you look who it is! It's {T_04.teacher} in the {T_04.subject} class!\nShe has a question for you to pass Level 4! Press enter. ")

ask(q_04)

print(f"WOWOWOW! You did it!\n\nBut uh oh! She tries using {T_04.special} to stop you! What shall you do?")

choose("""git commit -am "Save changes" """, "Excellent Python skills. Have some items!\n", "Use the 3-D printer to generate a gift for her.", "She loves it! Have some items!\n", "Just whip it.", "Effective. Carry on with more items.\n")
show_inventory()


###################THIS IS LEVEL 5##########################
input("\nI CAN ALMOST SEE THE LIGHT. LET'S GO! PRESS ENTER!!! ")

print(f"NO!!! {T_05.teacher} IS TRYING TO STOP US IN HIS {T_05.subject} CLASS! HE'S GIVING US A POP QUIZ FOR LEVEL 5! Press enter. ")

ask(q_05)

print(f"AH YES! You did it!\n\nBut uh oh! He tries using {T_05.special} to stop you! What shall you do?")

choose("Play Despacito.", "He loves that song! Get some items!\n", "Challenge him to a 1v1 in basketball and juke him out.", "Ah, yes, you broke his ankles! Get some items!\n", "Buy him Chick-fil-A.", "He is satisfied and gives you items.\n")
show_inventory()

###############THIS IS LEVEL 6/BOSS LEVEL####################
input("\nWE MADE IT DUDES!!!!!!!!!!!! PRESS ENTER! ")

input(f"{T_06.teacher}?!?!?!? WHAT ARE YOU DOING HERE? I'M TRYING TO GRADUATE!\nIt looks like this is THE FINAL LEVEL!!! Press enter. ")

ask(q_06)

print(f"You make your final escape!\n\nOh no! He tries using {T_06.special} to stop you! What shall you do?")

choose("Ace the PARCC test.", "Efficient. Have a pizza party and more items!\n", "Show him your ID.", "He allows you to pass because you won't get a LOP. Gather items.\n", "Take a selfie with him.", "Ah, yes. Excellent. Get some items!\n")
show_inventory()


#End of the game narrative/Conclusion
input("""\n\nCongratulation! "Looks like we madeee ittttt!"
Let's see what your extra points says about your future!!\nPress enter!\n\n""")
future()
quit()