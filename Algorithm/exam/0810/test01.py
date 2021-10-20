# Generator
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n     # return 과 달리 여기까지 실행 중이던 값을 내보내는 것 그리고 함수는 종료되지 않음


g = get_natural_number()
for _ in range(0, 100):
    print(next(g))  # 다음값 생성
