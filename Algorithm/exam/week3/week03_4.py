# from itertools import combinations
#
#
# def solution(numbers, target):
#     cnt = 0
#     for i in range(2, len(numbers)):
#         res = list(combinations(numbers, i))
#         for j in res:
#             if target == sum(j):
#                 cnt += 1
#
#     # res = list(permutations(numbers, target))
#     print(cnt)
#     answer = 0
#     return answer


from collections import deque


def solution(numbers, target):
    # answer = 0
    # n = len(numbers)
    # queue = [[numbers[0], 0], [-1 * numbers[0], 0]]
    # while queue:
    #     temp, idx = queue.pop()
    #     idx += 1
    #     if idx < n:
    #         queue.append([temp + numbers[idx], idx])
    #         queue.append([temp - numbers[idx], idx])
    #     else:
    #         if temp == target:
    #             answer += 1
    answer = [0]
    for i in numbers:
        sub = []
        for j in answer:
            sub.append(j+i)
            sub.append(j-1)
        answer = sub
    return answer.count(target)


print(solution([1, 1, 1, 1, 1], 3))
