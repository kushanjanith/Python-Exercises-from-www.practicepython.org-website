import random


def game():
    print("Welcome to the Cows and Bulls Game!\n")
    rand = random.randint(999,9999)
    cow = 0
    while cow != 4:
        cow = 0
        bull = 0
        number = input("Enter a 4 digit number: ")
        userInput = [int(i) for i in str(number)]
        randomNumber = [int(j) for j in str(rand)]

        for item in randomNumber:
            itemIndex = randomNumber.index(item)
            if item == userInput[itemIndex]:
                cow += 1
            else:
                bull += 1

        print(f"{cow} cows, {bull} bulls\n")
    print("Congratulations!")


game()