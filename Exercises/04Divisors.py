import math

num = int(input("Number: "))
list = []
x = num / 2

for i in range(1,math.floor(x)):
    if num % i == 0:
        list.append(i)
print(list)