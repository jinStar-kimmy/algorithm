import math

# 에라토스 테네스의 체
def solution(n):
    arr = [True for _ in range(n+1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i * j] = False
                j += 1

    return len([i for i in range(2, n+1) if arr[i]])


print(solution(10))

'''
0~17 - True
for 2~5:   i = 2~4
j = 2
4 * 2 <= 17
[4, 6, 8, 9, 10, 12, 14, 15, 16] = False

return 2, 3, 5, 7, 11, 13, 17
'''