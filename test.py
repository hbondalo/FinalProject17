import random
a = {'hey': 0, 'hi': 5}


def add():
    a[random.choice(a.keys())] += 1

add()
print(a)