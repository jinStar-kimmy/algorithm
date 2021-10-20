# 짝수의 합, 홀수의 합
# 짝수의 리스트를 만드는 함수 1개, 홀수의 리스트를 만드는 함수 1개를 만든다
# 짝수의 리스트를 받아와서 합을 구하는 함수 1개, 홀수의 리스트를 받아와서 합을 구하는 함수 1개





# def make_lst(n):    # 10
#     lst = []
#     for i in n:
#         pass        # 1~10(n)까지 숫자가 담긴 리스트를 만든다
#
#     my_even = make_even(lst)  # 1~10까지 숫자가 담긴 리스트를 짝수만 담긴 리스트로 바꿔준다.
#
#     return my_even
#
#
# def make_even(lst):     # 1~10까지 담긴 리스트가 들어옴  ->  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     lst_even = []
#     for i in lst:
#         pass        # 짝수가 담긴 리스트를 만든다.
#
#     return lst_even

def get_even_total(lst):    # [5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1]
    even_total = 0

    # 짝수를 가져온다 -> get_even()함수를 사용해서 짝수를 가져온다.
    for i in lst:   # [5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1]
        my_even = get_even(i)   # 0

        if my_even == 0:
            pass

        print(my_even, end='   ')
        even_total += my_even   # 0 + 0

    return even_total


def get_odd_total(lst):     # [5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1])
    odd_total = 0
    # 홀수를 가져온다 -> get_odd()함수를 사용해서 홀수를 가져온다.
    for i in lst:
        my_odd = get_odd(i)     # [5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1])

        if my_odd == 0:
            continue

        print(my_odd, end='   ')
        odd_total += my_odd

    return odd_total


def get_even(number):    # 5
    if number % 2 == 0:
        return number
    else:
        return 0


def get_odd(number):
    if number % 2 != 0:
        return number
    else:
        return 0


def get_total(lst):
    # 짝수의 합을 가져온다   -> get_even_total() 함수를 이용한다.
    total_even = get_even_total(lst)
    print('=  ', total_even)   # 0 + 0 + 2 + 0 + 0 + 56 + 34 + 0 + 6 + 0 + 0 = 98

    # 홀수의 합을 가져온다   -> get_odd_total() 함수를 이용한다.
    total_odd = get_odd_total(lst)
    print('=  ', total_odd)    # 5 + 7 + 9 + 11 + 21 + 3 + 1 = 57

    return total_even + total_odd    # 짝수와 홀수의 합을 리턴한다.


# 리티스를 인자값으로 받아 리스트 값들의 합을 구하는 함수를 만들어보자.
def hap(my_lst): # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = 0
    for i in my_lst:
        total += i
    print("aaaaa:", total)
    # return total    # total = 55


def get_sum(my_lst):    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = 0
    for i in my_lst:
        total += i      # 1~10까지의 합
    print("total:", total)
    return total        # 55를 리턴


def make_lst_a(n):  # n = 10
    lst = []
    for i in range(1, n+1):     # 1 ~ 10
        lst.append(i)   # 리스트에 1부터 10까지 추가된다.
    print("=======>", lst)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = get_sum(lst)    # get_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("======================", total)
    return total


# make_lst(10)
if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    hap(a)
    # result = hap(a)
    # print(result)
    print("-----------------------------")
    # n이라는 정수를 받아서 1부터 n까지의 수를 리스트로 만드는 함수를 만들고, 이 함수를 가지고 리스트의 합을 구하는 함수를 만들자
    m_result = make_lst_a(10)   # m_reuslt = 55
    print(m_result)
    # total = get_total([5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1])
    # print(total)


