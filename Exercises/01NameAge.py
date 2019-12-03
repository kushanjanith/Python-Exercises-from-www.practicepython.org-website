import datetime

name = input("Your Name: ")
age = int(input("Age: "))
copies = int(input("How many copies do you want?: "))

now = datetime.datetime.now()

newAge = now.year + (100 - age)

for i in range(copies):
    print(f"Hi, {name}. You'll be 100 years old by the year {newAge}\n")