# def solution(array, commands):
#     answer = []
#     for command in commands:
#         # another_array = array[i[0]-1:i[1]]
#         # another_array.sort()
#         # answer.append(another_array[i[2]-1])
#         ####################축소 버전###################
#         i, j, k = command
#         answer.append((sorted(array[i-1:j]))[k-1])
#     return answer
#
#
# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for i in reserve:
        print('----iii------', i)
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
            continue
        if lost:
            print('----lost------', lost)
            for j in lost:
                print('----jjj------', j)
                if (j - i) == -1 or (j - i) == 1:
                    lost.remove(j)
                    reserve.remove(i)
                    print('--l&r--------', lost, reserve)
                    break
    print(len(lost))
    answer = n - len(lost)
    return answer


print(solution(4, [3, 1], [2, 4]))

'''
5	    [2, 4]	    [1, 3, 5]	    5
5	    [2, 4]	    [3]	            4
3	    [3]	        [1]	            2
4, [3, 1], [2, 4]   > 4
2, [2, 1], [1, 2]   > 2
10 [5,4,3,2,1] [3,1,2,5,4] > 10
전체 학생의 수는 2명 이상 30명 이하입니다.

체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.

여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.

여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.

여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 
남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
'''