N = int(input())
cost = [0 for _ in range(N+1)]

for idx in range(1, N+1):
    work_tmp = list(map(int, input().split()))
    if work_tmp[1]:
        for pre_idx in work_tmp[2:]:
            cost[idx] = max(cost[idx], cost[pre_idx] + work_tmp[0])
    else:
        cost[idx] = work_tmp[0]
print(max(cost))