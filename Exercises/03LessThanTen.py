a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def less(x):
    return [item for item in a if item < x]


num = int(input("Number: "))
print(less(num))

# for item in a:
#     if item < 10:
#         new.append(item)
# print(new)
