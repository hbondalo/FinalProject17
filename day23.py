import random

results = {}

for n in range(5000):
    die = random.randint(1, 20)
    if die in results.keys():
        results[die] += 1
    else:
        results[die] = 1

for n in range(20):
    print(f'{n + 1}: {results[n + 1]}')