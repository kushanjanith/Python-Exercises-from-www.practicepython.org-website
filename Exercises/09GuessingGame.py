import random

ran = random.randint(1,9)
ex = True
count = 0

while ex:
    guess = input("Guess the number: ")
    count += 1
    if guess == 'exit':
        ex = False
        count -= 1
    elif int(guess) > ran:
        print("Guessed too high")
    elif int(guess) < ran:
        print("Guessed too low")
    else:
        print("Exactly!")

print(f"Guessed count = {count}")