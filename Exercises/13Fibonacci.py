num = int(input("How many Fibonacci numbers?: "))
list = []


def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


for i in range(1, num+1):
    list.append(fib(i))


print(list)