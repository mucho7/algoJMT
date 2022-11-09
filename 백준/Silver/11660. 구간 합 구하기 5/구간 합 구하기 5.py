import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

N_list = [[0 for _ in range(N+1)] for _ in range(N+1)]

for y_idx in range(1, N+1):
    tmp = list(map(int, input().split()))

    for x_idx in range(1, N+1):
        N_list[y_idx][x_idx] = N_list[y_idx][x_idx - 1] + N_list[y_idx - 1][x_idx] + tmp[x_idx - 1] - N_list[y_idx - 1][x_idx - 1]

for _ in range(M):
    x1, y1, x2, y2 = list(map(int, input().split()))
    ans = N_list[x2][y2] - N_list[x1 - 1][y2] - N_list[x2][y1 - 1] + N_list[x1 - 1][y1 - 1]
    print(ans)