def DFS(index: int, starting: int, depth: int, cost: int):
    for idx in range(N):
        if city_cost[index][idx] and not visited[idx]:
            visited[idx] = 1
            cost += city_cost[index][idx]
            depth += 1

            DFS(idx, starting, depth, cost)

            visited[idx] = 0
            cost -= city_cost[index][idx]
            depth -= 1
    if depth == N - 1 and city_cost[index][starting]:
        result_list.append(cost + city_cost[index][starting])


N = int(input())
city_cost = [list(map(int, input().split())) for _ in range(N)]

visited = [0 for _ in range(N)]
result_list = []

for start in range(N):
    visited[start] = 1
    DFS(start, start, 0, 0)
    visited[start] = 0

print(min(result_list))
