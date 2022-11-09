from collections import deque


def where_start(some_list):
    for y_idx in range(1, N + 1):
        for x_idx in range(1, N + 1):
            if some_list[y_idx][x_idx] == '3':
                return [y_idx, x_idx]


def bfs(maze_list, starting):

    maze_queue = deque()
    maze_queue.append(starting)

    dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while maze_queue:
        tmp = maze_queue.pop()

        for direction in dxy:
            ny = tmp[0] + direction[0]
            nx = tmp[1] + direction[1]
            if maze_list[ny][nx] == '0' and visit[ny][nx] == False:
                maze_queue.append([ny, nx])
                distance[ny][nx] = distance[tmp[0]][tmp[1]] + 1
                visit[ny][nx] = True
            elif maze_list[ny][nx] == '2':
                distance[ny][nx] = distance[tmp[0]][tmp[1]]
                return distance[ny][nx]


T = 10

for _ in range(1, T+1):
    tc = int(input())
    
    N = 16

    wall = list('1' * (N + 2))
    maze = [wall]
    for _ in range(N):
        maze.append(list('1' + input() + '1'))
    maze.append(wall)

    start = where_start(maze)

    visit = [[False for _ in range(N+2)] for _ in range(N+2)]
    distance = [[0] * (N+2) for _ in range(N+2)]

    ans = bfs(maze, start)

    if ans:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
