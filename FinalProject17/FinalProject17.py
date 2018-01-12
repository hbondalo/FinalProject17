#Start
class Teacher(object):
    """Teacher class for each level played in the game"""

    def __init__(self, teacher, subject, special, health):
        """Parameters of class for each teacher"""
        self.teacher = teacher
        self.subject = subject
        self.special = special
        self.health = health

T_1 = Teacher("Mrs. Kipp", "Intro to Engineering & Digital Modeling", "T-Square", 100)
T_2 = Teacher("Mr. Pantaleo", "SIA", "Gravity", 100)
T_3 = Teacher("Mr. Merkl", "Biology", "Dinosaurian Society", 100)
T_4 = Teacher("Mrs. O'Connor", "Technology and Design", "The Power of AutoCAD", 100)
T_5 = Teacher("Dr. Fang", "Physics I", "Degree from Columbia University", 100)
T_6 = Teacher("Ms. Monroy", "Chemistry", "Dimensional Analysis", 100)
T_7 = Teacher("Mr. Raite", "AP Chemistry", "...", 100)
T_8 = Teacher("Mr. Straut", "AP Calculus", "....", 100)
T_9 = Teacher("Mrs. Gerstein", "Introduction for Programming", "Python", 100)
T_10 = Teacher("Mrs. Pinto", "Modern American Literature", "...", 100)
T_11 = Teacher("Mrs. Valley", "U.S. History I", "Her Strength", 100)
T_12 = Teacher("Mr. Sanservino", "U.S. History II", "POP QUIZ", 100)
T_13 = Teacher("Mr. Rafalowski", "Principal", "MakerSpace", 100)


name = input("What is your name? \n")
n = input(f"Welcome, {name}, to your worst nightmare. It's time to escape Magnet! Are you ready? ")

if n == "yes":
    print("It doesn't matter. You're going to play. Let's begin the journey.\n")
else:
    print("It doesn't matter. You're going to play. Let's begin the journey.\n")

print(f"""Good morning, {name}! I have some good news and some bad news. Congratulations! Today's graduation!
Bad news is that you're stuck in Magnet, and you need to figure out a way to get to the AIT gym in time for graduation!
You don't want to be THAT kid.


BRINNNGGGGG!! BRINGGGGGGGG!!

That's the bell!""")

print("""1. Go to class.
2. Run to the bathroom.
3. Pull the fire alarm.
4. Cry.""")
x = input("Choose which number you want to choose. ")

if x == "1" or "1.":
    print("Go.")
elif x == "2"