N = int(input())

atm_list = list(map(int, input().split()))

atm_list = sorted(atm_list)

ans = 0
for idx_1 in range(N):
    for idx_2 in range(N-idx_1):
        ans += atm_list[idx_2]

print(ans)