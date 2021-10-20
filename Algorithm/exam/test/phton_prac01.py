# ================ if 조건문 =============
# number01 = 31
#
# if number01 % 2 == 0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")

'''
3~5월 :봄
6~8월 : 여름
9~11월 : 가을
12월 ~ 2월: 겨울
'''
#
#
# month = input("입력하세요: ")
# month = int(month)
# if 3 <= month <= 5:
#     print("봄이야")
# elif 6 <= month <= 8:
#     print("여름이야")
# elif 9 <= month <= 11:
#     print("가을이야")
# if month in range(1, 13):
#     print("겨울이야")
# else:
#     print("잘못입력된 값입니다")

'''
============== 반복문 ==============
'''


# 1~10 까지 반복을 하는데 반복 숫자를 i라는 변수에 집어넣어서 i가 짝수인지 홀수인지 구해라
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i, "는 짝수입니다")
#     else:
#         print(i, "는 홀수입니다")
# 리스트를 받아와서 리스트에 들어있는 값들이 짝수인지 홀수인지 구하라

# number = [11, 2, 6, 9, 25, 7, 3, 23]
# cnt = 0
# cnt02 = 0
# for i in number:
#     if i % 2 == 0:
#         cnt += 1
#         print("짝수")
#     else:
#         print("홀수")
#         cnt02 += 1
#
# for i in range(0, len(number)):
#     if number[i] % 2 == 0:
#         cnt += 1
#         print("짝수")
#     else:
#         cnt02 += 1
#         print("홀수")
#
# print("짝수는 ", cnt)
# print("홀수는 ", cnt02)

# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# lst1.extend(lst2)
# cnt = []
# print(lst1)
# for i in range(0, len(lst2)):
#     lst1.append(lst2)
# for i in range(0, len(lst1)):   # [3, 4, 5, 6]
#     cnt.append(lst1.pop(0))
#     # print(lst1, len(lst1))
#     print(cnt)
# print(lst1)

'''
1~9 단 구구단
'''


# for i in range(1, 10):          # i = 10
#     for j in range(1, 10):      # j = 1 2 3 4 ,9
#         print(i, "   x   ", j, "     =     ", i * j)
#


'''
2개의 list를 비교해서 같은 값이 몇개 있는지 출력하자
'''
# lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lst2 = [2, 4, 6, 8]
# cnt = 0
# for i in lst1:
#     for j in lst2:
#         print(i, j)
#         if i == j:
#             cnt += 1
# print(cnt)


number = [11, 2, 6, 9, 25, 7, 3, 23, 20]
for i in number:
    if i % 2 == 0 or i % 3 == 0:
        if i % 2:
            print(i, "는 2의 배수")
        elif i % 3:
            print(i, "는 3의 배수")
    else:
        print(i, "는 아무것도 아님")
