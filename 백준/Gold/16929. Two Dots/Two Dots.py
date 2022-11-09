def DFS(x: int, y: int, char: str, depth: int):
    if not visited[y][x]:
        visited[y][x] = depth

    for direc in dxy:
        delta_x = x + direc[0]
        delta_y = y + direc[1]
        if 0 <= delta_x < M and 0 <= delta_y < N \
                and char == graph[delta_y][delta_x] and not visited[delta_y][delta_x]:
            is_connected = DFS(delta_x, delta_y, char, depth + 1)
            if is_connected:
                return True
            visited[delta_y][delta_x] = 0
        if 0 <= delta_x < M and 0 <= delta_y < N \
                and depth >= 4 and visited[delta_y][delta_x] == 2:
            return True
    return False


N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(input())

visited = [[0 for _ in range(M)] for _ in range(N)]
dxy = [[1, 0], [0, 1], [0, -1], [-1, 0]]

ans = False

for y_idx in range(N):
    for x_idx in range(M):
        visited[y_idx][x_idx] = 2
        ans = DFS(x_idx, y_idx, graph[y_idx][x_idx], 1)
        if ans:
            print('Yes')
            break
        visited[y_idx][x_idx] = 0

    if ans:
        break
else:
    print('No')
