N, K = list(map(int, input().split()))

coins = []
for _ in range(N):
    coins.append(int(input()))

ans = [0 for _ in range(K + 1)]

for idx in range(1, K + 1):
    temp = []
    for coin in coins:
        if coin <= idx and ans[idx - coin] != -1:
            temp.append(ans[idx - coin])

    if not temp:
        ans[idx] = -1
    else:
        ans[idx] = min(temp) + 1

print(ans[K])