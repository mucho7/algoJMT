# N : 시간
# M : 챕터 수
N, M = map(int, input().split())
pages = []
knapsack = [[0 for _ in range(N+1)] for _ in range(M+1)]

for _ in range(M):
    pages.append(list(map(int, input().split())))

pages = sorted(pages)

for idx in range(M):
    for day in range(1, N+1):
        day_cost = pages[idx][0]
        page = pages[idx][1]

        if day_cost <= day:
            knapsack[idx+1][day] = max(knapsack[idx][day], knapsack[idx][day - day_cost] + page)
        else:
            knapsack[idx+1][day] = knapsack[idx][day]

print(knapsack[M][N])
