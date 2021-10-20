import datetime


def solution(a, b):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    answer = days[datetime.date(2016, a, b).weekday()]
    return answer


print(solution(1, 3))

'''
import datetime
import time

def getDay_c(a,b,c):
    #리스트에 월 ~ 일까지 담아둠
    daylist = ['월', '화', '수', '목', '금', '토', '일']
    #datetime.date(2019,1,20).weekday() 
    #weekday() 라는 메소드의 반환 값은 월요일은 0, 화요일은 1 이므로
    #요일의 값이 리스트의 0번째 값인 daylist[0] = '월' 방식으로 가져온다.
    return daylist[datetime.date(a,b,c).weekday()]

# 사용자에게 입력 받음 
y = int(input("연 : "))
m = int(input("월 : "))
d = int(input("일 : "))

ddd = getDay_c(y,m,d)   # 입력한 날'
print(f"입력 한 {y}.{m}.{d} 는 {ddd}요일 입니다.")
'''