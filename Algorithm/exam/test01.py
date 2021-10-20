def solution(prices):
    answer = [] * len(prices)
    for i in range(len(prices)):
        count = 0
        if i == len(prices) - 1:
            answer.append(count)
            break
        for j in range(i + 1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
        answer.append(count)
    return answer


print(solution([1, 2, 3, 2, 3]))   # [4, 3, 1, 1, 0]


'''
i = 0                   |   1
j = 1, 2, 3, 4          |   2, 3, 4 
c = 1, 2, 3, 4          |   1, 2, 3           
if = 1>2, 1>3, 1>2, 1>3 |   2>3, 2>2, 2>3
a = 4                   |   3

'''