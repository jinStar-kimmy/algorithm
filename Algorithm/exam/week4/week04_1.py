# import math
# import sys
#
# while True:
#     number = sys.stdin.readline().rstrip()
#     if number == '0':
#         break
#     else:
#         total = 0
#         j = 0
#         for i in number:
#             # answer = factorial(len(number) - j)
#             total += (int(i) * math.factorial(len(number) - j))
#             j += 1
#         print(total)


import sys


def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1


while True:
    number = sys.stdin.readline().rstrip()
    if number == '0':
        break
    else:
        total = 0
        j = 0
        for i in number:
            total += (int(i) * factorial(len(number) - j))
            j += 1
        print(total)
