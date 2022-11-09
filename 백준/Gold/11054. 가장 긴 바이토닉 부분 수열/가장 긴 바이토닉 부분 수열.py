N = int(input())

bitonic = list(map(int, input().split()))
bitonic_reverse = bitonic[::-1]

dp = [1] * N
dp_down = [0] * N

for idx_1 in range(N):
    for idx_2 in range(idx_1):
        if bitonic[idx_1] > bitonic[idx_2]:
            dp[idx_1] = max(dp[idx_1], dp[idx_2] + 1)
        if bitonic_reverse[idx_1] > bitonic_reverse[idx_2]:
            dp_down[idx_1] = max(dp_down[idx_1], dp_down[idx_2] + 1)


for idx in range(N):
  dp[idx] = dp[idx] + dp_down[N - idx - 1]

print(max(dp))