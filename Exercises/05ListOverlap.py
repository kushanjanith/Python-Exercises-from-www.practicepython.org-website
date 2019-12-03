import random

a = [8,14,5,1,6,10,7,4,19,13,50]
b = [8,8,18,11,20,14,22,9,6,10,13,8,50,60]

# a = random.sample(range(1, 101), 20)
# b = random.sample(range(1, 101), 20)

# list = []

# for i in a:
#     if i in b and i not in list:
#         list.append(i)
# print(list)

list = [i for i in a if i in b and i]

print(list)