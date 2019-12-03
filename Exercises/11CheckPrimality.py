import math

def prime():
    num = int(input("Number: "))
    list = []
    x = num / 2

    for i in range(1, math.floor(x)):
        if num % i == 0:
            list.append(i)

    if len(list) == 1:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")


prime()