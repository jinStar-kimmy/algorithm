"""
"17"	3
"011"	2
print(list("17"), list("011"))
"""
from itertools import permutations


# def solution(numbers):
#     answer = 0
#     lst = list(numbers)
#     lst_length = len(lst)
#
#     for i in range(len(lst)):
#         for j in range(len(lst)):
#             # if i != j:
#             lst.append(str(lst[i])+str(lst[j]))
#             if len(lst[-1]) > lst_length:
#                 lst.pop()
#     lst = map(int, list(set(lst)))
#     lst = sorted(lst)
#     for i in range(len(lst)):
#         check = 0
#         if int(lst[i]) == 0 or int(lst[i]) == 1:
#             continue
#         for j in range(2, int(lst[i])):
#             if int(lst[i]) % int(j) == 0:
#                 check = 1
#         if check == 0:
#             answer += 1
#     print(lst)
#     print(answer)
#     return answer
def func_div(number):
    for i in range(2, int(number)):
        if int(number) % int(i) == 0:
            return False
    return True


def solution(numbers):
    answer = []
    lst_n = []
    lst_numbers = []
    # lst_numbers = list(numbers)
    # print(lst_numbers)
    for i in range(1, len(numbers)+1):
        lst_n = list(map(''.join, permutations(numbers, i)))
        lst_numbers.extend(lst_n)
        # for j in lst_n:
        #     lst_numbers.append(int(j))
    # lst_numbers = list(map(''.join, permutations(list(numbers))))
    lst_numbers = list(set(lst_numbers))
    print(lst_numbers)

    for i in range(len(lst_numbers)):
        if int(lst_numbers[i]) == 0 or int(lst_numbers[i]) == 1:
            continue

        # for j in range(2, int(lst_numbers[i])):
        #     if int(lst_numbers[i]) % int(j) == 0:
        #         check = False
        #         continue
        # if check is True:
        #     answer.append(int(lst_numbers[i]))
        if func_div(lst_numbers[i]):
            answer.append(int(lst_numbers[i]))
    answer = list(set(answer))
    print(answer)
    return len(answer)


print(solution("17"))
print(solution("011"))
# solution("0113")
