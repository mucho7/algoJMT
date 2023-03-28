def DFS(start: int, count: int):
    visited[start] = count
    for num in graph[start]:
        if not visited[num]:
            DFS(num, count)

N, M = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

visited = [0 for _ in range(N + 1)]
ans = 0

for _ in range(M):
    start, end = list(map(int, input().split()))
    graph[start].append(end)
    graph[end].append(start)

for idx in range(1, N + 1):
    if not visited[idx]:
        ans += 1
        DFS(idx, ans)

print(ans)