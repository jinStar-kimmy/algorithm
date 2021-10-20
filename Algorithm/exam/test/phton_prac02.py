'''
함수 만들기 1
        인자를 입력받아서 다음과 같은 기능을 구현하고 출력하는 함수를 만들어보자
e.g.) 1. 더하기 함수    2. 빼기 함수    3.곱하기 함수    4. 나누기 함수
'''


def hap(a, b):
    print("여기는 합을 구하는 함수입니다.")
    minus = a - b
    return minus


def caculator(a, b, *args):
    hap = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return hap, sub, mul, div

'''
함수 만들기 2
인자를 입력받아 for 문 사용하기
    a라는 입력값과 b라는 입력값을 받아서 a부터 b까지 출력하는 함수를 만들어보자
    e.g.) a = 3,    b = 10   -> 3부터 10까지 출력하는 함수 
'''


def prn(start, end):
    lst = []
    for i in range(start, end+1):
        lst.append(i)
    return lst


# a, b를 입력받아서 a부터 b까지의 합을 구하는 함수를 만들어보자
def prn_hap(a, b):
    j = 0
    for i in range(a, b+1):
        j += i
    return j


if __name__ == '__main__':
    # a = 10
    # b = 5
    # print(a-b)
    # c = hap(5, 10)  # c = add   c = 15
    # print(c)
    # a = 15
    # a = -5
    # print(a)
    # a, b, c, d = caculator(5, 10)    # c = 15 -5 50 0.5
    # print(a, d)
    result = prn(3, 10)
    print(result, result[3])

    # map 정의 -> map(데이터 타입, 리스트 또는 튜플)  -> 리스트 또는 튜플을 앞에 정의된 데이터 타입으로 변환 시켜주는 것
    # join 정의 -> 특정 문자열 또는 리스트의 문자열 요소들을 하나로 합치는 것

    # 동작 과정
    # 1. 리스트나, 튜블 형태를 문자열로 변환 시켜준다 -> 리스트에 들어있는 요소를 하나씩 앞에 정의된 데이터 타입으로 변환한다.
    # 2. 변환된 요소들을 join 앞에 쓰여진(', ') 형식으로 묶어준다
    print(', '.join(map(str, result)))  # 3, 4, 5, 6, 7, 8, 9, 10   -> ['3', '4']
    result_a = ', '.join(map(str, result))
    print(result_a)
    print(type((str(result))))    # result 전체를 string으로 바꿔준다.  '[3,  4]'
    my_string = str(result)
    print(my_string)    # 괄호[] 까지 string으로 바꿔줌
    # 리스트 안에 있는 문자열을 join 앞에 쓰여진 형식으로 합쳐준다.
    c = ['a', 'b', 'c']
    print(', '.join(c))     # a, b, c


    # for i in result:
    #     print(i)
    # for i in range(len(result)):
    #     print(result[i])
    print(prn_hap(3, 10))



