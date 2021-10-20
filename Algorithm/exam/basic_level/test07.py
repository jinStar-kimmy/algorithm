'''
BCDEFGHIJ K  L   M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
12345678910  11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 
JAN
9
1
13

JEROEN
9
1
4
1
17  /  9
1
14  /  12
1
4
1
13  /  13
'''


def solution(name):
    answer = 0
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    for i in name:
        # if name[alpha.index(i):alpha.index(i) + 2] == 'A':
        #     answer += 0
        # else:
        #     answer += 1

        if i > alpha[int(len(alpha)/2)]:
            # print(len(alpha) - alpha.index(i))
            answer += (len(alpha) - alpha.index(i))
        else:
            # print(alpha.index(i))
            answer += alpha.index(i)
    # if 'A' in name:
    #     answer += (len(name) - 1 - name.count('A'))
    # else:
    #     answer += (len(name) - 1)
    return answer


print(solution("JEROEN"))  # 56
print()
print(solution("JAN"))  # 23
print()
# 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1
print(solution("ZAAAZZZZZZZ"))  # 15
print()
# 0 1 1 1 000..000 1 1 1 1
print(solution("ABAAAAAAAAABB"))  # 7
print()
print(solution("AABAAAAAAABBB"))  # 11
print()
print(solution("BBBAAB"))  # 9
print()
print(solution("ZAAAZAAAAAA"))  # 6
print()
print(solution("NNAAAAANNN"))  # 70
print()
print(solution("ABABAAAAAAABA"))
