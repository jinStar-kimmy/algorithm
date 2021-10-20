'''
3/4 둥근 길
시간 제한 : 2초메모리 제한 : 256MB

문제 설명
엘보니아의 왕은 width미터 * length미터 넓이의 궁전에서 살고 있다.
그는 신하들을 진흙 위에 살고 있게 하였기 때문에 인기 있는 왕은 아니었다.
그는 방문자들이 그를 접견하기 위해 오래 걷게 만들고 싶어서 궁전을 나누고 싶어했다.
왕의 보안 고문은 나선형으로 나누자고 제안했다. 방문자는 남서쪽 모서리에서 입궁하여 동쪽으로 걷는다.
방문자 앞에 벽이 나타나면 왼쪽으로 방향을 바꾼다. 나선형 복도의 너비는 1미터이다.

아래 다이어그램은 나선형 길의 한 예제이다:
방문객은 a (남서쪽 모서리)에서 출발하여 알파벳 순서대로 x (왕좌)까지 이동한다.
nmlkji
oxwvuh
pqrstg
abcdef

왕은 궁전의 길을 새로 만들기 전에 그의 왕좌를 먼저 정확한 위치로 옮기고 싶어하기 때문에 나선형의 길이 어디서 끝날지 알아야 한다.
왕좌의 좌표를 두개의 정수로 리턴하시오.

남서쪽 모서리는 (0, 0)이고 남동쪽 모서리는 (width - 1, 0), 그리고 북동쪽 모서리는 (width - 1, length - 1)이다.
                0,0       5,0   5,3
참고 / 제약 사항
width와 length는 둘 다 최소값 1, 최대값 5000의 범위를 가진다.

테스트 케이스
width = 6
length = 4  리턴(정답): [1,2]
문제 내용에 언급된 예제이다.
nmlkji
oxwvuh
pqrstg  q
abcdef

width = 6
length = 5  리턴(정답): [3,2]
nmlkji
oxwvuh
pqrstg  s
abcdef
111111

width = 1
length = 11 리턴(정답): [0,10]

width = 12
length = 50 리턴(정답): [5,6]

width = 50
length = 50 리턴(정답): [24,25]
'''

class Solution:
    def solution(self, width, length):  # 6 4       6 5
        state = 0
        x, y = 0, 0
        area = width * length       # 24            30

        while True:
            x += (width - 1)                    # 5 4                   5 4 3
            state += width                      # 6, 20                 6, 22, 30
            if state == area: return [x, y]                                     # [3, 2]

            y += (length - 1)                   # 3 2                   4 3 2
            state += (length - 1)               # 9, 21                 10, 24
            if state == area: return [x, y]

            x -= (width - 1)                    # 0 1                   0 1 2
            state += (width - 1)                # 14, 24                15, 27
            if state == area: return [x, y]             # [1, 2]

            y -= (length - 2)                   # 1                     1 2
            state += (length - 2)               # 16,                   18, 28
            if state == area: return [x, y]

            x += 1                              # 1                     1 2
            width -= 2                          # 4                     4 2
            length -= 2                         # 2                     3 1

        '''
        nmlkji
        oxwvuh
        pqrstg      q
        abcdef
        
        nmlkji
        oxwvuh
        pqrstg      s
        abcdef
        111111
        
        '''
        # coordinate = []
        # x, y = 0, 0
        # status = True
        # x_status, y_status = True, True
        # x_cnt, y_cnt = 0, 0
        #
        # for i in range(width * length, 1, -1):
        #     print(i)
        #     flag = True
        #     if i == width * length:
        #         if x + 1 >= width:
        #             status = False
        #     if flag and status:
        #         if flag and status:
        #             x += 1
        #             if x >= (width - 1 - x_cnt):
        #                 status = False
        #                 x_status = False
        #                 flag = False
        #         elif flag:
        #             x -= 1
        #             if x <= x_cnt:
        #                 status = False
        #                 x_status = True
        #                 flag = False
        #                 y_cnt += 1
        #     elif flag:
        #         if flag and y_status:
        #             y += 1
        #             if y >= (length - 1 - y_cnt):
        #                 status = True
        #                 y_status = False
        #                 flag = False
        #             elif flag:
        #                 y -= 1
        #                 if y <= y_cnt:
        #                     status = True
        #                     y_status = True
        #                     flag = False
        #                     x_cnt += 1
        #
        # coordinate.append(x)
        # coordinate.append(y)
        #
        # return coordinate


s1 = Solution()
result = s1.solution(6, 5)
print(result)
