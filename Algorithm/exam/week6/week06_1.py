# import sys
#
# n = int(sys.stdin.readline().strip())
# # n = int(input())
# mod = []
# while True:
#     div = n // 2
#     mod.append(n % 2)
#     n = div
#     if div <= 1:
#         mod.append(div)
#         break
# mod.reverse()
# print(''.join(map(str, mod)))


print(bin(int(input()))[2:])