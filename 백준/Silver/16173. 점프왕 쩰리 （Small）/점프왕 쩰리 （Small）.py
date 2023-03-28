def DFS(x:int, y:int):
    reach = graph[y][x]

    if reach == 0:
        return False

    for direc in dxy:
        nx = x + reach * direc[0]
        ny = y + reach * direc[1]
        if nx == N - 1 and ny == N -1:
            return True
        if 0 <= nx < N and 0 <= ny < N:
            if DFS(nx, ny):
                return True
    return False

N = int(input())
graph =[]
dxy = [[1, 0], [0, 1]]

for _ in range(N):
    graph.append(list(map(int, input().split())))

if DFS(0, 0):
    print("HaruHaru")
else:
    print("Hing")


