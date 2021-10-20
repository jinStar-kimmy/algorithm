from collections import defaultdict


# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     name = ''
#     count = dict()
#     for i in participant:
#         try: count[i] += 1
#         except: count[i] = 1
#         if i not in completion:
#             answer = i
#             return answer
#         if count[i] > 1:
#             name = i
#     return name


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()


# def solution(participant, completion):
#     set_p = set(participant)
#     set_c = set()
#     answer = ''.join(map(str, set_p.difference(completion)))
#     answer =
#     print(set_p)
#     print(answer)

'''
["leo", "kiki", "eden"]	                            ["eden", "kiki"]	                        "leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	            ["stanko", "ana", "mislav"]	                "mislav"
'''
lst = ["marina", "marina", "marina", "josipa"]
lst2 = ["josipa", "marina", "marina"]
print(solution(lst, lst2))

