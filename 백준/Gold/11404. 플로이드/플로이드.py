def floyd(num):
    for idx_1 in range(1, num+1):
        for y_idx in range(1, num+1):
            for x_idx in range(1, num+1):
                if floyd_list[y_idx][x_idx] > floyd_list[y_idx][idx_1] + floyd_list[idx_1][x_idx]:
                    floyd_list[y_idx][x_idx] = floyd_list[y_idx][idx_1] + floyd_list[idx_1][x_idx]


N = int(input())
M = int(input())

inf = 10 << 20

floyd_list = [[inf for _ in range(N+1)] for _ in range(N+1)]


for _ in range(M):
    start, end, distance = list(map(int, input().split()))

    if floyd_list[start][end] != inf:
        distance = min(distance, floyd_list[start][end])

    floyd_list[start][end] = distance

floyd(N)

for y_idx in range(1, N+1):
    for x_idx in range(1, N+1):
        if x_idx == y_idx or floyd_list[y_idx][x_idx] == inf:
            print(0, end=' ')
        else:
            print(floyd_list[y_idx][x_idx], end=' ')
    print()