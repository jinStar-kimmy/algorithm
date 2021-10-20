def solution(d, budget):
    answer = 0
    d.sort()

    if sum(d) == budget:
        return len(d)
    elif (len(d) == 1) and d[0] <= budget:
        return len(d)

    for i in range(1, len(d) + 1):
        if sum(d[:i]) > budget:
            break

        if sum(d[:i]) <= budget:
            answer = len(d[:i])

    return answer


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
print(solution([100, 101], 101))
'''
(ex) d = [100], budget = 101, result = 1
'''