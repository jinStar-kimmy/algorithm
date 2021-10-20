# my_lst = [1, 2, 3, 4, 5]
# str_lst = ['a', 'b', 'c', 'd', 'e', 'f']
#
# print(my_lst, str_lst)
# # 형식 -> del my_lst[index]
# # del은 예약어 (함수x) --> my_lst.del
# # del my_lst[4]
# # print(my_lst)
# # del str_lst[4]
# # print(str_lst)
#
# del str_lst[2:]
# print(str_lst)
# str_lst.remove('b')
#
# for i in range(0, len(my_lst)):
#     if i % 2 == 0:
#         del my_lst[i]
#         break
#
# print(my_lst)

# 단일 클래스
# 파이썬 클래스 이름은 대문자로 시작한다.
# 함수는 단어마다 _를 써서 이어준다.
#   ->  e.g.  def make_string
# class UserInfo:
#     # this.name = name
#     def __init__(self, name):
#         self.name = name
#
#     def user_info(self):
#         print("Name: ", self.name)
#
#
# user1 = UserInfo("Kim")  # 객체를 인스턴스화 시킨다.   --> 메모리에 올려 놓는다.
# print(user1.name)
# user1.user_info()
#
# user2 = UserInfo("Lee")
# print(user2.name)
# user2.user_info()
#
#
# class SelfTest:
#     def function_1():
#         print("function1 called")
#
#     def function_2(self):
#         print("function2 called")
#
#
# SelfTest.function_1()
# test = SelfTest()
# test.function_2()

class Calculator:

    def add(self, a, b):
        self.a = a
        self.b = b
        self.c = self.a + self.b
        return self.c

    def sub(self, a, b):
        self.a = a
        self.b = b
        self.result = self.a - self.b
        return self.result

    def multy(self, a, b):
        self.a = a
        self.b = b
        return self.a * self.b

    def div(self, a, b):
        self.a = a
        self.b = b
        return self.a / self.b


my_cal = Calculator()
print(my_cal.add(10, 5))
print()
print(my_cal.sub(20, 11))
print()

