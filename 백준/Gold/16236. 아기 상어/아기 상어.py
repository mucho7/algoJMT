import sys
from collections import deque 
input = sys.stdin.readline


def moveShark(shark: list, shark_size: int):
    """
    BFS를 통해 shark를 이동시키는 함수
    물고기를 먹으러 가는데 필요한 최소한의 이동과 상어의 위치를 반환
    """
    result = deque()
    result.append(shark)

    distance = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[shark[1]][shark[0]] = 1

    temp = []


    while result:
        cur_x, cur_y = result.popleft()

        for direc in dxy:
            nx = cur_x + direc[0]
            ny = cur_y + direc[1]

            if 0 <= nx < N and 0 <= ny < N and shark_size >= graph[ny][nx] and not visited[ny][nx]:
                result.append([nx, ny])
                visited[ny][nx] = 1
                distance[ny][nx] = distance[cur_y][cur_x] + 1

                if graph[ny][nx] < shark_size and graph[ny][nx]:
                    temp.append([nx, ny, distance[ny][nx]])

    return sorted(temp, key=lambda x: (-x[2], -x[1], -x[0]))


N = int(input())
graph = []
shark_size = 2
stomache = 0
ans = 0

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]


for y_idx in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

    for x_idx in range(N):
        if row[x_idx] == 9:
            shark = [x_idx, y_idx]


for _ in range(N ** 2):

    temp = moveShark(shark, shark_size)
    
    if not temp:
        break
    
    move_x, move_y, move = temp.pop()
    

    graph[shark[1]][shark[0]] = 0
    shark = [move_x, move_y]
    graph[move_y][move_x] = 0

    ans += move
    stomache += 1

    if stomache == shark_size:
        stomache = 0
        shark_size += 1

print(ans)