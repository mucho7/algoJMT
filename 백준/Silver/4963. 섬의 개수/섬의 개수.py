import sys
sys.setrecursionlimit(10 ** 6)

def DFS(x:int, y:int, number: int):
    visited[y][x] = 1
    
    for direc in dxy:
        nx = x + direc[0]
        ny = y + direc[1]
        if 0 <= nx < w and 0 <= ny < h:
            if graph[ny][nx] != 0 and not visited[ny][nx]:
                DFS(nx, ny, number)


dxy = [
        [0, 1], [0, -1],[-1, 1],[-1, -1],
        [1, 0], [-1, 0],[1, -1],[1, 1],
    ]

w = h = -1

while True:
    ans = 0
    w, h = list(map(int, input().split()))
    if w == 0 and h == 0:
        break
    
    graph = []
    visited = [[0 for _ in range(w)] for _ in range(h)]

    for _ in range(h):
        data = list(map(int, input().split()))
        graph.append(data)

    for y_idx in range(h):
        for x_idx in range(w):
            if not visited[y_idx][x_idx] and graph[y_idx][x_idx]:
                ans += 1
                DFS(x_idx, y_idx, ans)

    print(ans)