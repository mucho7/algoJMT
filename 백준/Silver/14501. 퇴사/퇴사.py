N = int(input())
co_list = [[0 for _ in range(N+1)] for _ in range(2)]
ans_list = [0 for _ in range(21)]

for idx in range(N):
    day, cost = list(map(int, input().split()))
    co_list[0][idx] = day
    co_list[1][idx] = cost
    ans_list[idx] = cost

for idx in range(N, -1, -1):
    if co_list[0][idx] + idx > N:
        ans_list[idx] = ans_list[idx + 1]
    else:
        ans_list[idx] = max(ans_list[idx+1], co_list[1][idx] + ans_list[idx + co_list[0][idx]])

print(ans_list[0])