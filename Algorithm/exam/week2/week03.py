"""
N: 10
N = [6 3 2 10 10 10 -10 -10 7 3]
M: 8
M = [10 9 -5 2 3 4 5 -10]


3 0 0 1 2 0 0 2


5
1 1 1 1 1
4
1 1 1 1
"""

from sys import stdin

#
# def solution_02(n, number_n, m, number_m):
#     answer = [0] * m
#     for i in range(m):
#         for j in range(n):
#             if number_m[i] == number_n[j]:
#                 answer[i] += 1
#     answer = ' '.join(map(str, answer))
#     return answer
#
#
# def solution(n, number_n, m, number_m):
#     dict_m = dict.fromkeys(number_m, 0)
#     number_m = sorted(number_m)
#     for i in range(n):
#         left = 0
#         right = n - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if number_m[mid] == number_n[i]:
#                 dict_m[number_m[mid]] += 1
#                 break
#             elif number_m[mid] < number_n[i]:
#                 left = mid + 1
#             elif number_m[mid] > number_n[i]:
#                 right = mid - 1
#     answer = ' '.join(map(str, list(dict_m.values())))
#     return answer
#

# print(solution(int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split()))))
# print(solution_02(10, [6, 3, 2, 10, 10, 10, -10, -10, 7, 3], 8, [10, 9, -5, 2, 3, 4, 5, -10]))
# print(solution_02(5, [1, 1, 1, 1, 1], 4, [1, 1, 1, 1]))

"""
N: 10
N = [6 3 2 10 10 10 -10 -10 7 3]
M: 8
M = [10 9 -5 2 3 4 5 -10]


3 0 0 1 2 0 0 2


5
1 1 1 1 1
4
1 1 1 1


count_n = int(input())
lst_n = list(map(int, input().split()))
count_m = int(input())
lst_m = list(map(int, input().split()))
"""

# count_n = 5
# lst_n = [1, 1, 1, 1, 1]
# count_m = 4
# lst_m = [1, 1, 1, 1]
# count_n = 10
# lst_n = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
# n = 8
# lst_m = [10, 9, -5, 2, 3, 4, 5, -10]


n = stdin.readline()
lst_n = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
lst_m = map(int,stdin.readline().split())
answer = []
dict_lst = dict()

for i in lst_n:
    if i in dict_lst.keys():
        dict_lst[i] += 1
    else:
        dict_lst[i] = 1

for j in lst_m:
    if j in dict_lst.keys():
        answer.append(dict_lst[j])
    else:
        answer.append(0)

answer = ' '.join(map(str, answer))

print(answer)
