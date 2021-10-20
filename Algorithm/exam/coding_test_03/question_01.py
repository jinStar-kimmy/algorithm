'''
문제 설명
두개의 정수 a와 b에 대하여 a와 b 사이에 있는 모든 정수가 한번씩만 등장했을 때, 이를 정수가 연속한다고 말한다.

당신의 아들이 연속된 양의 정수를 임의의 순서대로 종이에 쓰고 있었다.
이 때, 각 숫자는 정확히 한번만 쓰여졌다. 그리고나서 그 중 하나의 숫자를 지웠다. 아들은 어느 숫자를 지웠는지 맞춰보라고 한다.

예를 들어, (10, 7, 12, 8, 11)이 종이에 남아 있었다면 지운 숫자는 9가 된다.
만약 남은 숫자가 (2, 3)이라면 지운 숫자는 1 혹은 4가 된다. 남은 숫자가 (3, 6)이라면 당신의 아들이 실수한 것이다.

종이에 남은 숫자는 numbers로 주어진다. 당신의 아들이 지웠을 가능성이 있는 모든 숫자를 정수 배열의 형태로 반환하여라.
숫자들은 높은 차순으로 정렬되어야하며 중복되는 숫자는 없어야 한다. 만약 아들이 실수를 했다면 아무것도 들어있지 않은 정수 배열을 반환하여라.

참고 / 제약 사항
numbers는 1개 이상, 50개 이하의 요소를 가진다.
numbers의 각 요소는 1 이상, 1000000000 이하이다.

테스트 케이스
numbers = [10,7,12,8,11]리턴(정답): [9]
문제 내용에 나온 예제이다.

numbers = [3,6]리턴(정답): []
문제 내용에 나온 예제이다.

numbers = [5,6,7,8]리턴(정답): [4,9]
원래 숫자 목록은 {4,5,6,7,8} 혹은 {5,6,7,8,9}가 될 수 있다.

numbers = [1000000000]리턴(정답): [999999999,1000000001]
numbers = [1,6,9,3,8,12,7,4,11,5,10]리턴(정답): [2]

'''


#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, numbers):
        numbers.sort()
        answer = []
        count = 0

        if len(numbers) == 0 or len(numbers) > 50:
            return answer

        if len(numbers) != len(set(numbers)):
            return answer

        if len(numbers) == 1:
            if numbers[0] == 0:
                answer.append(1)
                return answer
            elif numbers[0] == 1:
                answer.append(2)
                return answer
            else:
                answer.append(numbers[0] - 1)
                answer.append(numbers[0] + 1)
                return answer

        for i in range(len(numbers) - 1):
            if numbers[i] < 0 or numbers[i] > 1000000000:
                answer = []
                return answer
            # # 5,6,7,,9
            if numbers[i] + 1 == numbers[i+1]:
                continue
            elif abs(numbers[i]) - abs(numbers[i + 1]) <= -3:
                answer = []
                return answer
            else:
                answer.append(numbers[i] + 1)
                count += 1

        if len(answer) == 0:
            answer.append(numbers[0] - 1)
            if answer[0] <= 0:
                answer.pop()
            answer.append(numbers[-1] + 1)

        if count >= 2:
            answer = []
            return answer

        return answer


s1 = Solution()
result = s1.solution([1])
print(result)
result = s1.solution([1,6,9,3,8,12,7,4,11,5,10])
print(result)


