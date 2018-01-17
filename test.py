q_1 = input("Is this going to work? ")
a_1 = "yes".lower()
health = 100


while q_1 != a_1:
    health -= 2
    q_1 = input(f"You're health is now {health}. Try again. ")
print(f"Yay! Health is now {health}!")
