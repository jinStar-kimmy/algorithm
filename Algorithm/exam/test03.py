from collections import deque


# def solution(bridge_length, weight, truck_weights):
#     count = 0
#     que = deque(truck_weights)
#     for i in range(len(que)):
#         count += 1
#         if que[i] + truck_weights[i] >= weight:
#
#     return count


def solution(bridge_length, weight, truck_weights):
    answer = 0
    count = [0] * len(truck_weights)
    passing = []

    while truck_weights:
        count += 1
        passing.append(truck_weights.pop(0))
        if sum(passing) > weight:
            truck_weights.insert(0, passing.pop())

        if count > bridge_length:
            passing.pop(0)
            answer += count
            count = 2
            passing.append(truck_weights.pop(0))


        # passing.append(truck_weights[0])
        # if sum(passing) > weight:
        #     passing.pop()
        # else:
        #     truck_weights.pop(0)
        #
        # if count == bridge_length:
        #     passing.pop(0)
        #     answer += count
        #     count = 0
        #     # truck_weights.pop(0)

    return answer


# bridge_length	    weight	    truck_weights
print(solution(2, 10, [7, 4, 5, 6]))   # 8
print(solution(100, 100, [10]))	    # 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110
