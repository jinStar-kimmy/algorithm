"""
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,

                     1, 3, 2, 4, 2, 1, 2, 3, 4, 5, 2, 4, 2, 1, 3, 4, 5, 2, 4, 4, 5, 2, 3, 4
                     3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1
                        o        o              o           o

                     2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5
                2번:       o     o     o           o     o

                1번: 1  2  3  4  5  1  2  3  4  5  1  2  3  4  5  6  1  2  3  4  5  1  2  3
                    o        o     o  o   o  o  o                      o      o  o

[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
"""


def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    count1 = 0
    count2 = 0
    count3 = 0
    for index, value in enumerate(answers):
        print(index, value)

    for i in range(len(answers)):
        if len(a) <= i:
            a.extend(a)
        if answers[i] == a[i]:
            count1 += 1

        if len(b) <= i:
            b.extend(b)
        if answers[i] == b[i]:
            count2 += 1

        if len(c) <= i:
            c.extend(c)
        if answers[i] == c[i]:
            count3 += 1

    max_count = max(count1, count2, count3)

    if max_count == count1:
        answer.append(1)

    if max_count == count2:
        answer.append(2)

    if max_count == count3:
        answer.append(3)

    return answer


# print(solution([1,2,3,4,5]))
# print(solution([1,3,2,4,2]))
print(solution([1,3,2,4,2,1,2,3,4,5,2,4,2,1,3,4,5,2,4,4,5,2,3,4]))

