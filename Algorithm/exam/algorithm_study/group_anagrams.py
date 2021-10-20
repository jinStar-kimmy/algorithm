'''
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

import collections
#
# a = collections.defaultdict(list)

# str_n = [""]
# print(str_n)
# print(len(str_n))
#
# str_a = ["a"]
# print(str_a)
# print(len(str_a))
#
#
# print(list("abc"))
#
# a = {"abc": "abc"}
# print(a)

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs.sort()     # ['ate', 'bat', 'eat', 'nat', 'tan', 'tea']
word_dict = collections.defaultdict(list)
# spelling_list = list()

for word in strs:
    spelling = ''.join(sorted(list(word)))
    word_dict[spelling].append(word)  # {'aet': ['ate', 'eat', 'tea'], 'abt': ['bat'], 'ant': ['nat', 'tan']}

    # spelling_list.append(word_dict[word])

# word_count = collections.Counter(word_dict.values())  # Counter({'aet': 3, 'ant': 2, 'abt': 1})

print(word_dict.values())

answer = list()
for key in word_dict.keys():
    answer.append(word_dict[key])

print(answer)

# s = "acbabd!!!!!!"
# print("sssssss=====" + s[1:1])
# print(s.upper())    # no error
