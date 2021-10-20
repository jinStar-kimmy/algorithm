# a = [1, 7, 8, 9, 10, 50, 11]
#
# add = 0
# for i in range(len(a)):
#     add += a[i]
#     print(add)
#
# print("---------------------------------------")
#
# i = 0
# add = 0
# while i < len(a):       # while i < 7:          1 < 7               2 < 7               3 < 7
#     add += a[i]         # 0 = 0 + a[0] (1)      1 = 1 + a[1] (7)    8 = 8 + a[2] (8)    16 = 16 + a[3] (9)
#     print(add)          # print(1)              print(8)            print(16)           print(16)
#     i += 1              # 0 = 0 + 1             1 = 1 + 1           2 = 2 + 1           3 = 3 + 1
# print("---------------------------------------")
#
#
# # a = [1, 7, 8, 9, 10, 50, 11]
# add = 0
# for i in a:         # for i in [1, 7, 8, 9, 10, 50, 11]
#     add += i        # 0 = 0 + 1  ->   1 = 1 + 7     -> 8 = 8 + 8    -> 16 = 16 + 9    -> 25 = 25 + 10
#     print(add)      # print(1)          print(8)
#
#
# print("---------------------------------------")
# i = 0
# add = 0
# while a:
#     add += a[i]
#     print(add)
#     i += 1
#     if i >= len(a):
#         break


# 짝수의 합, 홀수의 합
# 짝수의 리스트를 만드는 함수 1개, 홀수의 리스트를 만드는 함수 1개를 만든다
# 짝수의 리스트를 받아와서 합을 구하는 함수 1개, 홀수의 리스트를 받아와서 합을 구하는 함수 1개

# Hint !
# def total_even(lst_a_from_main):
#     pass
#
#
# def total_odd(lst_a_from_main):
#     pass
#
#
# def lst_even(get_a_from_total_even):
#     pass
#
#
# def lst_odd(get_a_from_total_even):
#     pass
# 저 잠시.. 조금만 저희 쉬는시간을 가질까요? 죄송합니다~~~~~~ 금방 올게요 !
# 별찍기 해볼까요~


# 2중 for 문
# 구구단 출력


# 홀수 구구단 출력
# for i in range(1, 10):
#     if i % 2 != 0:
#         for j in range(1, 10):
#             print(str(i) + "*" + str(j) + "=" + str(i*j))
#
# a = [[10, 20], [30, 40], [50, 60]]
# '''
# 출력형식
# 10 20
# 30 40
# 50 60
# '''
# for i in a:
#     for j in i:
#         print(j, end=' ')
#     print()


#
# # 문장 안에서 t의 개수를 출력해라
# def t_count(char):
#     cnt = 0
#     my_first_string = ["In type annotations you can now use built-in collection types such as list and dict as generic types instead of importing the corresponding capitalized types (e.g. List or Dict) from typing. Some other types in the standard library are also now generic, for example queue.Queue."]
#     for i in my_first_string:
#         for j in i:
#             if j == char:
#                 cnt += 1
#     return cnt
#
#
# if __name__ == '__main__':
#     print(t_count('t'))



#
# # 문장 안에서 대,소문자 h의 개수를 출력해라
# my_string = [['Hello'], ['Hi-hi-hi'], ['Heaven']]
#
# cnt = 0
# for i in my_string:
#     for j in i:
#         for k in j:
#             if k == 'H' or k == 'h':
#                 cnt += 1
# print(cnt)
#
#
#
# s = [['Hi'], ['my'], ['name'], ['is'], ['K']]
# # 출력 형식: Hi my name is K


'''
*
**
***
****
*****
'''
# for i in range(1, 6):
#     j = 0
#     while j < i:
#         print('*', end='')
#         j += 1
#     print()

# for i in range(1, 6):
#     for _ in range(i):
#         print('*', end='')
#     print()


# a = [1, 11, 10, 9, 8, 50, 7]

'''
00000
0
00000
0
00000
'''
'''
  12345     = j
1 00000
2 0
3 00000
4 0
5 00000
"
i
'''
# for i in range(5):
#     if i % 2 == 0:
#         for _ in range(5):
#             print(0, end='')
#         print()
#     else:
#         print(0)
# '''
# 00000
#     0
# 00000
#     0
# 00000
# '''
#
# for i in range(5):
#     for j in range(5):
#         if i % 2 == 0:
#             print(0, end='')
#         else:
#             if j == 0:
#                 print(0, end='')
#             elif j == 4:
#                 print(0, end='')
#             else:
#                 print(end=' ')
#     print()


def get_even_total(lst):    # [5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1]
    even_total = 0

    # 짝수를 가져온다 -> get_even()함수를 사용해서 짝수를 가져온다.
    my_even = get_even(lst)
    print("짝수 리스트:", my_even)
    for i in my_even:   # [2, 56, 34, 6]
        even_total += i

    return even_total   # 98


def get_odd_total(lst):  # [5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1]
    odd_total = 0
    # 홀수를 가져온다 -> get_odd()함수를 사용해서 홀수를 가져온다.
    my_odd = get_odd(lst)   # [5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1]
    print("홀수 리스트: ", my_odd)
    for i in my_odd:    # [5, 7, 9, 11, 21, 3, 1]
        odd_total += i

    return odd_total    # 57


def get_even(lst_number):   # [5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1]
    even_lst = []

    for i in lst_number:
        if i % 2 == 0:
            even_lst.append(i)

    return even_lst     # 짝수 리스트


def get_odd(number_lst):    # [5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1]
    odd_lst = []

    for i in number_lst:
        if i % 2 != 0:
            odd_lst.append(i)

    return odd_lst


def get_total(lst):     # [5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1]
    # 짝수의 합을 가져온다   -> get_even_total() 함수를 이용한다.
    total_even = get_even_total(lst)
    print('total of even = ', total_even)   # 2 + 56 + 34 + 6 = 98

    print()

    # 홀수의 합을 가져온다   -> get_odd_total() 함수를 이용한다.
    total_odd = get_odd_total(lst)  # 57
    print('total of odd = ', total_odd)    # 5 + 7 + 9 + 11 + 21 + 3 + 1 = 57

    return total_even + total_odd    # 짝수와 홀수의 합을 리턴한다. 98 + 57


if __name__ == '__main__':
    total = get_total([5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1])
    print(total)
