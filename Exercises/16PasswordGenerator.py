import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = ('!', '@', '#', '$', '%', '&', '*')
password = []


def randString(x, y, z):
    for i in range(x):
        password.append(random.choice(letters))

    for i in range(y):
        password.append(random.choice(numbers))

    for i in range(z):
        password.append(random.choice(symbols))

    return ''.join(password)


x = int(input("Enetr the number of letters: "))
y = int(input("Enetr the number of digits: "))
z = int(input("Enetr the number of special characters : "))

print(randString(x, y, z))