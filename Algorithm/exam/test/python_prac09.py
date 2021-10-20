import numpy as np

np.random.seed(1)
myArr = np.random.randint(1, 30, 16).reshape(4, 4)
print(myArr)
total = 0
for i in myArr:
    for j in i:
        total += j

# print(total)
# print(sum(myArr))

# for i in range(len(myArr)):     # i = 2
#     for j in range(len(myArr[i])):  # len(myArr[2])) -> 4  j= 0, 3
#         if myArr[i][j] == 2:    # myArr[2][2]
#             print("2의 위치는", i, ',', j, "입니다.")

# print(np.where(myArr == 2))

# 각 요소들이 짝수인지 홀수인지 출력해라
# for i in myArr:
#     for j in i:
#         if j % 2 == 0:
#             print("짝수", end=' ')
#         else:
#             print("홀수", end=' ')
#     print()

# 각 row의 합이 짝수인지 홀수인지 출력해라

# for i, v in enumerate(myArr):     # [ 6 12 13  9], [10 12  6 16], [ 1 17  2 13], [ 8 14 29  7]
#     total = 0
#     for j in v:     # [10 12  6 16]
#         total += j
#     if total % 2 == 0:
#         print(i, "번째 row의 합은 ", total, "이고, 짝수입니다.")
#     else:
#         print(i, "번째 row의 합은 ", total, "이고, 홀수입니다.")

# total_even = 0
# total_odd = 0
# for i, v in enumerate(myArr):
#     if i % 2 == 0:
#         for j in v:
#             total_even += j
#     else:
#         for j in v:
#             total_odd += j
# print(total_odd, total_even)
# my_t = 0
# for i in range(len(myArr)):
#     for j in range(len(myArr[i])):
#         if j == 2:
#             my_t += myArr[i][j]
# print(my_t)

'''
[ 6      12     13      9 ]
[ 10     12     6      16 ]
[ 1      17     2      13 ]
[ 8      14     29      7 ]
[0][0] [0][1] [0][2] [0][3]
[1][0] [1][1] [1][2] [1][3]
[2][0] [2][1] [3][2] [3][3]
[3][0] [3][1] [3][2] [3][3]
'''

for i in range(len(myArr)):     # i =  0, 1, 2, 3
    total = 0
    for j in range(len(myArr[i])):  # j = 0, 1, 2, 3
        total += myArr[j][i]
    print(total, end='  ')

print()

# 슬라이싱
# for i in myArr:
#     for j in i[2:]:
#         print(j, end=' ')
#     print()


# my_sum = sum(myArr)
# my_total = sum(my_sum)
# print(my_sum, my_total)
# print(np.sum(myArr))
# print(myArr.sum())
# myEye = np.eye(3, k=-1, dtype=int)
# print(myEye)
#
# myEye2 = np.eye(3,5, k=2, dtype=int)
# print(myEye2)

