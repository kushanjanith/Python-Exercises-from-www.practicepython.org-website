import random

a = random.sample(range(1, 10), 5)
b = random.sample(range(1, 10), 6)

list = [i for i in a if i in b and i]

print(list)