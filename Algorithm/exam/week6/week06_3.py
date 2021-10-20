def solution(phone_book):
    answer = True
    phone_book.sort()
    my_book = "".join(map(str, phone_book))
    cnt = 0

    for i in range(len(phone_book)-1):
        cnt += len(phone_book[i])
        if my_book[cnt:].startswith(phone_book[i]):
            answer = False
            return answer

    return answer


def solution_2(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True


print(solution_2(["123", "456", "789"]))
# 효율성 3, 4