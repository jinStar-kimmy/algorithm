def solution(n):
    if n > 1:
        return n * solution(n-1)
    else:
        return 1


n = int(input())
print(solution(n))