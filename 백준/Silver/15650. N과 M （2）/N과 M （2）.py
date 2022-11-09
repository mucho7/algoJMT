from itertools import combinations

N, M = list(map(int, input().split()))

N_list = [idx for idx in range(1, N+1)]
ans_list = list(combinations(N_list, M))

for ans in ans_list:
    print(*ans)