def floyd(num):
    for idx_1 in range(1, num+1):
        for y_idx in range(1, num+1):
            for x_idx in range(1, num+1):
                if floyd_list[y_idx][x_idx] > floyd_list[y_idx][idx_1] + floyd_list[idx_1][x_idx]:
                    floyd_list[y_idx][x_idx] = floyd_list[y_idx][idx_1] + floyd_list[idx_1][x_idx]


N, M = list(map(int, input().split()))

floyd_list = [[101 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    start, end = list(map(int, input().split()))

    floyd_list[start][end] = 1
    floyd_list[end][start] = 1

floyd(N)

min_kebin = -1
min_sum = 9999

for y_idx in range(1, N+1):
    tmp_sum = 0
    for x_idx in range(1, N + 1):
        if y_idx != x_idx:
            tmp_sum += floyd_list[y_idx][x_idx]

    if min_sum > tmp_sum:
        min_sum = tmp_sum
        min_kebin = y_idx

print(min_kebin)

