# def solution(s):
#     # answer = ''
#     div = int(len(s) // 2)
#     if len(s) % 2 == 0:
#         answer = s[div-1:div+1]
#     else:
#         answer = s[div]
#     return answer
#
#
# result = solution("abcedfeg")
# print(result)
#
# a, b = map(int, input().strip().split(' '))
# for _ in range(b):
#     for _ in range(a):
#         print('*', end='')
#     print()
#
# print()
#
# for _ in range(b):
#     print('*' * a)
#
# print()
#
# a = 5
# for i in range(a):
#     if i % 2 != 0:
#         print(0)
#     else:
#         print('0'*a)
#
# print()
#
# for j in range(a):
#     if j % 2 != 0:
#         print(' ' * (a-1), end='')
#         print(0)
#     else:
#         print('0'*a)

# def solution(a, b):
#     if a == b:
#         return a
#     if a > b:
#         a, b = b, a
#     else:
#         pass
#     answer = sum(range(a, b+1))
#     return answer
#
#
# print(solution(3, 5))

# def solution(n):
#     answer = '수박'
#     return (answer * n)[:n]
#
# print(solution(5))
#
# result = ['수', '박', '수', '박']
# result = ''.join(map(str, result))
# print("리스트 합치기 ! ---> ", result)
# # 출력 결과: 리스트 합치기 ! --->  수박수박


# def solution(seoul):
#     return "김서방은 " + str(seoul.index("Kim")) + "에 있다"
#
#
# print(solution(["Jane", "Kim"]))


# def solution(arr1, arr2):
#     answer = []
#     for x, y in zip(arr1, arr2):
#         i = []
#         for a, b in zip(x, y):
#             i.append(a + b)
#         answer.append(i)
#     # while i < len(arr1):
#     #     j = 0
#     #     while j < len(arr1[i]):
#     #         answer.insert(i,j, )
#     #         answer[i][j].append(arr1[i][j] + arr2[i][j])
#     #         print(answer)
#     #         j += 1
#     #     i += 1
#     return answer
#
#
# result = solution([[1, 2], [2, 3]], [[3, 4], [5, 6]])
# print(result)

# def solution(arr):
#     answer = list()
#     answer.append(arr[0])
#
#     for num in arr:
#         if answer[-1] != num:
#             answer.append(num)
#
#     return answer
#
#
# print(solution([1, 1, 3, 3, 0, 1, 1]))

# def solution(s):
#     return True if s.lower().count('p') == s.lower().count('p') else False
#
#
# print(solution("PyY"))
