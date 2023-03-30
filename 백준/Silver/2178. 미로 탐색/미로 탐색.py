import sys
from collections import deque
input = sys.stdin.readline


def BFS(x: int, y: int, depth: int):
    que = deque([(x, y)])
    visited[y][x] = 1

    while que:
        x, y = que.popleft()
        for direc in dxy:
            nx = x + direc[0]
            ny = y + direc[1]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] and not visited[ny][nx]:
                    que.append([nx, ny])
                    visited[ny][nx] = 1
                    graph[ny][nx] = graph[y][x] + 1
    return graph[N - 1][M - 1]



N, M = list(map(int, input().split()))
graph = []
dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
visited = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    nums = list(map(int, input().rstrip()))
    graph.append(nums)

BFS(0, 0, 1)
print(graph[N - 1][M - 1])