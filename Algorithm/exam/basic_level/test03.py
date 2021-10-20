def solution(s, n):
    answer = ''
    for i in s:
        if i.isalpha():
            if i.islower():
                if ord(i) + n > 122:
                    answer += chr(96 + (ord(i) + n - 122))
                else:
                    answer += chr(ord(i) + n)
            else:
                if ord(i) + n > 90:
                    answer += chr(64 + (ord(i) + n - 90))
                else:
                    answer += chr(ord(i) + n)
        else:
            answer += i
    return answer


print(solution("a B z", 4))


'''
"AB"	    1	"BC"
"z"	        1	"a"
"a B z"	    4	"e F d"
"bC",      25   "aB" 
'''