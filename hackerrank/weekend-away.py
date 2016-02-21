t = int(input())
import sys

def dfs(node, visited, cost, min_cost):

    if len(visited) == 3:
        # print(visited, cost)
        return cost

    if cost >= min_cost:
        return cost

    out = sys.maxsize
    n_visited = visited.copy()
    for path in g[node]:
        if path not in visited:
            n_visited[path] = True
            out = min(out, dfs(path, n_visited, cost + g[node][path], out))
            del n_visited[path]

    return out

for i in range(t):
    n, m = map(int, input().split())

    g = {}
    for i in range(m):
        a, b, d = map(int, input().split())

        if a not in g:
            g[a] = {}

        if b not in g:
            g[b] = {}

        g[a][b] = d
        g[b][a] = d

    # print(g)

    # dist = []
    # for i in g.keys():
    #     queue = [(i, 2, 0, {i : True})]
    #     while queue:
    #         a_node, rem_count, cost, prev = queue.pop(0)
    #         # print(a_node, rem_count, cost, prev)
    #         if rem_count == 0:
    #             # dist.append((cost, prev))
    #             dist.append(cost)
    #
    #         else:
    #             for path in g[a_node]:
    #                 if path not in prev:
    #                     a_new_prev = prev.copy()
    #                     a_new_prev[path] = True
    #                     queue.append((path, rem_count-1, cost + g[a_node][path], a_new_prev))
    #
    #
    # print(min(dist))

    out = sys.maxsize
    for i in g.keys():
        out = min(out, dfs(i, {i: True}, 0, out))

    print(out)

"""
2
5 4
1 2 1
1 3 1
3 4 10
4 5 10
4 6
1 2 2
1 3 4
1 4 8
2 3 3
2 4 3
3 4 1
"""