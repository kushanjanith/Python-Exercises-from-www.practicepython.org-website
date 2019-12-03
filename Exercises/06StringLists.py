import math

str = input("Word: ")

#################### MY CODE ###################

# len = len(str)
#
# count = 0
# eCount = 0
# x = -1
#
# for c in str:
#     count = count + 1
#     if count > math.ceil(len / 2):
#         break
#     elif c == str[x]:
#         x = x - 1
#         eCount = eCount + 1
#         continue
#
# if eCount == math.ceil(len / 2):
#     print(f"'{str}' is a palindrome!")
# else:
#     print(f"'{str}' is not a palindrome!")

################# With reversed() function #################

reversedStr = ''.join(reversed(str))

if reversedStr == str:
    print(f"'{str}' is a palindrome!")
else:
    print(f"'{str}' is not a palindrome!")