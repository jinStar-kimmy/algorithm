'''
4 5 1           1 2 4 3
1 2             1 2 3 4
1 3
1 4             start_node = 1  (시작 노드(정점))
2 4             E = 5 (간선 수)
3 4             V = 4 (노드(정점) 수)

    1 - 2       dfs: 1 2 4 3
    |   |
    3 - 4       bfs: 1 2 3 4

5 5 3
5 4
5 2
1 2
3 4
3 1
'''


def dfs(start_node):
    print(start_node, end=' ')
    visited.append(start_node)
    for i in lst_node[start_node]:
        if i not in visited:
            dfs(i)


def bfs(lst_node, start_node):
    visited, need_visited = list(), list()
    need_visited.append(start_node)
    while need_visited:
        node = need_visited.pop(0)
        if node not in visited:
            visited.append(node)
            need_visited.extend(lst_node[node])
            print(visited[-1], end=' ')


n, m, v = map(int, input().split())
lst_node = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    lst_node[x].append(y)
    lst_node[y].append(x)

for i in lst_node:
    i.sort()

visited = list()

dfs(v)
print()
bfs(lst_node, v)


# def dfs(lst_node, start_node):
#     # dfs_lst_node = lst_node
#     # print("dfs: ", lst_node)
#     # for i in range(1, len(lst_node)):
#     #     lst_node[i].reverse()
#
#     print("dfs - reverse: ", lst_node)
#     visited, need_visited = list(), list()
#     need_visited.append(start_node)
#
#     while need_visited:
#         if need_visited[-1] == min(need_visited):
#             node = need_visited.pop()
#         else:
#             node = need_visited.pop(0)
#         if node not in visited:
#             visited.append(node)
#             need_visited.extend(lst_node[node])
#
#     print("dfs: ", visited)
#     print("============================================")
#
#
# def bfs(lst_node, start_node):
#     bfs_lst_node = lst_node
#     print("bfs: ", lst_node)
#     for i in range(1, len(lst_node)):
#         lst_node[i].sort()
#     visited, need_visited = list(), list()
#     need_visited.append(start_node)
#
#     while need_visited:
#         node = need_visited.pop(0)
#         if node not in visited:
#             visited.append(node)
#             need_visited.extend(lst_node[node])
#             print(need_visited)
#
#     print("bfs: ", visited)
#
#
# n, m, v = map(int, input().split())
# lst_node = [[] for _ in range(n + 1)]
#
# for _ in range(m):
#     x, y = map(int, input().split())
#     lst_node[x].append(y)
#     lst_node[y].append(x)
#
# print(lst_node)
# print("============================================")
# for i in lst_node:
#     i.sort()
#
# bfs_lst_node = lst_node
# dfs_lst_node = lst_node
# print(lst_node)
# print("dfs: ", dfs_lst_node)
# print("bfs: ", bfs_lst_node)
# print("============================================")
#
# dfs(lst_node, v)
# bfs(lst_node, v)






