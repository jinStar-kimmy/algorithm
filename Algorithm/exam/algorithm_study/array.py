# product of array except self
def multiply(myList):   # 1, 2, 3, 4
    output = []
    p = 1
    # 왼쪽 곱셈
    for i in range(len(myList)):
        output.append(p)    #output:  1 1 2 6
        p = p * myList[i]   # 1 1 2 6

    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(myList) - 1, -1, -1):
        output[i] = output[i] * p  # 6*1 =6,    2*4= 8,     1*12=12,      1*24=24
        p = p * myList[i]   # 1 4 12 24

    return output


result = multiply([1, 2, 3, 4])
print(result)
