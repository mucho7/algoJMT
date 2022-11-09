N, M = map(int, input().split())

coin_list = []
for _ in range(N):
    coin_list.append(int(input()))

ans = 0
while M != 0:
    for idx in range(N-1, -1, -1):
        while M >= coin_list[idx]:
            M -= coin_list[idx]
            ans += 1
print(ans)