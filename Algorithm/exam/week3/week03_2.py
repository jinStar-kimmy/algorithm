'''
바이러스
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''


def dfs_bfs(graph, start_node):
    visted = list()
    need_visited = list()
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.pop(0)
        if node not in visted:
            visted.append(node)
            need_visited.extend(graph[node])
    print(visted)
    print(len(visted)-1)


n = int(input())
m = int(input())
lst_node = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    lst_node[x].append(y)
    lst_node[y].append(x)

dfs_bfs(lst_node, 1)
