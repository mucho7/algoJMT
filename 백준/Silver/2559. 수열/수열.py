N, K = list(map(int, input().split()))

temperature = [0] + list(map(int, input().split()))
prefix_sum = [0] * (N + 1)

ans = -9999999

for idx in range(1, N+1):
    prefix_sum[idx] = prefix_sum[idx-1] + temperature[idx]

for idx in range(N-K+1):
    tmp = prefix_sum[idx + K] - prefix_sum[idx]
    if ans < tmp:
        ans = tmp

print(ans)