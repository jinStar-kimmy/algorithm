'''for 문을 이용해서 1~10 까지의 숫자 중 홀수만 출력하기. 단, if문은 쓰지 말 것'''
# for i in range(1, 11, 2):  # hint: range 함수를 이용할 것
#     print(i)

# hint
# for i in range(0, len(number)):
#     if number[i] % 2 == 0:
#         cnt += 1
#         print("짝수")
#     else:
#         cnt02 += 1
#         print("홀수")
''' for 문과 if 문을 이용해서 1~50까지의 숫자 중 3으로 나누어 떨어지는 숫자를 구하시오'''
# for i in range(1, 51):
#     if i % 3 == 0:
#         print(i)
#     else:
#         print("아니요")
''' n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오. '''
''' 3 -> 6 '''
# n = 5
# for i in range(n, 0, -1):
#     print('*' * i)
#
#

# i = 0
# while i < 11:            # i = 1, 2, 11
#     print(i, end=' ')    # 0, 1 ,10
#     i += 1               # 1, 2, 11
#
# print()
#
# j = 0
# while j < 11:           # 10
#     j += 1              # 11
#     print(j, end= ' ')  # 10, 11
'''
# # number = [11, 2, 6, 9, 25, 7, 3, 23]
# '''
# x = 5
# a = [1, 10, 4, 9, 2, 3, 8, 5, 7, 6]
#
# print(max(a))

'''
마구잡이로 정렬된 리스트를 받아서 오름차순으로 정렬을 해봅시다
for 문 
while 문
2가지 버전으로 작성할 것
'''
# lst = [5, 2, 3, 4, 1]
# temp = []
# for i in range(0, len(lst)):                # i = 1 lst[1] = 2
#     for j in range(i+1, len(lst)):
#         if lst[i] > lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]
#             print(lst)
#     print("============")
# print(lst)


'''1부터 입력된 수 n까지의 합을 while문으로 작성해라'''


'''1부터 입력된 수 n까지의 수 중에서 홀수와 짝수를 각 배열에 담아 출력해라'''
# lst1 = []   # 홀수 배열
# lst2 = []   # 짝수 배열
# i = 1
# n = 10


''' 1부터 입력된 수 n까지의 수 중에서 n의 짝수 첫번째 배열에, 홀수 두번쩨 배열에 담아 출력해라 '''

# lst1 = []   # 홀수 배열
# lst2 = []   # 짝수 배열
# i = 1
# n = 50


def prn():     # n = 50
    lst1 = []   # 홀수 배열
    lst2 = []   # 짝수 배열

    for i in range(1, 51):     # n + 1 = 51
        if i % 2 == 0:
            lst2.append(i)
        else:
            lst1.append(i)

    print(lst1)
    print(lst2)

# 1 ~ 50까지
if __name__ == '__main__':
    prn()



# while i <= n:
#     if i % 2 == 0:
#         lst1.append(i)
#     elif i % 5 == 0:
#         lst2.append(i)
#     i += 1
#
# print(lst1)
# print(lst2)
