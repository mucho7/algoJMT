N, K = map(int, input().split())
ans = [[0 for _ in range(201)] for _ in range(201)]

for idx in range(N + 1):
    ans[1][idx] = 1
    ans[2][idx] = idx + 1

for y_idx in range(2, 201):
    ans[y_idx][1] = y_idx
    for x_idx in range(2, 201):
        ans[y_idx][x_idx] = (ans[y_idx][x_idx - 1] + ans[y_idx - 1][x_idx]) % 1000000000

print(ans[K][N])