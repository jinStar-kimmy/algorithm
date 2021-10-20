# def combine_list(str_list):
#                     # 바꿔줄 데이터 타입, 리스트, 튜플
#     combine_str = ' '.join(map(str, str_list))
#     prn(combine_str)
#
#
# def prn(combine_str):
#     print(combine_str)

# def my_function(str_list):
#     for my_string in str_list:
#         m_prn(my_string)
#
#
# def m_prn(my_str):
#     if len(my_str) >= 5:
#         print(my_str)


def upper_lower_case(lst):
    for charcater in lst:
        if charcater.islower():
            return charcater.upper()
        else:
            return charcater.lower()


if __name__ == '__main__':
    # string_lst = ['Hi', 'My', 'name', 'is', 'HJ']
    # combine_list(string_lst)
    # q2 = ["nice", "study", "python", "ananconda", "!"]
    # my_function(q2)

    q3 = ['A', 'B', 'c', 'D', 'e', 'F', 'G', 'h']
    upper_lower_case(q3)
    my_res = ''.join(map(str, q3))
    print(my_res)
    res = list(map(upper_lower_case, q3))
    print(res)
    a, b = map(int, input().split())
    print(a, b)
    # 함수호출 -> 소문자를 대문자로 대문자를 소문자로 만들어주는 함수 !
    # 호출은 한번 ! 함수는 2개를 만들어보자 !








    # q4 = {"봄": "딸기", "여름": "수박", "가을": "사과", "겨울": "귤"}
