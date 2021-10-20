# class Solution:
#     def solution(self, number, dictionary):
#         self.number = number
#         self.dictionary = sorted(dictionary)
#         self.my_str = []
#         for i in self.number:
#             for j in self.dictionary:
#                 if int(i) == len(j):
#                     self.my_str.append(j)
#                     self.dictionary.remove(j)
#                     break
#         self.my_str = ' '.join(map(str, self.my_str))
#         return self.my_str
#
#
# if __name__ == '__main__':
#     number = "2222"
#     dictionary = ["ab","cd","ef","a","b","ab"]
#     my_solution = Solution()
#     print(my_solution.solution(number, dictionary))
'''
문제 설명
선희와 영수는 대학에서 문자열 이론을 공부하고 있다. 영수는 팰린드롬을 아주 좋아한다. 팰린드롬은 앞에부터 읽어도, 뒤에서부터 읽어도 같은 단어를 말한다. 선희는 영수를 임의의 문자열 s로 팰린드롬을 만들어 영수를 깜짝 놀래켜주고 싶어한다. 이때 선희은 문자열 s 뒤에 0개 이상의 문자를 추가해 팰린드롬을 생성하려 한다. 선희가 생성할 수 있는 가장 짧은 팰린드롬의 길이를 반환하라.

참고 / 제약 사항
s : 영어 소문자 ('a' ~ 'z')로 구성된 1~50글자의 문자열
테스트 케이스
s = "abab"리턴(정답): 5
"ababa"가 선희가 구할 수 있는 가장 짧은 팰린드롬입니다.

s = "abacaba"리턴(정답): 7
입력 자체가 이미 팰린드롬입니다.

s = "qwerty"리턴(정답): 11
모든 문자가 다릅니다.
'''
class Solution:
    def check_palindrome(self, my_str, length_str):
        self.my_str = my_str
        self.length_str = length_str
        print(self.length_str // 2)
        for i in range(self.length_str // 2):
            print(i)
            print(self.my_str[i], self.my_str[self.length_str - 1 - i])
            if self.my_str[i] == self.my_str[self.length_str - 1 - i]:
                continue
            else:
                return False
        return True

    def solution(self, s):
        self.s = s
        self.answer = 0
        # if self.s == self.s[::-1]:
        #     return len(self.s)
        if self.check_palindrome(self.s, len(self.s)):
            return len(self.s)
        else:
            for i in range(len(self.s), 0, -1):
                print(list(reversed(self.s)), i)
                if self.check_palindrome(list(reversed(self.s)), i):
                    self.answer = len(self.s) + (len(self.s) - i)
                    break

        return self.answer


if __name__ == '__main__':
    s = "abab"
    my_s = Solution()
    print(my_s.solution(s))

"""
당신은 새 물건을 판매하기에 앞서 어떻게 하면 매출을 극대화할 수 있는지 알고 싶다.
물건의 최적의 가격을 정하는 것도 여러 전략 중 하나이다.
당신은 잠재적 고객들이 지출할 수 있는 제일 높은 가격을 적은 고객 목록을 만들었다.
당신은 또한 각 고객들에게 물건을 배송하기 위해 얼마의 비용이 필요한지 알고 있다.
배송 비용은 당신이 모두 부담해야되기 때문에 배송 비용이 너무 비싸다면 그 고객에게는 물건을 팔지 않을 수도 있다.

주어진 정수배열 price과 cost에는 각각 고객 i가 지출할 수 있는 제일 높은 가격과 배송 비용이 담겨 있다.
매출을 극대화할 수 있는 물건의 가격을 반환하여라.
최적의 가격이 2가지 이상 존재한다면 더 작은 가격을 리턴하시오.
이윤을 남길 수 없다면 0을 리턴하시오.


테스트 케이스
price = [13,22,35]
cost = [0,0,0]리턴(정답): 22
13원에 물건을 팔면 3명 모두 구입할 것이다: 매출: 3*13=39
22원에 물건을 팔면 2명만 구입할 것이다: 매출: 2*22=44
35원에 물건을 팔면 1명만 구입할 것이다: 매출: 1*35=35
그러므로 22가 최적의 가격이다.


price = [13,22,35]
cost = [5,15,30]
리턴(정답): 13
13원에 물건을 팔면 3명 모두 구입하겠지만, 배송비를 고려하여 첫번째 고객에게만 물건을 팔 것이다: 매출: 13-5=8
22원에 물건을 팔면 2명이 구입하겠지만 배송비를 고려하여 두번째 고객에게만 물건을 팔 것이다: 매출: 22-15=7
35원에 물건을 팔면 1명만이 물건을 구입할 것이다: 매출: 35-30=5
그러므로 13이 최적의 가격이다.


price = [13,22,35]
cost = [15,30,40]
리턴(정답): 0
배송비가 너무 비싸 누구에게도 팔 수 없으므로 0을 반환한다.

price = [10,10,20,20,5]
cost = [1,5,11,15,0]
리턴(정답): 10
10원에 물건을 팔면 첫번째, 두번째 고객에게 물건을 팔고 14의 총 매출을 거둘 수 잇다.
20원에 물건을 팔면 세번째, 네번째 고객에세 물건을 팔고 14의 총 매출을 거둘 수 있다.
5원에 물건을 팔면 다섯번째 고객에게 물건을 팔고 5의 총 매출을 거둘 수 있다.
10과 20이 최적의 가격이므로 이 중에서 더 작은 10을 반환한다.

price = [13,17,14,30,19,17,55,16]
cost = [12,1,5,10,3,2,40,19]
리턴(정답): 17
"""


# class Solution:
#     def solution(self, price, cost):
#         self.price = price
#         self.cost = cost
#         best_price = 0
#         for i in zip(self.price, self.cost):
#             print(i)
#
#         return 0
#
#
# if __name__ == '__main__':
#     price = [13, 22, 35]
#     cost = [0, 0, 0]
    # 13
    # my_s = Solution()
    # print(my_s.solution(price, cost))

"""
    price = [13,22,35]
    cost = [15,30,40]
    0
    
    price = [10,10,20,20,5]
    cost = [1,5,11,15,0]
    10

    price = [13,17,14,30,19,17,55,16]
    cost = [12,1,5,10,3,2,40,19]
    17
    """


"""
당신은 학교에서 집까지 도시를 거쳐 걸어가고 있다. 
도시는 무한히 크며 모든 X값에는 수직 도로가 놓여있고 모든 Y에는 수평 도로가 놓여있다. 
당신은 현재 (0, 0)에 있으며 (X, Y)에 있는 집에 가려고 한다. 
집까지 가는 방법에는 두가지가 있다: 
수평 혹은 수직으로 인접한 교차로를 거쳐 ( walkTime 초가 걸린다) 도로를 따라 걷는 것과 
몰래 대각선으로 건너 ( sneakTime 초가 걸린다) 반대쪽 모서리로 가는 방법이 있다. 
이미지에 나와있는 것처럼 걷거나 대각선을 가로지르는 8가지 방향 어느쪽으로도 가는 것이 가능하다 (예제 2번 참고).

테스트 케이스
X = 4
Y = 2
walkTime = 3
sneakTime = 10리턴(정답): 18
전혀 가로질러가지 않는 것이 가장 빠른 길이다.

X = 4
Y = 2
walkTime = 3
sneakTime = 5
리턴(정답): 16
가장 빨리 가는 방법은 두번 가로질러서 가는 길로서 경로는 다음과 같다: 
(0,0)->(1,0)->(2,1)->(3,1)->(4,2). 
도합 가로지르는데 10초가 걸리고 걷는데 6초가 걸린다.

X = 2
Y = 0
walkTime = 12
sneakTime = 10
리턴(정답): 20
다음과 같은 경로를 택할 수 있다: (0,0)->(1,1)->(2,0).

X = 1000000
Y = 1000000
walkTime = 1000
sneakTime = 1000
리턴(정답): 1000000000

X = 0
Y = 0
walkTime = 12
sneakTime = 25
리턴(정답): 0
"""