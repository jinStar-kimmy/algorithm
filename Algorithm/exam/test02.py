def solution(progresses, speeds):
    answer = []
    day = 0
    for i in range(len(progresses)):
        if progresses[i] + speeds[i] * day >= 100:
            answer[-1] += 1
        while progresses[i] + speeds[i] * day < 100:
            day += 1
            if progresses[i] + speeds[i] * day >= 100:
                answer.append(1)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))    # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))   # [1, 3, 2]
