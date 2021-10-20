words = "dream"
for s in words:
    print(s)


for n in words:
    if n.isupper():     # 해당 문자가 대문자일 때
        print(n.lower())    # 소문자로 바꾸기
    else:
        print(n.upper())    # 대문자로 바꾸기

q1 = {"봄": "딸기", "여름": "수박", "가을": "사과", "겨울": "귤"}
for k in q1.keys():
    if k == '가을':
        print(q1[k])

for k, v in q1.items():
    if k == '가을':
        print(v)

for k, v in q1.items():
    if v == '사과':
        print(k, v)
        break


a, b, c = 12, 6, 18
max_num = 12

if b > a:
    max_num = b
if c > b:
    max_num = c
print(max_num)


s = '881012-2345678'
if int(s[7]) % 2 == 0:
    print("여자")
else:
    print("남자")

# 정을 제외하고 출력
q3 = ['갑', '을', '병', '정']
for i in q3:
    if i == '정':
        continue
    else:
        print(i, end=' ')

print()
# 5글자 이상 출력
q4 = ["nice", "study", "python", "ananconda", "!"]
for v in q4:
    if len(v) >= 5:
        print(v)

# 소문자만 출력
q5 = ['A', 'b', 'c', 'D', 'e', 'F', 'G', 'h']
for v in q5:
    if v.islower():
        print(v)

# 대문자는 소문자로, 소문자는 대문자로 출력
q6 = ['A', 'B', 'c', 'D', 'e', 'F', 'G', 'h']
for v in q6:
    if v.isupper():
        print(v.lower())
    else:
        print(v.upper())

    # for 앞에 x는 res.append(x) 라는 뜻
res = [x for x in range(1, 101) if x % 2 != 0]
print(res)

my_res = []
for i in range(1, 101):
    if i % 2 != 0:
        my_res.append(i)
print(my_res)
