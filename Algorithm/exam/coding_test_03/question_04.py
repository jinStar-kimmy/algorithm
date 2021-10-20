'''
4/4 가방 퀴즈
시간 제한 : 2초메모리 제한 : 256MB
문제 설명
1부터 n까지 번호가 붙여진 n개의 가방이 있다. 각 가방은 다른 가방에 넣을 수 있으며,
다른 가방에 들어간 가방 역시 다른 가방을 넣고 있을 수 있다.
문제의 명확성을 위해 가방 i가 가방 j의 안에 있다는 것은 가방 i가 가방 j에 직접적으로 들어있음을 의미한다.
예를 들어서, 가방 2가 가방 1 안에 있고, 가방 3이 가방 2 안에 있으면, 가방 3은 가방 2 안에 있지만 가방 1 안에 있지는 않다.

모든 가방은 처음에 다 빈 채로 바닥에 놓여 있다.
우리는 다음에 나열되는 것들 중 하나의 행동을 각각 단계적으로 취할 것이다.

PUT i INSIDE j - 가방 i를 가방 j안에 넣는다. 이 행동을 취하기 위해서는 가방 i와 j는 반드시 바닥에 놓여있어야 한다.
SET i LOOSE - 가방 i안에 있는 모든 가방을 다시 꺼내서 바닥에 놓는다. 이 행동을 취하기 위해서는 가방 i는 반드시 바닥에 놓여 있어야 한다.
SWAP i WITH j - 가방 i와 가방 j의 내용물을 서로 바꾼다
(다시 말하면, 가방 i의 모든 내용물을 꺼내서 가방 j에 넣고, 가방 j의 모든 내용물을 꺼내서 가방 i에 넣는다).
이 행동을 취하기 위해서는 가방 i와 j는 반드시 바닥에 놓여 있어야 한다.

가방들이 놓여진 마지막 상태에서 어떤 가방도 자기보다 더 작은 번호의 가방 안에 들어가 있지 않을 때, 이 상태를 적절하다고 말한다.
주어진 가방의 개수 n과 취할 행동의 단계 actions를 이용하여 마지막 상태가 적절한지 판단하여라.
만약 적절하다면 마지막 상태에 바닥에 놓인 가방의 개수를 반환하여라. 적절하지 않거나 어느 단계의 행동이 유효하지 않다면 -1을 반환하여라.

참고 / 제약 사항
n은 1 이상, 50 이하이다.
actions는 0개 이상, 50개 이하의 요소를 가진다.
actions의 각 요소는 "PUT i INSIDE j" (이 때, i와 j는 1부터 n사이의 서로 다른 두 정수이며 leading zero는 없다),
혹은 "SET i LOOSE" (이 때, i는 1부터 n사이의 정수이며 leading zero는 없다),
혹은 "SWAP i WITH j" (이 때, i와 j는 1부터 n사이의 서로 다른 두 정수이며 leading zero는 없다)와 같은 형태로 이루어지며 따옴표는 문자열에 포함되지 않는다.


테스트 케이스
n = 2
actions = ["PUT 1 INSIDE 2"]리턴(정답): 1
가방 1이 가방 2 안에 들어가 있으므로 적절한 상태이고 오직 하나의 가방만이 바닥에 놓여있다.

n = 2
actions = ["PUT 1 INSIDE 2","SET 2 LOOSE"]리턴(정답): 2
처음 상태와 마지막 상태가 동일하게 된다.

n = 2
actions = ["PUT 2 INSIDE 1"]리턴(정답): -1
가방 2가 가방 1 안에 들어가 있으므로, 더 적은 숫자의 가방 안에 들어가 있게 된다. 따라서 이 경우는 부적절한 상태이다.

n = 4
actions = ["PUT 3 INSIDE 2","SWAP 4 WITH 2","PUT 2 INSIDE 4","SET 1 LOOSE"]리턴(정답): 2
n = 3
actions = ["PUT 1 INSIDE 2","PUT 3 INSIDE 1"]리턴(정답): -1
마지막 행동은 가방 1이 바닥에 놓여 있지 않으므로 유효하지 않다.

'''


class Solution:
    def solution(self, n, actions):
        bags = [[] for _ in range(n+1)] # 빈 가방 만들기
        # print(bags)
        check = [1] * (n+1)
        # print(check)

        for action in actions:
            action = action.split()
            if action[0] == "PUT":
                x, y = int(action[1]), int(action[3])
                if not check[x] or not check[y]:
                    return -1
                bags[y].append(x)
                check[x] = 0

            elif action[0] == "SET":
                i = int(action[1])
                if not check[i]: return -1


s1 = Solution()
result = s1.solution(2, ["PUT 1 INSIDE 2"])
