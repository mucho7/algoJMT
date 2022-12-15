import sys
from collections import deque


def make_it_rich():
    while rich:
        x_axis, y_axis = rich.popleft()
        for direc in dxy:
            nx, ny = x_axis + direc[0], y_axis + direc[1]
            if 0 <= nx < M and 0 <= ny < N:
                if tomato[ny][nx] == 0:
                    tomato[ny][nx] = tomato[y_axis][x_axis] + 1
                    rich.append([nx, ny])


input = sys.stdin.readline

M, N = list(map(int, input().split()))
tomato = []
rich = deque()
ans = 0

for y_idx in range(N):
    tomato.append(list(map(int, input().split())))

    for x_idx in range(M):
        if tomato[y_idx][x_idx] == 1:
            rich.append([x_idx, y_idx])

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

make_it_rich()

flag = False
for y_idx in range(N):
    for x_idx in range(M):
        if tomato[y_idx][x_idx] == 0:
            flag = True
            print(-1)
            break
        if ans < tomato[y_idx][x_idx]:
            ans = tomato[y_idx][x_idx]
    if flag:
        break
if not flag:
    print(ans -1)