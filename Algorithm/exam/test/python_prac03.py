'''
숫자 start와 end를 입력받아 start부터 end까지 중에서 홀수를 리턴하고 홀수의 합을 구하는 함수를 만들어보자
'''


# 1~10까지 중에서 홀수가 담긴 리스트를 리턴해라
# def prn(start, end):
#     lst_odd = list()
#     for i in range(start, end+1):
#         if i%2 != 0:
#             lst_odd.append(i)
#     return lst_odd
#
#
# # 홀수가 담긴 리스트를 입력받아 합을 구해라
# def hap(start, end):
#     lst_odd = prn(start, end)
#     result_hap = 0
#     for i in lst_odd:
#         result_hap += i
#     return result_hap


# def prn(start, end):
#     lst_odd = list()
#     for i in range(start, end+1):
#         if i % 2 != 0:
#             lst_odd.append(i)
#     result = hap(lst_odd)
#     return result
#
#
# def hap(lst_odd):
#     result_hap = 0
#     for i in lst_odd:
#         result_hap += i
#     return result_hap

def hap(get_result):
    my_hap = 0
    for i in get_result:
        my_hap += i
    return my_hap


def calculator(result):
    length = len(result)
    avg = hap(result)
    final_avg = avg/length
    return final_avg


def get_student_no(st_no):
    student_info = {'123456': [70, 80, 90], '12347': [80,90,10]}
    print(student_info.keys())
    print(student_info.values())
    my_result = []
    for key in student_info.keys():
        if key == st_no:
            print(student_info.get(key))
            my_result = student_info.get(key)
    grade = calculator(my_result)
    if grade >= 90:
        print('A')
    elif grade >= 80:
        print('B')
    elif grade >= 70:
        print('C')
    else:
        print('D')
    # return grade


if __name__ == '__main__':
    # result = prn(1, 10)
    # print(result)
    student_no = 's123456'
    get_student_no(student_no[1:])
