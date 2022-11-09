import sys
from collections import deque

input = sys.stdin.readline


def DFS(starting):
    visited[starting] = 1

    for dfs_idx in graph[starting]:
        if visited[dfs_idx] == 0:
            dfs_ans.append(dfs_idx)
            DFS(dfs_idx)
    return


def BFS(starting):

    bfs_que = deque([starting])
    visited[starting] = 1

    while bfs_que:
        tmp_V = bfs_que.popleft()
        bfs_ans.append(tmp_V)

        for bfs_idx in graph[tmp_V]:
            if visited[bfs_idx] == 0:
                visited[bfs_idx] = 1
                bfs_que.append(bfs_idx)


# N : 정점의 갯수
# M : 간선의 갯수
# V : 스타팅 정점
N, M, V = list(map(int, input().split()))

graph = [[] for _ in range(N+1)]

for _ in range(M):
    X, Y = list(map(int, input().split()))
    graph[X].append(Y)
    graph[Y].append(X)

for idx in range(N+1):
    graph[idx] = sorted(graph[idx])

dfs_ans = [V]
bfs_ans = []

visited = [0 for _ in range(N+1)]
DFS(V)

visited = [0 for _ in range(N+1)]
BFS(V)

print(*dfs_ans)
print(*bfs_ans)
