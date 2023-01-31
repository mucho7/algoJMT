N = int(input())
dp = [[0, []] for _ in range(N + 1)]

dp[1][0] = 0
dp[1][1] = [1]

for idx in range(2, N + 1):
    dp[idx][0] = dp[idx-1][0] + 1
    dp[idx][1] = dp[idx-1][1] + [idx]
    
    if idx % 3 == 0 and dp[idx // 3][0] + 1 < dp[idx][0]:
        dp[idx][0] = dp[idx // 3][0] + 1
        dp[idx][1] = dp[idx // 3][1] + [idx]

    if idx % 2 == 0 and dp[idx // 2][0] + 1 < dp[idx][0]:
        dp[idx][0] = dp[idx // 2][0] + 1
        dp[idx][1] = dp[idx // 2][1] + [idx]

print(dp[N][0])
print(*dp[N][1][::-1])