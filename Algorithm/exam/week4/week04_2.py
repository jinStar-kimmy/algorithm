# a = 'ZZZZZ'
# b = 36
# #   (35 * 36 ^ 4) + (35 * 36 ^ 3) + (35 * 36 ^ 2) + (35 * 36 ^ 1) + (35 * 36 ^ 0)
# print(len(a))
# print(2 * 2 ** 3)
#
# j = 1
# total = 0
# for i in a:
#     if i.isdigit():     # 숫자인지 확인
#         total += i * b ** (len(a) - j)
#     else:
#         total += ((ord(i)-55) * (b ** (len(a)-j)))
#     j += 1
# print(total)
import sys


convert_to, notation = sys.stdin.readline().split()
notation = int(notation)
length = len(convert_to)

total = 0
for i, v in enumerate(convert_to):
    v = int(v) if v.isdigit() else ord(v) - 55
    total += v * notation ** (length - i - 1)

sys.stdout.write(str(total))        # 메모리 초과를 대비해서 print문 대신 사용

# if i.isdigit():
#     total += i * int(notation) ** (len(convert_to) - j)
# else:
#     total += (ord(i) - 55) * int(notation) ** (len(convert_to) - j)

# if __name__ == '__main__':
#     n, b = input().split()
#     b = int(b)
#     length = len(n)
#     total = 0
#
#     for i, v in enumerate(n):
#         v = int(v) if v.isdigit() else ord(v) - 55
#         total += v * b ** (length - i - 1)
#
#     print(total)