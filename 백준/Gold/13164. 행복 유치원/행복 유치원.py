N, K = map(int, input().split())
children = list(map(int, input().split()))

diff = []
for idx in range(N - 1):
    diff.append(children[idx + 1] - children[idx])
diff = sorted(diff)

ans = 0
for idx in range(N-K):
    ans += diff[idx]

print(ans)