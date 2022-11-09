from collections import deque

T = int(input())

for _ in range(T):
    I = int(input())

    start_X, start_Y = list(map(int, input().split()))
    end_X, end_Y = list(map(int, input().split()))

    visited = [[0 for _ in range(I)] for _ in range(I)]
    visited[start_X][start_Y] = 1

    dxy = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

    tmp_que = deque([[start_X, start_Y]])
    while tmp_que:
        cur_X, cur_Y = tmp_que.popleft()
        for move_X, move_Y in dxy:
            tmp_X = cur_X + move_X
            tmp_Y = cur_Y + move_Y
            if -1 < tmp_X < I and -1 < tmp_Y < I and visited[tmp_X][tmp_Y] == 0:
                tmp_que.append([tmp_X, tmp_Y])
                visited[tmp_X][tmp_Y] = visited[cur_X][cur_Y] + 1

    print(visited[end_X][end_Y] - 1)