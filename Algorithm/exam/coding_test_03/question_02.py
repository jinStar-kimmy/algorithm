'''
문제 설명
스미드 교수는 논리 수업을 가르친다. 어느 날 그는 다음과 같은 문장을 칠판에 썼다.
이 문장들 중 정확히 a개의 문장이 참이다.
이 문장들 중 정확히 b개의 문장이 참이다.
이 문장들 중 정확히 c개의 문장이 참이다.
.
.
.
a, b, c 등은 각각 숫자이다. 그리고 그는 학생들에게 이 중 몇개의 문장이 참인지 물어보았다.

주어진 정수 배열 statements에 Smith 교수가 쓴 숫자들이 적혀있다. 모두 몇 개의 문장이 참인지 리턴하시오.
만약 가능한 답이 두개 이상이라면 그 중 더 큰 숫자를 반환하여라. 가능한 답이 없다면 -1을 리턴하시오.

참고 / 제약 사항
statements는 1개 이상, 50개 이하의 요소를 가지고 있다.
statements의 각 요소는 0 이상, 50 이하이다.
테스트 케이스
statements = [0,1,2,3]리턴(정답): 1
2번째 문장만이 참이고 (이 문장들 중 정확히 하나의 문장만이 참이다) 나머지는 다 거짓이다.

statements = [0]리턴(정답): -1
이 문제는 역설이다. 만약 문장이 참이라면 그것은 거짓을 주장하는 것이 되고, 거짓이라면 그것이 곧 참이 된다.

statements = [0,3,1,3,2,3]리턴(정답): 3
3번째 문장이 (1개의 문장이 참이다) 참이되는 경우와 2, 4, 6번째 문장이 (3개의 문장이 참이다) 참이 되는 경우 2가지가 있다. 더 큰 숫자를 반환하여야 하므로 답은 3이 된다.

statements = [1,1]리턴(정답): 0
statements = [1]리턴(정답): 1

'''

#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.

# 숫자가 3이면 3이 3개 있어야 한다.
class Solution:
    def solution(self, statements):
        my_lst = list(set(statements))
        print(my_lst)
        my_lst.sort(reverse=True)   # 숫자 1이 1개 숫자 3이 3개 있다면 3을 출력해야 하기 때문에 큰 순서대로 정렬한다.
        for i in my_lst:
            if i == statements.count(i):
                return i

        if 0 in statements:
            return -1

        return 0
        # for i in reversed(list(set(statements))):
        #     if statements.count(i) == 1:
        #         return i
        #     if i == 0:
        #         return -1
        #     else:
        #         return 0

s1 = Solution()
result = s1.solution([0,1,2,3])
print(result)
result = s1.solution([0,3,1,3,2,3])
print(result)